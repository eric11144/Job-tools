#!/bin/bash

# Function: Display help message
function show_help() {
    echo "Usage: $0 <package_name>"
    echo "       $0 -h"
    echo
    echo "This script downloads a package and all its dependencies as .deb files."
    echo
    echo "Arguments:"
    echo "  package_name    The name of the package to download."
    echo "  -h              Display this help message."
    exit 0
}

# Step 1: Check for -h or missing arguments
echo "========================= STAGE 1: Argument Validation ========================="
echo "Timestamp: $(date)"
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    show_help
elif [ -z "$1" ]; then
    echo "[ERROR] No package name provided."
    show_help
fi
PACKAGE_NAME="$1"
OUTPUT_DIR="${PACKAGE_NAME}_packages"
echo "[SUCCESS] Arguments validated."

# Step 2: Create a directory to store downloaded files
echo "========================= STAGE 2: Directory Setup ============================"
echo "Timestamp: $(date)"
mkdir -p "$OUTPUT_DIR" && echo "[SUCCESS] Directory created: $OUTPUT_DIR"

# Step 3: Check network connection
echo "========================= STAGE 3: Network Check =============================="
echo "Timestamp: $(date)"
if ! ping -c 1 -W 3 google.com > /dev/null 2>&1; then
    echo "[ERROR] No internet connection. Please check your network and try again."
    exit 1
fi
echo "[SUCCESS] Internet connection is OK."

# Step 4: Check and install apt-rdepends
echo "========================= STAGE 4: Install apt-rdepends ======================="
echo "Timestamp: $(date)"
if ! command -v apt-rdepends > /dev/null; then
    echo "Installing apt-rdepends..."
    sudo apt-get update && sudo apt-get install -y apt-rdepends
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install apt-rdepends."
        exit 1
    fi
fi
echo "[SUCCESS] apt-rdepends is installed."

# Step 5: Resolve dependencies
echo "========================= STAGE 5: Resolve Dependencies ======================="
echo "Timestamp: $(date)"
apt-rdepends -p "$PACKAGE_NAME" | grep -E "^ " | awk '{print $1}' | grep -vE "Depends|PreDepends" > dependencies.txt
if [ ! -s dependencies.txt ]; then
    echo "apt-rdepends failed, using apt-cache depends as fallback..."
    apt-cache depends "$PACKAGE_NAME" | grep "Depends:" | awk '{print $2}' > dependencies.txt
fi
echo "$PACKAGE_NAME" >> dependencies.txt
sort -u dependencies.txt -o dependencies.txt
echo "[SUCCESS] Dependencies resolved."

# Step 6: Download packages
echo "========================= STAGE 6: Download Packages =========================="
echo "Timestamp: $(date)"
while read -r pkg; do
    echo "Downloading package: $pkg"
    if apt-get download "$pkg"; then
        echo "[SUCCESS] Downloaded: $pkg"
        mv "$pkg"*.deb "$OUTPUT_DIR"/ 2>/dev/null
        echo "------------------------------------------------------------------------"
    else
        echo "[ERROR] Failed to download: $pkg" >> error.log
    fi
done < dependencies.txt
echo "[SUCCESS] All packages downloaded."

# Final Stage: Completion
echo "========================= STAGE 7: Completion ================================="
echo "Timestamp: $(date)"
echo "[SUCCESS] Package download complete."
echo "Files are stored in: $OUTPUT_DIR"
echo "========================= $PACKAGE_NAME Package Download Complete ==========================="
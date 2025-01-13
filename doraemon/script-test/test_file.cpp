#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <thread>
#include <vector>
#include <filesystem>
#include <iomanip>

namespace fs = std::filesystem;

class DataLogger {
public:
    DataLogger(const std::string& baseDir, size_t maxFileSize, size_t maxFiles)
        : baseDir_(baseDir), maxFileSize_(maxFileSize), maxFiles_(maxFiles) {
        if (!fs::exists(baseDir_)) {
            fs::create_directory(baseDir_);
        }
        openNewFile();
    }

    void writeData() {
        auto now = std::chrono::system_clock::now();
        std::time_t now_c = std::chrono::system_clock::to_time_t(now);
        std::stringstream ss;
        ss << std::put_time(std::localtime(&now_c), "%F %T");

        std::string data = "1 61 121 3 183 0 1 [0, 0] Pass " + ss.str() + " FALSE\n";
        if (currentFileSize_ + data.length() >= maxFileSize_) {
            openNewFile();
        }

        fileStream_ << data;
        currentFileSize_ += data.length();
    }

private:
    std::ofstream fileStream_;
    std::string baseDir_;
    size_t maxFileSize_;
    size_t maxFiles_;
    size_t currentFileSize_ = 0;

    void openNewFile() {
        if (fileStream_.is_open()) {
            fileStream_.close();
            currentFileSize_ = 0;
        }

        auto now = std::chrono::system_clock::now();
        std::time_t now_c = std::chrono::system_clock::to_time_t(now);
        std::stringstream fileName;
        fileName << baseDir_ << "/Log_" << std::put_time(std::localtime(&now_c), "%Y-%m-%d_%H-%M-%S") << ".txt";

        fileStream_.open(fileName.str());
        fileStream_ << "Unit Grab Time Test Time Storage Time Cycle Time UPH StartKey ErrorCode Result Current Time DMC ByPass\n";
        currentFileSize_ = fileStream_.tellp();

        cleanOldFiles();
    }

    void cleanOldFiles() {
        std::vector<fs::path> files;
        for (const auto& entry : fs::directory_iterator(baseDir_)) {
            files.push_back(entry.path());
        }
        sort(files.begin(), files.end(), [](const fs::path& a, const fs::path& b) {
            return fs::last_write_time(a) < fs::last_write_time(b);
        });
        while (files.size() > maxFiles_) {
            fs::remove(files.front());
            files.erase(files.begin());
        }
    }
};

int main() {
    DataLogger logger("logs", 64 * 1024 * 1024, 1000); // 64MB, 1000 files

    while (true) {
        logger.writeData();
        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // 每10毫秒写入一次
    }

    return 0;
}
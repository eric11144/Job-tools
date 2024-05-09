
#include <cstdint>
#include <fstream>
#include <iostream>
#include <ios>
#include <chrono>
#include <thread>
#include <filesystem>

using MyClock = std::chrono::system_clock;
using MyDateTime = std::chrono::time_point<MyClock>;

// Size constants
const uint64_t c_1KB = 1024l;
const uint64_t c_1MB = 1024l * c_1KB;
const uint64_t c_1GB = 1024l * c_1MB;
const uint64_t c_1TB = 1024l * c_1GB;


uint64_t parseSize(std::string s, uint64_t const defaultValue)
{
    std::basic_string <char>::size_type index1;
    uint64_t factor = 1;
    uint64_t value = 0;
    if (s == "") { return defaultValue; }
    try {
        if ((index1 = s.find("TB")) != std::string::npos) {
            s.erase(index1, std::string::npos);
            factor = c_1TB;
        } else if ((index1 = s.find("GB")) != std::string::npos) {
            s.erase(s.begin() + index1, s.end() - 1);
            factor = c_1GB;
        } else if ((index1 = s.find("MB")) != std::string::npos) {
            s.erase(s.begin() + index1, s.end() - 1);
            factor = c_1MB;
        } else if ((index1 = s.find("KB")) != std::string::npos) {
            s.erase(s.begin() + index1, s.end() - 1);
            factor = c_1KB;
        }
        value = std::stoull(s);
        return factor * value;
    }
    catch (...) {
        return defaultValue;
    }
}

std::string fmtSize(uint64_t value)
{
    double val = value;
	int unit = 0;
	while (val >= 1024.0) {
		val = val / 1024.0;
		unit++;
	}

	std::string unitstr;
	switch (unit) {
	case 0: unitstr = " Byte"; break;
	case 1: unitstr = " KByte"; break;
	case 2: unitstr = " MByte"; break;
	case 3: unitstr = " GByte"; break;
	case 4: unitstr = " TByte"; break;
	default: unitstr = " unknown unit"; break;
    }

    return std::to_string(val) + unitstr;
}

std::string fmtRate(double value)
{
	int unit = 0;
	while (value > 1024.0) {
		value = value / 1024.0;
		unit++;
	}

	std::string unitstr;
	switch (unit) {
	case 0: unitstr = " Bytes/s"; break;
	case 1: unitstr = " KBytes/s"; break;
	case 2: unitstr = " MBytes/s"; break;
	case 3: unitstr = " GBytes/s"; break;
	default: unitstr = " unknown unit"; break;
    }

    return std::to_string(value) + unitstr;
}

void printUsage()
{
    std::cout << std::endl;
    std::cout << "Usage: writedata [options] <file>" << std::endl;
    std::cout << std::endl;
    std::cout << "    -t <bytes>      Number of bytes to write (''|KB|MB|GB|TB)" << std::endl;
    std::cout << "    -b <bytes>      Number of bytes in each write (''|KB|MB|GB|TB)" << std::endl;
    std::cout << "    -p <us>         Time between each write" << std::endl;
    std::cout << std::endl;
}

int main(int argc, char* argv[])
{
    uint64_t total = 20l * c_1GB;
    uint64_t block = 10l * c_1KB;
    uint64_t period = 300l;
    std::string filename;

    for (int i = 1; i < argc; i++) {
        std::string const arg = argv[i];
        uint64_t* puint64Size = nullptr;
        uint64_t* puint64 = nullptr;

        if ((arg == "-?") || (arg == "-h") || (arg == "--help")) {
            printUsage();
		    std::cout << "Parameters, Total: " << fmtSize(total) << 
                        ", Block size: " << fmtSize(block) << 
                        ", period [us]: " << period << 
                        ", File: " << filename << "\n\n";
            return 0;
        }
        else if (arg == "-t") {
            puint64Size = &total;
        }
        else if (arg == "-b") {
            puint64Size = &block;
        }
        else if (arg == "-p") {
            puint64 = &period;
        }
        else {
            filename = arg;
        }

        if ((puint64Size != nullptr) && ((i + 1) < argc)) {
            i++;
            *puint64Size = parseSize(argv[i], *puint64Size);
            puint64Size = nullptr;
        }
        if ((puint64 != nullptr) && ((i + 1) < argc)) {
            i++;
            *puint64 = std::stoull(argv[i]);
            puint64 = nullptr;
        }
    }

    std::cout << "Parameters, Total: " << fmtSize(total) << 
                 ", Block size: " << fmtSize(block) << 
                 ", period [us]: " << period << 
                 ", File: " << filename << "\n\n";

	const auto period_us = std::chrono::microseconds(period);

	char* pBuf = new char[block];

	std::ofstream outfile;
	outfile.open(filename.c_str(), std::ios::binary|std::ios::out);

    // =============================================================

    MyDateTime starttime = MyClock::now();
    
	uint64_t left = total;
	while (left > 0) {
		uint64_t num = block;
		if (num > left) { num = left; }
		outfile.write(pBuf, num);
		left -= num;
		std::this_thread::sleep_for(period_us);
	}

    MyDateTime stoptime = MyClock::now();

    // =============================================================

	auto dur_us = std::chrono::duration_cast<std::chrono::microseconds>(stoptime - starttime);

	double rate = (total * 1000000l ) / dur_us.count();

	std::cout << "Took " << dur_us.count() << " us, Written data with " << fmtRate(rate) << "\n";

    return 0;
}



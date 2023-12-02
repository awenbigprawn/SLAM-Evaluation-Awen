#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <gflags/gflags.h>

#include <boost/filesystem.hpp>  // to create folders
#include <boost/foreach.hpp>

// Wrapper for std::ofstream to open/close it when created/destructed.
class OfstreamWrapper {
 public:
  OfstreamWrapper(const std::string& filename,
                  const bool& open_file_in_append_mode = false);
  virtual ~OfstreamWrapper();
  void closeAndOpenLogFile();

 public:
  std::ofstream ofstream_;
  const std::string filename_;
  const std::string output_path_;
  const bool open_file_in_append_mode = false;

 protected:
  void openLogFile(const std::string& output_file_name,
                   bool open_file_in_append_mode = false);
};

class EurocGtLogger {
 public:
  EurocGtLogger();
  virtual ~EurocGtLogger() = default;

  /**
   * @brief logGtData Simply copy-pastes the file given as input to the
   * file output_gt_poses.csv inside the output folder.
   * @param gt_file file where the data.csv file in Euroc is located.
   * Usually inside `mav0/state_groundtruth_estimate0/data.csv`.
   */
  void logGtData(const std::string& gt_file);

 private:
  // Filenames to be saved in the output folder.
  OfstreamWrapper output_gt_poses_csv_;
};

class AwenLogger {
 public:
    AwenLogger();
    ~AwenLogger();
    void setLogger();

    double feature_tracker_time;
    double process_time;
    double solver_cost;
    double whole_marginalization_cost;
    double whole_time_for_ceres;
    void logTiming();

 private:
    OfstreamWrapper output_timing_csv_;
    bool is_header_written_timing_ = false;
};

// Open files with name output_filename, and checks that it is valid
static inline void OpenFile(const std::string& output_filename,
                            std::ofstream* output_file,
                            bool append_mode = false) {
  //CHECK_NOTNULL(output_file);
  output_file->open(output_filename.c_str(),
                    append_mode ? std::ios_base::app : std::ios_base::out);
  output_file->precision(20);
  //CHECK(output_file->is_open()) << "Cannot open file: " << output_filename;
  //CHECK(output_file->good()) << "File in bad state: " << output_filename;
}


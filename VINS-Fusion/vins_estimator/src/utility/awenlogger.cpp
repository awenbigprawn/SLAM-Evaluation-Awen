#include "awenlogger.h"

DEFINE_string(output_path, "./", "Path where to store VIO's log output.");

AwenLogger::AwenLogger()
    : output_timing_csv_("output_timing.csv") {}

void AwenLogger::setLogger(){

    feature_tracker_time=0;
    process_time=0;
    solver_cost=0;
    whole_marginalization_cost=0;
    whole_time_for_ceres=0;
}

void AwenLogger::logTiming(){
    std::ofstream& output_stream = output_timing_csv_.ofstream_;
    bool& is_header_written = is_header_written_timing_;

    if(is_header_written){
        output_stream << "feature_tracker_time,process_time,"
                      << "solver_cost,whole_marginalization_cost,"
                      << "whole_time_for_ceres"<< std::endl;
        is_header_written = true;
    }

    output_stream << feature_tracker_time <<","
                  << process_time <<","
                  << solver_cost <<","
                  << whole_marginalization_cost <<","
                  << whole_time_for_ceres 
                  << std::endl;

}

OfstreamWrapper::OfstreamWrapper(const std::string& filename,
                                 const bool& open_file_in_append_mode)
    : filename_(filename), output_path_(FLAGS_output_path) {
  openLogFile(filename, open_file_in_append_mode);
}

// This destructor will directly close the log file when the wrapper is
// destructed. So no need to explicitly call .close();
OfstreamWrapper::~OfstreamWrapper() {
  ofstream_.close();
}

void OfstreamWrapper::closeAndOpenLogFile() {
  ofstream_.close();
  OpenFile(output_path_ + '/' + filename_, &ofstream_, false);
}

void OfstreamWrapper::openLogFile(const std::string& output_file_name,
                                  bool open_file_in_append_mode) {
  OpenFile(output_path_ + '/' + output_file_name,
           &ofstream_,
           open_file_in_append_mode);
}

/* ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
EurocGtLogger::EurocGtLogger() : output_gt_poses_csv_("traj_gt.csv") {}

void EurocGtLogger::logGtData(const std::string& file_path) {
  std::ifstream f_in(file_path.c_str());
  // Drop first line, we want to use our own header.
  std::string dummy_header;
  std::getline(f_in, dummy_header);

  std::ofstream& output_stream = output_gt_poses_csv_.ofstream_;
  // First, write header
  output_stream << "#timestamp,x,y,z,qw,qx,qy,qz,vx,vy,vz,"
                << "bgx,bgy,bgz,bax,bay,baz" << std::endl;
  // Then, copy all gt data to file
  output_stream << f_in.rdbuf();

  // Clean
  f_in.close();
}

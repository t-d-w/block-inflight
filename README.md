# block-inflight
Track current amount of inflight requests to a block device.

Polls the file /sys/block/BLOCK DEVICE/inflight file. For example, if you want to track how many requests are in flight against sda the block-inflight is tracking the file /sys/block/sda/inflight. 

# Usage
Block device and filename are required arguments. You can optionally specify verbosity although it adds overhead. Here's the usage:
  
usage: block-inflight.py [-h] -d DEVICE -f FILENAME [-v]

optional arguments:
  
  -h, --help            show this help message and exit
  
  -d DEVICE, --device DEVICE
                        Block device you want to track inflights for
  
  -f FILENAME, --filename FILENAME
                        File name for CSV file that will store all the data
  
  -v, --verbose         Enable verbose output
  
# Installation

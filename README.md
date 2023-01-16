# block-inflight
Track current amount of inflight requests to a block device.

Polls the file /sys/block/<devlabel>/inflight file.

## Usage
usage: block-inflight.py [-h] -d DEVICE -f FILENAME [-v]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
                        Block device you want to track inflights for
  -f FILENAME, --filename FILENAME
                        File name for CSV file that will store all the data
  -v, --verbose         Enable verbose output
  
  

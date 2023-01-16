import sys
import datetime
import time
import argparse
import functools
import signal
import numpy as np

def get_inflight(device, verbose):
    inflight_file = "/sys/block/" + device + "/inflight"
    inflight_contents = open(inflight_file, 'r').read()
    if verbose == 1:
        print("inflight file: \n" + inflight_contents)
    return inflight_contents

def parse_inflight(inf_file, verbose):
    thelist = inf_file.split()
    if verbose == 1:
        print(thelist)
        print("\n")
    return thelist

def collect_and_record(dev, record_name, verbose):
    inflight_content = get_inflight(dev, 0)
    inflight_list = parse_inflight(inflight_content, 0)
    rinf = inflight_list[0]
    winf = inflight_list[1]
    if verbose == 1:
        print("Reads in flight: " + rinf + "\t" + "Writes in flight: " + winf)

    # get timestamp

    #timestamp = str(datetime.datetime.now().timestamp())
    timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    

    append_str = timestamp_str + "," + rinf + "," + winf + "\n"
    
    #if verbose == 1:
    #    print("append string to csv: " + append_str)


    with open(record_name, "a") as f:
        f.write(append_str)
        f.close()
    return 1

def get_stats(filename):
    
    print("Getting stats...\n")

    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.split(','))
    reads = []
    writes = []
    for line in data:
        reads.append(int(line[1]))
        writes.append(int(line[2].rstrip('\n')))
        #print(reads[-1] + "\t" + writes[-1])
        #print(writes[-1])

    #print(reads)
    #print(writes)
    ravg=str(np.average(reads))
    rstdev=str(np.std(reads))

    wavg=str(np.average(writes))
    wstdev=str(np.std(writes))

    rmin=np.min(reads)
    rmax=np.max(reads)

    wmin=np.min(writes)
    wmax=np.max(writes)


    print ("Average reads in flight / stdev: " + ravg + " / " + rstdev)
    print("Min / Max reads in flight: " + str(rmin) + " / " + str(rmax) + "\n")
    
    print ("Average writes in flight / stdev: " + wavg + " / " + wstdev)
    print("Min / Max writes in flight: " + str(wmin) + " / " + str(wmax))

    print("Sample size: " + str(len(writes)))


    #print ("Time elapsed: " + str(data[0]['timestamp'] - data[0]['timestamp']))

def handle_ctrlc(filename, signal, frame):
    get_stats(filename)
    exit(1)


def main():
    #device = sys.argv[1]
    #filename = sys.argv[2]
    parser = argparse.ArgumentParser()  # Create argument parser object
    parser.add_argument("-d", "--device", help="Block device you want to track inflights for")  # Add argument for name
    parser.add_argument("-f", "--filename", help="File name for CSV file that will store all the data")
    #parser.add_argument("-p", "--print", help="Print to stdout. Will introduce overhead")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()  # Parse arguments from command lin
    device = args.device  # Get name from parsed argument
    filename= args.filename
    printstdout=args.verbose

    signal.signal(signal.SIGINT, functools.partial(handle_ctrlc, filename))

    while True:
        collect_and_record(device, filename, printstdout)

if __name__ == "__main__":
    main()

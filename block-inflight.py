import sys
import datetime

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
    
    if verbose == 1:
        print("append string to csv: " + append_str)


    with open(record_name, "a") as f:
        f.write(append_str)
        f.close()
    return 1


def main():
    device = sys.argv[1]
    filename = sys.argv[2]

    while True:
        collect_and_record(device, filename, 1)

if __name__ == "__main__":
    main()

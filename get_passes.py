import os

def max_elev_for_chunk(chunk):
    m = 0
    for line in chunk:
        if int(line[4]) > m:
            m = int(line[4])

    return m

def get_passes(threshold):
    passes = []

    with open("tmp.txt") as f:
        chunk = []
        high_enough = False

        for idx,line in enumerate(f.readlines()):
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")
            line = line.replace("  ", " ")
            split_data = line.split(" ")
            
            if int(split_data[4]) <= 0:
                if high_enough:
                    start_time = chunk[0][0]
                    end_time = chunk[-1][0]
                    max_elev = max_elev_for_chunk(chunk)
                    passes.append({"start_time": start_time, "end_time": end_time, "max_elev": max_elev})
                chunk = []
                high_enough = False
                continue 
            else:
                if int(split_data[4]) >= threshold:
                    high_enough = True
                chunk.append(split_data)

    os.system("rm tmp.txt")
    return passes

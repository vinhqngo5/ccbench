import json
import os
import shutil
import subprocess
from variables import EVENTS, DEFAULT_DISTANCE_SETTINGS, DEFAULT_CORES, DEFAULT_CORE_TO_GET_RESULT

# monitored EVENTS
monitored_EVENTS = [
    "STORE_ON_MODIFIED",
    "STORE_ON_EXCLUSIVE",
    "STORE_ON_SHARED",
    "STORE_ON_OWNED",
    "STORE_ON_INVALID",
    # "LOAD_FROM_MODIFIED",
    # "LOAD_FROM_EXCLUSIVE",
    # "LOAD_FROM_SHARED",
    # "LOAD_FROM_OWNED",
    # "LOAD_FROM_INVALID",
    # "CAS",
    # "FAI",
    # "TAS",
    # "SWAP",
    # "CAS_ON_MODIFIED",
    # "FAI_ON_MODIFIED",
    # "TAS_ON_MODIFIED",
    # "SWAP_ON_MODIFIED",
    # "CAS_ON_SHARED",
    # "FAI_ON_SHARED",
    # "TAS_ON_SHARED",
    # "SWAP_ON_SHARED",
    # "CAS_CONCURRENT",
    # "FAI_ON_INVALID",
]

# monitored distances
monitored_distances = ["same_core", "same_ccx",
                       "same_ccd", "same_socket", "2_sockets"]

# output directory
output_dir = "output"
subdirs = monitored_distances

# remove the output directory if it exists
shutil.rmtree(output_dir, ignore_errors=True)

# Create output directories (if they don't exist)
for subdir in subdirs:
    os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)

# remove result.json if it exists
if os.path.exists(os.path.join(output_dir,"result.json")):
    os.remove(os.path.join(output_dir,"result.json"))
    
# result dictionary (will be printed in result.json)
result = {}

# Loop through each event
for i, event in enumerate(monitored_EVENTS):
    for distance in monitored_distances:
        # if distance_setting exists, set distance_setting   else use default value
        distance_setting = EVENTS[event]["distance_setting"] if "distance_setting" in EVENTS[event] else DEFAULT_DISTANCE_SETTINGS[distance]
        cores = EVENTS[event]["cores"] if "cores" in EVENTS[event] else DEFAULT_CORES
        which_core_to_get_result = EVENTS[event]["which_core_to_get_result"] if "which_core_to_get_result" in EVENTS[event] else DEFAULT_CORE_TO_GET_RESULT

        # Construct ccbench command arguments
        command = [
            "./ccbench",
            "--cores", str(cores),
            *distance_setting.split(),
            "-t", str(EVENTS[event]["event_id"]),
            "--mem-size", "2122317824",
            # "--flush"
        ]

        output_filename = os.path.join(output_dir, distance, f"{event}_{'_'.join([i[1:] for i in distance_setting.split()])}")

        # Run ccbench with both capture and print
        print ("run command: ", command)
        is_needed_core = False
        with open(output_filename, "w") as outfile:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in process.stdout:
                if "*** Core" in line.decode():
                  core_number = int(line.split()[3])
                  if core_number == which_core_to_get_result:
                    is_needed_core = True
                if is_needed_core and "avg" in line.decode():
                  avg = float(line.split()[3])
                  result[event] = result.get(event, {})
                  result[event][distance] = avg
                  print(line.decode(), end="")
                  is_needed_core = False
                # print(line.decode(), end="")  # Print to screen
                outfile.write(line.decode())  # Write to file
            process.wait()

        # output to json
        with open(os.path.join(output_dir, "result.json"), "w") as outfile:
            json.dump(result, outfile, indent=4)
        # Print status message
        print(f"Finished running ccbench with event {event} for distance {distance} (number: {i})")

print("All EVENTS processed.")

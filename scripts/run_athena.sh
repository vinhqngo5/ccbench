#!/bin/bash

# Array of event names
events=(
"STORE_ON_MODIFIED"
"STORE_ON_MODIFIED_NO_SYNC"
"STORE_ON_EXCLUSIVE"
"STORE_ON_SHARED"
"STORE_ON_OWNED_MINE"
"STORE_ON_OWNED"
"STORE_ON_INVALID"
"LOAD_FROM_MODIFIED"
"LOAD_FROM_EXCLUSIVE"
"LOAD_FROM_SHARED"
"LOAD_FROM_OWNED"
"LOAD_FROM_INVALID"
"CAS"
"FAI"
"TAS"
"SWAP"
"CAS_ON_MODIFIED"
"FAI_ON_MODIFIED"
"TAS_ON_MODIFIED"
"SWAP_ON_MODIFIED"
"CAS_ON_SHARED"
"FAI_ON_SHARED"
"TAS_ON_SHARED"
"SWAP_ON_SHARED"
"CAS_CONCURRENT"
"FAI_ON_INVALID"
"LOAD_FROM_L1"
"LOAD_FROM_MEM_SIZE"
"LFENCE"
"SFENCE"
"MFENCE"
"PROFILER"
"PAUSE"
"NOP"
)

# remove output directory if it exists && make output directory if it doesn't exist
rm -rf output && mkdir output
mkdir output/same_core
mkdir output/same_ccx
mkdir output/same_ccd
mkdir output/same_socket
mkdir output/2_sockets

# Loop through each event and its corresponding index
for ((i=0; i<${#events[@]}; i++)); do
  event="${events[$i]}"

  # same core
  ./ccbench -x1 -y257 -t $((i)) --mem-size 2122317824 --flush &> "output/same_core/${event}_x1_y257.txt"; 

  # same ccx
  ./ccbench -x1 -y263 -t $((i)) --mem-size 2122317824 --flush &> "output/same_ccx/${event}_x1_y263.txt"; 

  # same ccd
  ./ccbench -x1 -y271 -t $((i)) --mem-size 2122317824 --flush &> "output/same_ccd/${event}_x1_y271.txt";

  # same socket
  ./ccbench -x1 -y383 -t $((i)) --mem-size 2122317824 --flush &> "output/same_socket/${event}_x1_y383.txt";

  # 2 sockets
  ./ccbench -x1 -y499 -t $((i)) --mem-size 2122317824 --flush &> "output/2_sockets/${event}_x1_y499.txt";
  echo "Finished running ccbench with event: $event (number: $((i)))"
done

echo "All events processed."
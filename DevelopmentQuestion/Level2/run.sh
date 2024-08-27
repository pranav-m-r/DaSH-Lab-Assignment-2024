#!/bin/bash

# Start the server and wait for some time
python server.py &
sleep 2

# Define the number of clients
num_clients=3
# Get the number of lines in input.txt
total_lines=$(wc -l < input.txt)
# Calculate the number of lines per client
lines_per_client=$((total_lines / num_clients))
# Initialize start_line as zero
start_line=0

# Start multiple clients and allot their respective sections of the input
for i in $(seq 1 $num_clients);
do
    end_line=$((start_line + lines_per_client + 1))
    START_LINE=$start_line END_LINE=$end_line python client.py &
    start_line=$end_line
done

# Wait for all processes to finish
wait
#!/bin/bash

for i in $(seq -w 1 20); do
    echo "Running test case $i"
    python3 insertion_benchmark.py < "testcases/input$i.txt" | diff "testcases/output$i.txt" -
    if [ $? -eq 0 ]; then
        echo "Test case $i passed"
    else
        echo "Test case $i failed"
    fi
    echo
done

for i in $(seq -w 1 20); do
    echo "Running test case $i"
    start_time=$(date +%s.%N)
    python3 insertion_benchmark.py < "testcases/input$i.txt" > /dev/null
    end_time=$(date +%s.%N)  # Capture end time
    elapsed_time=$(echo "$end_time - $start_time" | bc)
    echo "Test case $i completed in $elapsed_time seconds"
    echo
done

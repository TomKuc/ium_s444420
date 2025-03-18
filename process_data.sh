#!/bin/bash

CUTOFF=$1

if [ -z "$CUTOFF" ]; then
  CUTOFF=3
fi

echo "Using CUTOFF value: $CUTOFF"

echo "id,name,age,salary" > data.csv
echo "1,Alice,30,5000" >> data.csv
echo "2,Bob,25,4500" >> data.csv
echo "3,Charlie,35,6000" >> data.csv
echo "4,David,40,7000" >> data.csv
echo "5,Emma,28,5200" >> data.csv

shuf data.csv | head -n "$CUTOFF" > processed_data.csv

cut -d ',' -f1,2,4 processed_data.csv > final_data.csv

echo "Data processing complete. Output saved in final_data.csv."

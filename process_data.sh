#!/bin/bash

INPUT_FILE=$1

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File $INPUT_FILE not found!" > stats_result.txt
    exit 1
fi

LINES=$(tail -n +2 "$INPUT_FILE" | wc -l)

echo "Liczba rekordów w zbiorze: $LINES" > stats_result.txt
echo "Statystyki zapisane w stats_result.txt"
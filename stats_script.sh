#!/bin/bash

INPUT_FILE="final_data.csv"

LINES=$(tail -n +2 "$INPUT_FILE" | wc -l)

echo "Liczba rekordów w zbiorze: $LINES" > stats_result.txt
echo "Statystyki zapisane w stats_result.txt"

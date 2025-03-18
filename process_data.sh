#!/bin/bash

# Pobranie zbioru danych (przykładowy plik CSV)
echo "id,name,age,salary" > data.csv
echo "1,Alice,30,5000" >> data.csv
echo "2,Bob,25,4500" >> data.csv
echo "3,Charlie,35,6000" >> data.csv
echo "4,David,40,7000" >> data.csv

# Przetwarzanie: losowe sortowanie i wybór 2 pierwszych wierszy
shuf data.csv | head -n 3 > processed_data.csv

# Usunięcie trzeciej kolumny (np. wieku)
cut -d ',' -f1,2,4 processed_data.csv > final_data.csv

# Informacja o przetworzeniu
echo "Data processing complete. Output saved in final_data.csv."

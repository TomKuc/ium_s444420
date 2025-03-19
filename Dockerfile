# Używamy Ubuntu jako bazowego obrazu
FROM ubuntu:latest

# Instalujemy niezbędne pakiety
RUN apt update && apt install -y coreutils

# Tworzymy katalog roboczy /app
WORKDIR /app

# Kopiujemy skrypt do kontenera
COPY ./process_data.sh ./

# Nadajemy skryptowi prawa do wykonywania
RUN chmod +x process_data.sh

# Ustawiamy domyślną komendę uruchamianą w kontenerze
CMD ["./process_data.sh"]

FROM ubuntu:latest

RUN apt update && apt install -y coreutils

WORKDIR /app

COPY ./process_data.sh ./

RUN chmod +x process_data.sh

CMD ["./process_data.sh"]

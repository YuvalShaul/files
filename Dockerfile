FROM  nginx:latest
WORKDIR /app
RUN apt update && apt install -y python3
COPY my_clock.py ./
COPY run_all ./
RUN chmod +x ./run_all
CMD ["./run_all"]

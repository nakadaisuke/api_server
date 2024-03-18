FROM ubuntu
COPY ./main.py /home
COPY ./user_data.csv /home

RUN apt-get update \
 && apt-get install -y \
  python3 \
  python3-pip\
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
  fastapi \
  uvicorn

CMD ["python3", "/home/main.py"]

FROM python:3.7

RUN mkdir -p /client/

WORKDIR /client/

COPY . /client/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install nano

ENV DEBUG=1

ENTRYPOINT ["python", "main.py"]

EXPOSE 5001
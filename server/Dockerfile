FROM python:3.7

RUN mkdir -p /server/

WORKDIR /server/

COPY . /server/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install nano

ENV DEBUG=0
ENV COUNT_USERS=100
ENV GENDER=female


ENTRYPOINT ["python", "fill_db.py"]
ENTRYPOINT ["python", "main.py"]

EXPOSE 5000 
FROM python:3.7

RUN mkdir -p /server/

WORKDIR /server/

COPY . /server/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "ETL_users.py"]
ENTRYPOINT ["python", "main.py"]

EXPOSE 5000 
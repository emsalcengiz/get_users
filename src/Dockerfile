FROM python:3.7.10-stretch

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN apt-get update


RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["endpoint.py"]
ENTRYPOINT ["python3"]







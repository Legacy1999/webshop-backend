FROM python:3.10

WORKDIR /app

COPY backend/ /app

RUN pip install -r requirements.txt

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]

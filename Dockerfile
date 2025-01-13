FROM python:3.7

RUN pip install fastapi uvicorn

WORKDIR /app

COPY ./app.py .

CMD ["python", "/app/app.py"]


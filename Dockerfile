
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade "pip>=26.2.0"

RUN pip install --no-cache-dir --timeout=120 --retries=5 -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
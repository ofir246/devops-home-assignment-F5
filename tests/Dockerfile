FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY test_nginx.py /app/test_nginx.py

CMD ["python", "-u", "/app/test_nginx.py"]
FROM python:3.10

WORKDIR /app
ENV PYTHONBUFFERED=1

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . ./
EXPOSE 8000

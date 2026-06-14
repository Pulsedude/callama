FROM python:3.11.15-slim-trixie

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000" ]


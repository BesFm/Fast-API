FROM python:3.9-slim

WORKDIR /code_c

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code_c/requirements.txt

COPY service_c service_c

CMD ["uvicorn", "service_c.main:app", "--host", "0.0.0.0", "--port", "8003"]


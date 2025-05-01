FROM python:3.9-slim

WORKDIR /code_b

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code_b/requirements.txt

COPY service_b service_b

# CMD ["uvicorn", "service_b.main:app", "--host", "0.0.0.0", "--port", "8002"]
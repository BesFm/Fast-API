FROM python:3.9-slim

WORKDIR /code_a

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code_a/requirements.txt

COPY service_a service_a

CMD ["uvicorn", "service_a.main:app", "--host", "0.0.0.0", "--port", "8001"]
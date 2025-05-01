from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/test')
def test() -> str:
    return 'Response from SERVICE_C'


@app.get('/test_b')
def test_b() -> str:
    response = requests.get('http://service_b:8000/test')
    return response.text

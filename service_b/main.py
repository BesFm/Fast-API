from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/test')
def test() -> str:
    return 'Response from SERVICE_B'


@app.get('/test_c')
def test_c() -> str:
    response = requests.get('http://service_c:8000/test')
    return response.text

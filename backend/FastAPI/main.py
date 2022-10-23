from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from genprime import genPrime, genPrimeBtwn
from fastapi.responses import StreamingResponse
import io
import pandas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.environ('api_key')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/genprime")
def generate_prime(n: int, apikey: str):
    if apikey == api_key:
        return {"prime": genPrime(n)}
    return {"prime": -1}

@app.get("/gentestprime")
def generate_test_prime():
    """
    Generate a random 5 digit prime
    """
    return {"prime": genPrime(5)}

@app.get("/genprimebtwn")
def generate_prime_between(a: int, b: int, apikey: str):
    if apikey == api_key:
        return {"prime": genPrimeBtwn(a, b)}
    return {"prime": -1}
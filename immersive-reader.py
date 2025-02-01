
# Immersive Reader Text Conversion with Azure AI Immersive Reader API
# Glenn Yaniero 

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Replace these with your Azure Immersive Reader endpoint and key
endpoint = "YOUR_IMMERSIVE_READER_ENDPOINT"
key = "YOUR_IMMERSIVE_READER_KEY"

# Allowing CORS for local development (adjust as needed)
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5500",  # Adjust this for your front-end port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_immersive_reader_token():
    token_url = f"{endpoint}/issueToken"
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(token_url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.post("/immersive-reader")
def immersive_reader(text: str):
    token = get_immersive_reader_token()
    immersive_reader_url = f"{endpoint}/read"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": text,
        "lang": "en",
        "token": token,
        "subdomain": endpoint.split("//")[1].split(".")[0]
    }
    
    # post to Azure immersive reader api
    response = requests.post(immersive_reader_url, headers=headers, json=payload)
    return response.json()

# Run the application with: uvicorn filename:app --reload

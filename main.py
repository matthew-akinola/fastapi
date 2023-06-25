import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests
from dotenv import load_dotenv
import os
from fastapi import FastAPI

app = FastAPI()
  

@app.on_event("startup")
async def startup_event():
    load_dotenv()  


SERVICE_2_URL = os.getenv('SERVICE_2_URL')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')

# Load credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Check if the credentials are expired, and refresh if necessary
if credentials.expired:
    request = Request()
    credentials.refresh(request)

# Set the credentials as the default for the Google API client library
google.auth.default(credentials)




@app.get('/api/blogs/')
def get_blogs():
    # Obtain the access token
    access_token = credentials.token

    # Make a request to Service 2 using the access token
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(SERVICE_2_URL, headers=headers)
    response.raise_for_status()
    blogs = response.json()
    return blogs



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)

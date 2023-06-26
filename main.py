import os
from fastapi import FastAPI
import urllib
import google.auth.transport.requests
import google.oauth2.id_token
import uvicorn

app = FastAPI()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tolu-svca.json'
endpoint = 'https://django-service-3gjvcximaa-uc.a.run.app/blogposts'
audience = 'https://django-service-3gjvcximaa-uc.a.run.app'

@app.get('/api/blogs/')
def get_blogs():

    req = urllib.request.Request(endpoint)
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    return response.read()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)

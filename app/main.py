import imp
from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from app.config import settings
import requests

app=FastAPI()

@app.get('/')
async def index():
    return {'message': f'query_app_up ver: {settings.version} env:{settings.environment}'} 

@app.get('/participants')
async def index():
    query = {'participants': settings.participants}
    response = requests.get(f'{settings.baseurl}activity', params=query)
    data=response.json()
    if response.status_code == 200:
        return {'message': f'An activity suitable for {data["participants"]} participants would be: {data["activity"]}, which is of type: {data["type"]}'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="unable to process you request. Contact you admininstrator")

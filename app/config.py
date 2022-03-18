from ensurepip import version
from pydantic import BaseSettings

class Settings(BaseSettings):
    participants: str 
    baseurl: str 
    environment: str
    version:str 

settings = Settings()
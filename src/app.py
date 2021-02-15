from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Subscribe(BaseModel):
	name:str
	email:str 
	

@app.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request":Request}) 


@app.post("/subscribe", response_model(subscribe, response_model_exculde_unset))
async def subscribe(subscribe:Subscribe):
	return subscribe


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
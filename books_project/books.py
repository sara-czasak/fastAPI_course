from fastapi import FastAPI


app = FastAPI()
# To start app cd into dir then: uvicorn app_name:app --reload


@app.get('/api-endpoint')
async def first_api():
    return {'message': 'Hello, Sara!'}
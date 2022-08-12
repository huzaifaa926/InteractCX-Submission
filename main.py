from typing import Union
from urllib import response
from fastapi import FastAPI, Request
import requests

app = FastAPI()


def get_date():
    _response = requests.get("https://interview-test-webhook-response-dot-organization-project-311520.uc.r.appspot.com/")
    json_obj = _response.json()
    return json_obj["date"]

# @app.get("/")
@app.post("/")
async def read_root(request : Request):
    payload = await request.json()
    print(payload["queryResult"]["queryText"])
    print(payload["queryResult"]["fulfillmentText"])
    try:
        orderID = payload["queryResult"]["parameters"]["orderID"]
        return {
        "fulfillmentText": f"Your order {int(orderID)} has been dispatched on {get_date()}.",
        "source": "webhookdata"
    }
    except:
        return {"payload": payload}
    

@app.get("/orderDetails")
def order_details():
    return {"dispatched_date" : get_date()}

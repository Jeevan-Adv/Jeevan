from fastapi import FastAPI, Request
from pywa import WhatsApp, types, filters
import uvicorn

app = FastAPI()

wa = WhatsApp(
    phone_id='715412771651848',
    token='EAAQL8ZB2cPX0BO8i2jr8qm1Np5rEaf0K9k4CZBdXsnZCC0ZAWyQgDiKb8JSrMlGYtcXS4eOSsBvLt35i7qRS9RkmS4WheYWtbkgChHB3VTs5ZCq1BgLPY3ZAvICiMKQrHEpwDYaAgXO5ZBxUrfYD9JC1N96aRhgHr7i7wKHx0Y89gW6l9fKmX20KezTWdT9iYhVHv6ueZAloJBrYTLoPqIHhcyfgeKkNHO0sPm0ZD',
    verify_token='xyzxyz', 
    server=app, # Pass FastAPI app here
)

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    wa.handle_request(data)
    return {"status": "ok"}

@wa.on_message(filters.command("start"))
def start(client: WhatsApp, msg: types.Message):
    msg.reply("Hello! How old are you?")
    age: types.Message = client.listen(
        to=msg.sender,
        filters=filters.message & filters.text
    )
    msg.reply(f"Your age is {age.text}.")

if __name__ == "__main__":
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True)
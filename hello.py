from fastapi import FastAPI, Request
from pywa import WhatsApp, types, filters
import uvicorn

app = FastAPI()

wa = WhatsApp(
    phone_id='715412771651848',
    token='EAAQL8ZB2cPX0BO7w14HeDlcKfIpdOy4GaZCrkjkdZCf21xnADcW7eh1ZAAcfvFRCRWqCYmgvX8gsZAKDIaVR7gQZCZAGapU9hqeZCmohgZCy690btTJoZCK4mhZAkMwQZCWqrV8k58fclq5xvn1KYihRp7WmggEKGX8ubAJUiZAThe7PE0XTyHb2lyy9ZCRYwHKnMLmBVHgTiRVf8l0wdlU1sfTrhUWaXTrBw5jQ7MqU0ZD',
    verify_token='12345', 
    server=app, # Pass FastAPI app here
)

@wa.on_message
def echo(_: WhatsApp, msg: types.Message):
    try:
        msg.copy(to=msg.sender, reply_to_message_id=msg.message_id_to_reply)
    except ValueError:
        msg.reply_text("I can't echo this message")

@app.get("/")
def read_root():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True)
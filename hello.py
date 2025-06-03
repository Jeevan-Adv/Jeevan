from fastapi import FastAPI, Request
from pywa import WhatsApp, types, filters
import uvicorn
from pywa.types import SectionList, Section, SectionRow,Button

app = FastAPI()

wa = WhatsApp(
    phone_id='715412771651848',
    token='EAAQL8ZB2cPX0BO26Gj2ZB6xIfnTV7ZCCyCZBDMrMH0KJSGtseEyatlSqWXgH9t5T7zVELbrEAnKnDhi0HOmUhER2jfOJ7K2EyVyEUGwZAXMyi2kZCspueTVpLff2QKPPjnAXLma7zsXPMcSUxTiiG152gvDBUXGiDPpnkaHUe1aTMfDYImvO7jroZAUlKz9ZB3NzlwRKBcMSnWeeHoEIsn8oE59Ml9wk0PZBsgNra',
    verify_token='12345', 
    server=app, # Pass FastAPI app here
    validate_updates=False,
)

user_data = {}

@wa.on_message
def start(client: WhatsApp, msg: types.Message):
    msg.reply("Hello! What is your name?")
    name: types.Message = client.listen(
        to=msg.sender,
        filters=filters.message & filters.text
    )
    user_data[msg.sender] = {'name': name.text}

    msg.reply("Enter your Age?")
    age: types.Message = client.listen(
        to=msg.sender,
        filters=filters.message & filters.text
    )
    user_data[msg.sender]['age'] = age.text

    msg.reply("Enter your Profession?")
    profession: types.Message = client.listen(
        to=msg.sender,
        filters=filters.message & filters.text
    )
    user_data[msg.sender]['profession'] = profession.text

    r = msg.reply(
        text="Select your Gender",
        buttons=[
            Button(title="Male", callback_data="male"),
            Button(title="Female", callback_data="female"),
            Button(title="Other", callback_data="other"),
        ],
    )
    gender = r.wait_for_click()
    user_data[msg.sender]['gender'] = gender.title
    data = user_data[msg.sender]
    msg.reply(
        f"Name: {data.get('name')}\nAge: {data.get('age')}\nProfession: {data.get('profession')}\nGender: {data.get('gender')}"
    )

@app.get("/")
def read_root():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True)

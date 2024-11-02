import os
import requests
from twilio.rest import Client

# Use environment variables for sensitive information
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
api_key = os.getenv('OPENWEATHER_API_KEY')

base_url = "https://api.openweathermap.org/data/2.5/forecast"
api_params = {
    "lat": 23.8041,
    "lon": 90.4152,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(base_url, params=api_params)
response.raise_for_status()
weather_data = response.json()

is_raining = False
for i in weather_data["list"]:
    weather_id = i["weather"][0]["id"]
    if weather_id < 700:
        is_raining = True

client = Client(account_sid, auth_token)
if is_raining:
    message = client.messages.create(
        body='Have an umbrella with you',
        from_='Twilio Number',
        to='Recipient Number'
    )
else:
    message = client.messages.create(
        body='No need for an umbrella',
        from_='Twilio Number',
        to='Recipient Number'
    )
print(message.status)


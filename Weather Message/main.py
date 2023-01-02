import requests
from twilio.rest import Client

api_key = "620c61d572e081237cff298e74e269b9"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC58aac547b29f2c9265be5a692b3e6953"
auth_token = "12f9ca7a0c11d94054467b8c3eaf9496"

weather_params = {
    "lat": 41.385063,
    "lon": 2.173404,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status
weather_data = response.json()
#print(weather_data["hourly"][0]["weather"][0])
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_="+16307499491",
        to="+34632486338",
    )




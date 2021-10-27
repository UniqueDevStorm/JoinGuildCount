import requests
from flask import Flask, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(
        "https://discord.com/api/oauth2/authorize?client_id=774632098966667304&redirect_uri=http://test.devstorm.kr"
        ":3000/api/callback&response_type=code&scope=guilds "
    )


@app.route("/api/callback")
def callback():
    # get code from url
    code = request.args.get("code")
    # get token from code
    data = {
        "client_id": "774632098966667304",
        "client_secret": "B_bTaiUTAuroK0M-A4PXKsSRt6hLYFQN",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://test.devstorm.kr:3000/api/callback",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(
        "https://discord.com/api/oauth2/token", data=data, headers=headers
    ).json()
    guilds = requests.get(
        "https://discord.com/api/users/@me/guilds",
        headers={"Authorization": "Bearer " + r["access_token"]},
    ).json()
    print(guilds)
    return f'님 길드 수 {len(guilds)} 개임'


app.run(host="0.0.0.0", port=3000, debug=True)

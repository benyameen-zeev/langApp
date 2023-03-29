from flask_dance.contrib.google import make_google_blueprint

google_blueprint = make_google_blueprint(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    scope=["profile", "email"],
    offline=True,
    login_url="/google/login",
)

import os

class Config(object):
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	DEBUG=True
	SECRET_KEY = '975c3bb12c5b33353fe3436c0681cc568f21bbd8c86a7884b6b69497b564ce31'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENV='venv'
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/models/ted.db"
	URL = 'https://api.skypicker.com/flights?'
	CHECK = 'https://booking-api.skypicker.com/api/v0.1/check_flights?v=2&booking_token='
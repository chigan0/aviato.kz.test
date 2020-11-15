from threading import Thread
from app import app,api
from resources.Stp import Stp
from resources.util import update_flight
from models.models import *
from settings import Config

api.add_resource(Stp,'/api/flights')

if __name__ == '__main__':
	Thread(target=update_flight,daemon=True,args=(FlightData,CityName,db,Config.URL)).start()
	app.run()
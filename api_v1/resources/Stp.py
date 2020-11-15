import threading
import time
from datetime import datetime,timedelta
import requests
from flask import request,jsonify
from flask_restful import Resource
from app import app
from settings import Config
from models.models import FlightData
from settings import Config

class Stp(Resource):
	def get(self,):
		
		resul = {}

		def dw(ser,resul):
			a = requests.get(ser).json()
			if a['flights_checked'] == True:
				resul[(int(a['total']*430.25))] = {
					'flights_checked':a['flights_checked'],
					'adults_price':int(a['adults_price']*430.25),
					'infants_price':a['infants_price']
				}
				return True
				

		pd = datetime.now()-timedelta(days=1)
		yesterday = time.strftime('%d/%m/%Y',time.gmtime(time.time()-86400))
		date_to = '.'.join(request.args['dateTo'].split('/'))
		date_from = '.'.join(request.args['dateFrom'].split('/'))

		if request.args['dateFrom'] != yesterday:

			url = Config.CHECK

			a ={i.adults_price:[i.booking_token] for i in FlightData.query.filter_by(
				date_to=date_to,
				fly_from=request.args['fly_from'],
				fly_to=request.args['fly_to'],
			).all()}

			if len(a)>0:
				for g in a:
					ser = f"{url}{a[g][0]}&bnum=1&pnum={request.args['adults']}&currency=USD"
					threading.Thread(target=dw,args=(ser,resul,)).start()

				time.sleep(2)
				return jsonify(resul)

		return jsonify({'status':'Date time not valid'})

	def post(self,):
		print()
	def put(self,):
		pass
	def delete(self,):
		pass
import requests
import time
from threading import Thread
from datetime  import datetime,timedelta
from models.models import *
from functools import lru_cache


db.create_all()

url = 'https://api.skypicker.com/flights?'
check = 'https://booking-api.skypicker.com/api/v0.1/check_flights?v=2&booking_token='
city = ('ALA','TSE','MOW','LED','CIT')
timesum = 0

@lru_cache(maxsize=None)
def stt(url,conf,ff,ft,datat):
	tt = datetime.now()
	res = requests.get(f"{url}{conf}").json()
	datafrom = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
	for i in res['data']:#i['booking_token']
		if i['flyFrom'] == ff and i['flyTo'] == ft:
			try:
				a = FlightData(
					date_to='.'.join(datat.split('/')),
					fly_from=ff,
					fly_to=ft,
					booking_token=i['booking_token'],
					adults_price=i['price'],
				)
				db.session.add(a)
				db.session.commit()
			except:
				db.session.rollback() 
	
	print(datetime.now()-tt)

for dda in range(0,32):
	stt.cache_clear()
	pd = datetime.now()+timedelta(days=dda)
	for i in CityName.query.all():
		for g in CityName.query.all():
			if g.name != i.name:
				#&children=1,adults=1
				datab = f"{pd.day}/{pd.month}/{pd.year}"
				print(datab)
				Thread(target=stt,daemon=True,args=(url,
													f"flyFrom={i.name}&to={g.name}&dateTo={datab}&partner=picky&v=3&adults=1",
													i.name,g.name,datab)).start()
	time.sleep(7)
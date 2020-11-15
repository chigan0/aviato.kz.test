import os
import requests
import time
from threading import Thread
from datetime  import datetime,timedelta

def stt(url,conf,ff,ft,datat,FlightData,db):
	tt = datetime.now()

	print(ff,ft)

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
	return True

def update_flight(FlightData,CityName,db,url):
	while True:
		time.sleep(1)
		datekz = datetime.utcnow() + timedelta(hours=+6)
		
		if datekz.hour == 0 and datekz.minute == 0 and datekz.second == 0:
			dl = datetime.now()-timedelta(days=1)
			ddl = f"{dl.day}.{dl.month}.{dl.year}"
			a = FlightData.query.filter_by(date_to=ddl).all()
			#and datekz.second == 0
			print(ddl)
			if len(a)>0:
				for i in a:
					db.session.delete(i)
					db.session.commit()
				print(f'Все записи за {ddl} были успешно удаленый ')

			dn = datetime.now()+timedelta(days=32)

			for i in CityName.query.all():
				ddn = f"{dn.day}/{dn.month}/{dn.year}"
				for g in CityName.query.all():
					if i.name != g.name:
						Thread(target=stt,
								args=(url,f"flyFrom={i.name}&to={g.name}&dateTo={ddn}&partner=picky&v=3&adults=1",
										i.name,g.name,ddn,FlightData,db
									)
							).start()
						
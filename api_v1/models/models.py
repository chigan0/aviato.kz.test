from app import db

class CityName(db.Model):
	__tablename__='city_name'
	id = db.Column('id',db.Integer,primary_key=True)
	name = db.Column('name',db.String(4),unique=True)
	pri = db.relationship('FlightData',backref='name_city',lazy='dynamic')

	def __repr__(self):
		return f"City Name {self.name}"

class FlightData(db.Model):
	__tablename__='flight_data'
	id=db.Column('id',db.Integer,primary_key=True)
	date_to=db.Column('date_to',db.String(12),nullable=False)
	fly_from=db.Column(db.String, db.ForeignKey('city_name.name'))
	fly_to=db.Column('fly_to',db.String(4),nullable=False)
	booking_token=db.Column('token',db.String,nullable=False,unique=True)
	adults_price=db.Column('adults',db.Integer)

	def __repr__(self):
		return f"fly_from {self.fly_from} fly_to {self.fly_to} date_from {self.date_from}"

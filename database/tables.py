from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, CHAR, BINARY, TIMESTAMP, DateTime, Float, JSON, DECIMAL
from sqlalchemy.orm import relationship
from database.db_model import DBModel
import datetime


class User(DBModel):

    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(45), nullable=False, unique=True)
    email = Column(VARCHAR(45), nullable=False, unique=True)
    password = Column(BINARY(60), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    lamp_devices = relationship('LampDevice', backref='user', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            created_date=self.created_date,

            lamp_devices=self.lamp_devices
        )


class LampDevice(DBModel):

    __tablename__ = "lamp_device"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(VARCHAR(128), nullable=False)
    on_url = Column(VARCHAR(128), nullable=False)
    off_url = Column(VARCHAR(128), nullable=False)
    last_status = Column(VARCHAR(1), nullable=False, default='0')

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            on_url=self.on_url,
            off_url=self.off_url,
            last_status=self.last_status
        )


class WeatherCache(DBModel):

    __tablename__ = "weather_cache"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    lon = Column(CHAR(5))
    lat = Column(CHAR(5))
    data = Column(JSON)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow())

    def to_dict(self):
        return dict(
            id=self.id,
            lon=self.lon,
            lat=self.lat,
            data=self.data,
            timestamp=self.timestamp
        )

import datetime

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, CHAR, BINARY, DateTime, Float, JSON
from sqlalchemy.orm import relationship

from database.db_model import DBModel


class User(DBModel):
    __tablename__ = "user"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(45), nullable=False, unique=True)
    email = Column(VARCHAR(45), nullable=False, unique=True)
    password = Column(BINARY(60), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    lamp_devices = relationship('LampDevice', backref='user', lazy=True)
    colored_lamp_devices = relationship('ColoredLampDevice', backref='user', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            created_date=self.created_date,

            lamp_devices=self.lamp_devices,
            colored_lamp_devices=self.colored_lamp_devices,
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


class ColoredLampDevice(DBModel):
    __tablename__ = "colored_lamp_device"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(VARCHAR(128), nullable=False)
    update_url = Column(VARCHAR(128), nullable=False)
    last_red = Column(Float, nullable=False, default=0)
    last_green = Column(Float, nullable=False, default=0)
    last_blue = Column(Float, nullable=False, default=0)

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            update_url=self.update_url,
            last_red=self.last_red,
            last_green=self.last_green,
            last_blue=self.last_blue
        )


class WeatherCard(DBModel):
    __tablename__ = "weather_card"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(VARCHAR(32))
    lat = Column(Float)
    lon = Column(Float)
    locationname = Column(VARCHAR(32))

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            lat=self.lat,
            lon=self.lon,
            locationname=self.locationname
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


class DummyDevice(DBModel):
    __tablename__ = "Dummy_Device"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    dummy_type = Column(VARCHAR(32), nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(VARCHAR(128), nullable=False)
    value = Column(Integer, nullable=True)

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            dummy_type=self.dummy_type,
            name=self.name,
            description=self.description,
            value=self.value
        )

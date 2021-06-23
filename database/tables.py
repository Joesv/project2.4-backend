from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, CHAR, BINARY, TIMESTAMP, DateTime, Float, JSON
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

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            on_url=self.on_url,
            off_url=self.off_url
        )


class WeatherCache(DBModel):

    __tablename__ = "weather_cache"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    lon = Column(Float)
    lat = Column(Float)
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

'''        
class Game(DBModel):

    __tablename__ = "game"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    game_name = Column(VARCHAR(45), nullable=False, unique=True)
    topscores = relationship("TopScore")

    def to_dict(self):
        return dict(
            id=self.id,
            game_name=self.game_name,
            topscores=[dict(user=ts.user_id,score=ts.score) for ts in self.topscores]
        )
        
class TopScore(DBModel):

    __tablename__ = "topscore"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    game_id = Column(ForeignKey(Game.id), nullable=False)
    user_id = Column(ForeignKey(User.id), nullable=False)
    score = Column(Integer, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            game_id=self.game_id,
            user_id=self.user_id,
            score = self.score
        )
        
class UserGame(DBModel):
    
    __tablename__ = "user_game"
    
    game_id = Column(ForeignKey(Game.id), primary_key=True, nullable=False)
    user_id = Column(ForeignKey(User.id), primary_key=True, nullable=False)
    
    def to_dict(self):
        return dict(
            game_id=self.game_id,
            user_id=self.user_id,
        )
'''
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, CHAR, BINARY, TIMESTAMP, DateTime
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

    devices = relationship('Device', backref='user', lazy=True)

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            created_date=self.created_date,
            devices=self.devices
        )


class Device(DBModel):

    __tablename__ = "device"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(VARCHAR(32), nullable=False)
    description = Column(VARCHAR(128), nullable=False)
    control_type = Column(VARCHAR(32), nullable=False)
    control_url = Column(VARCHAR(64), nullable=False)
    fetch_url = Column(VARCHAR(64), nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            control_type=self.control_type,
            control_url=self.control_url,
            fetch_url=self.fetch_url
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
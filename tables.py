from sqlalchemy import Boolean, Column, Integer, String

from db import Model

class Films(Model):

    __tablename__ = 'films'

    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True) #индексируемость: строки 1 и 2 имеют значение А, в 3 строке = В, но А = [1, 2] а В = 3, индекс А хранит какие строки использует его, как и В
    title = Column(String)
    is_premiere = Column(Boolean)


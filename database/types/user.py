from sqlalchemy import Column, String, DateTime, func, BigInteger
from .BASE import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    full_name = Column(String(64), nullable=False)
    username = Column(String(64))
    locale = Column(String(8), default='en_US')
    last_active = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<User(id={}, full_name='{}', username='@{}')>"\
            .format(self.id, self.full_name, self.username)

from sqlalchemy import Column, String, Boolean, DateTime, func, BigInteger
from .BASE import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(64), nullable=False)
    username = Column(String(64))
    is_banned = Column(Boolean, default=False)
    locale = Column(String(8), default='en_US')
    last_active = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<User(id={}, first_name='{}', username='@{}', is_banned={})>"\
            .format(self.id, self.first_name, self.username, self.is_banned)

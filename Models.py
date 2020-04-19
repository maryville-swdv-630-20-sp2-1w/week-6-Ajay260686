from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

# The base class which our objects will be defined on.
Base = declarative_base()


# The CartInfo Table
class CartInfo(Base):
    __tablename__ = 'cart_info'

    # Every SQLAlchemy table should have a primary key named 'id'
    id = Column(Integer, Sequence('cart_info_seq', metadata=Base.metadata), primary_key=True)
    customerFirstName = Column(String)
    customerLastName = Column(String)
    productName = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    creditCardNumber = Column(String, nullable=False)

    # Lets us print out a CartInfo object conveniently.
    def __repr__(self):
        return "<Cart-Info(" \
               "customerFirstName='%s', " \
               "customerLastName='%s'," \
               "productName='%s', " \
               "price='%s', " \
               "quantity='%s', " \
               "creditCardNumber='%s')>" % (
                self.customerFirstName,
                self.customerLastName,
                self.productName,
                self.price,
                self.quantity,
                self.creditCardNumber)
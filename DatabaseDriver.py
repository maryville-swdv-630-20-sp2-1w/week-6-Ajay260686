from Models import *
from sqlalchemy.orm import sessionmaker

'''Database Driver class to Save the CartInfo Object in Database'''
class DatabaseDriver:

    # Method to Initialize the Database
    def databaseSetup(self,db_url):
        # Recreating database for every run
        db = create_engine(db_url, echo=False)
        Base.metadata.drop_all(bind=db)
        Base.metadata.create_all(bind=db)
        return db

    # Method to intialize the Database Session
    def getSession(self):
        database = self.databaseSetup(db_url)
        Session = sessionmaker(bind=database)
        session = Session()
        return session

    # Function to insert the object into database.
    def insertCart(self, session, cartInfo):
        session.add(cartInfo)
        session.commit()
        print('Record in database Cart Info >>', cartInfo.id)

    # Function to Query the object into database.
    def getCartInfo(self, session, queryValue):
        cart_by_creditCardNumber = session.query(CartInfo).filter(CartInfo.creditCardNumber == queryValue).first()
        print(cart_by_creditCardNumber)

# Main Method
if __name__ == "__main__":
    db_url = 'sqlite:///:memory:'
    databaseDriver = DatabaseDriver()
    dbSession = databaseDriver.getSession()
    cartInfo = CartInfo(customerFirstName='JOE',
                        customerLastName='APPROVAL',
                        productName='PEN', price=2.99,
                        quantity=2,
                        creditCardNumber='6123456789')
    cartInfo1 = CartInfo(customerFirstName='SAM',
                         customerLastName='APPROVAL',
                         productName='COKE', price=5.99,
                         quantity=1,
                         creditCardNumber='4567891234')
    databaseDriver.insertCart(dbSession, cartInfo)
    databaseDriver.insertCart(dbSession, cartInfo1)
    databaseDriver.getCartInfo(dbSession, '6123456789')
    databaseDriver.getCartInfo(dbSession, '4567891234')

from sqlalchemy import create_engine, Integer, String, Column, DateTime, ForeignKey, Float, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sqlite3.db', echo=True)
base = declarative_base()


class Customer(base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    selling_price = Column(Float(), nullable=False)
    quantity = Column(Integer())
    serial_number = Column(Integer())


class Order(base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", backref='order')
    order_number = Column(Integer())


class OrderLine(base):
    __tablename__ = 'order_lines'
    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


class Materials(base):
    __tablename__ = "materials"
    id = Column(Integer(), primary_key=True)
    material_name = Column(String(25), nullable=False)


engine.connect()
base.metadata.create_all(engine)

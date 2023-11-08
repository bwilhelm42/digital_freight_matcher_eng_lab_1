from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # Assuming a name field to identify the client
    locations = relationship('Location', back_populates='client')


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    marked = Column(Boolean)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', back_populates='locations')


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    location_origin_id = Column(Integer, ForeignKey('location.id'))
    location_dest_id = Column(Integer, ForeignKey('location.id'))
    client_id = Column(Integer, ForeignKey('client.id'))
    cargo_id = Column(Integer, ForeignKey('cargo.id'))
    route_id = Column(Integer, ForeignKey('route.id'))
    contract_type = Column(String(50))
    location_origin = relationship('Location', foreign_keys=[location_origin_id])
    location_dest = relationship('Location', foreign_keys=[location_dest_id])
    client = relationship('Client')
    cargo = relationship('Cargo')
    route = relationship('Route', back_populates='orders')


class Cargo(Base):
    __tablename__ = 'cargo'
    id = Column(Integer, primary_key=True)
    volume = Column(Float)
    weight = Column(Float)
    type = Column(String(50))
    orders = relationship('Order', back_populates='cargo')
    trucks = relationship('Truck', secondary='cargo_truck', back_populates='cargos')
    packages = relationship('Package', backref='cargo')


class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    volume = Column(Float)
    weight = Column(Float)
    type = Column(String(50))
    cargo_id = Column(Integer, ForeignKey('cargo.id'))


class Truck(Base):
    __tablename__ = 'truck'
    id = Column(Integer, primary_key=True)
    autonomy = Column(Float)
    capacity = Column(Float)
    type = Column(String(50))
    cargos = relationship('Cargo', secondary='cargo_truck', back_populates='trucks')


class Route(Base):
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True)
    location_origin_id = Column(Integer, ForeignKey('location.id'))
    location_dest_id = Column(Integer, ForeignKey('location.id'))
    profitability = Column(Float)
    location_origin = relationship('Location', foreign_keys=[location_origin_id])
    location_dest = relationship('Location', foreign_keys=[location_dest_id])
    orders = relationship('Order', back_populates='route')
    path = relationship('Location', secondary='route_location')


# Association Table for Many-to-Many relationship between Cargo and Truck
cargo_truck_association = Table('cargo_truck', Base.metadata,
                                Column('cargo_id', ForeignKey('cargo.id'), primary_key=True),
                                Column('truck_id', ForeignKey('truck.id'), primary_key=True)
                                )

# Association Table for Many-to-Many relationship between Route and Location
route_location_association = Table('route_location', Base.metadata,
                                   Column('route_id', ForeignKey('route.id'), primary_key=True),
                                   Column('location_id', ForeignKey('location.id'), primary_key=True)
                                   )

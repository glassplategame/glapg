from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from glapg.database import Model

branches = Table('branch', Model.metadata,
    Column('cube_id', Integer, ForeignKey('cube.id')),
    Column('connection_id', Integer, ForeignKey('connection.id'))
)

class Board(Model):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True)
    name = Column(String(63))

class Cube(Model):
    """Represents one if the player's moves."""
    __tablename__ = 'cube'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('board.id'))
    board = relationship('Board')
    plate_id = Column(Integer, ForeignKey('plate.id'))
    plate = relationship('Plate')
    # The sequential order in which this cube was placed.
    number = Column(Integer)
    state = Column(Integer)
    created = Column(DateTime)

class Plate(Model):
    """Represents one of the 'plates' in the Glass Plate Game."""
    __tablename__ = 'plate'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('board.id'))
    board = relationship('Board')
    # The plate's textual representation.
    name = Column(String(63))
    # The plate's visual representation.
    image_name = Column(String(63))

class Connection(Model):
    """Represents a connection between multiple cubes."""
    __tablename__ = 'connection'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('board.id'))
    board = relationship('Board')
    connection_next_id = Column(Integer, ForeignKey('connection.id'))
    connection_next = relationship('Connection')
    train_id = Column(Integer, ForeignKey('train.id'))
    train = relationship('Train')
    color = Column(Integer)
    # Player's description for the connection.
    text = Column(String(1023))
    cubes_prev = relationship('Cube', secondary=branches)
    cube_next = Column(Integer, ForeignKey('cube.id'))

class Train(Model):
    __tablename__ = 'train'

    id = Column(Integer, primary_key=True)
    color = Column(Integer)

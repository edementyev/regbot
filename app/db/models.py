import sqlalchemy.orm
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from app.utils import clock

Base = declarative_base()


def insert_me(self, session: sqlalchemy.orm.Session):
    session.add(self)
    session.commit()
    return self


def delete_me(self, session: sqlalchemy.orm.Session):
    session.delete(self)
    session.commit()
    return None


Base.insert_me = insert_me
Base.delete_me = delete_me


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    username = Column(String(255))
    name_surname = Column(String(255))
    edit_datetime = Column(DateTime, default=clock.now())

    def __init__(self,
                 uid,
                 username='',
                 name_surname='',
                 edit_datetime=clock.now()):
        self.uid = uid
        self.username = username
        self.name_surname = name_surname
        self.edit_datetime = edit_datetime

    def __repr__(self):
        return "User(id={}, uid={}, username={}, name_surname={}, edit_datetime={})" \
            .format(self.id, self.uid, self.username, self.name_surname, self.edit_datetime)


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(1000))
    hello_message = Column(String(1000))
    complete_message = Column(String(1000))
    edit_datetime = Column(DateTime, default=clock.now())

    def __init__(self,
                 title='',
                 description='',
                 hello_message='',
                 complete_message='',
                 edit_datetime=clock.now()):
        self.title = title
        self.description = description
        self.hello_message = hello_message
        self.complete_message = complete_message
        self.edit_datetime = edit_datetime

    def __repr__(self):
        return "Event(id={}, title={}, description={}, hello_message={}, complete_message={}, edit_datetime={})" \
            .format(self.id, self.title, self.description, self. hello_message, self. complete_message, self.edit_datetime)


class Enrollment(Base):
    __tablename__ = 'enrollment'
    id = Column(Integer, primary_key=True)
    complete = Column(Boolean(), default=False)
    admin_check = Column(Boolean(), default=False)
    file_type = Column(String(10))
    file_id = Column(String(1000))
    edit_datetime = Column(DateTime, default=clock.now())

    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    event_id = Column(Integer, ForeignKey('event.id'), index=True)

    user = relationship('User', backref='user_receipts', foreign_keys=[user_id])
    event = relationship('Event', backref='event_enrollments', foreign_keys=[event_id])

    def __init__(self,
                 user_id,
                 event_id,
                 complete=False,
                 admin_check=False,
                 file_type='',
                 file_id='',
                 edit_datetime=clock.now()):
        self.user_id = user_id
        self.event_id = event_id
        self.complete = complete
        self.admin_check = admin_check
        self.file_type = file_type
        self.file_id = file_id
        self.edit_datetime = edit_datetime

    def __repr__(self):
        return "Enrollment(id={}, user_id={}, event_id={}, complete={}, " \
               "admin_check={}, file_type={}, file_id={}, edit_datetime={})" \
            .format(self.id, self.user_id, self.event_id, self.complete,
                    self.admin_check, self.file_type, self. file_id, self.edit_datetime)

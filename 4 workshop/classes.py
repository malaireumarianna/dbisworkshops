from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sql_connection import engine
import json

from sqlalchemy.util import symbol

Base = declarative_base()

from sqlalchemy.orm import relationship, sessionmaker

class Categories(Base):

    __tablename__ = 'vacancy_categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(50))

    styles = relationship('Vacancy', backref='vacancy_categories', lazy=True)


class Vacancy(Base):

    __tablename__ = 'vacancy'

    id = Column(Integer, primary_key=True)
    vacancy_name = Column(String(50))
    id_category = Column(Integer, ForeignKey("vacancy_categories.id"))
    text_description = Column(String(100))
    about_company = Column(String(100))
    skills = Column(String(800))


class Users_users(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_username = Column(String(50))

class Opinion_of_workers(Base):

    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True)
    grade_value = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    vacancy_id = Column(Integer, ForeignKey("vacancy.id"))
    text_reviw = Column(String(100))

    styles = relationship('Users_users', backref='grade', lazy=True)
    styles_ = relationship('Vacancy', backref='grade', lazy=True)



Session = sessionmaker(bind = engine)
session = Session()

categories = open("C:/Users/Marianna/Desktop/4 workshop/categories.json",encoding="utf-8")
data_categories = json.load(categories)

vacancy = open("C:/Users/Marianna/Desktop/4 workshop/vacancy.json",encoding="utf8")
data_vacancy = json.load(vacancy)

session.add_all([
   Categories(id = data_categories['categories'][0]['id'], category_name = data_categories['categories'][0]['name']),
   Categories(id = data_categories['categories'][1]['id'], category_name = data_categories['categories'][1]['name']),
   Categories(id = data_categories['categories'][2]['id'], category_name = data_categories['categories'][2]['name']),
  ]
)

session.add_all([
    Vacancy(id = data_vacancy['vacancy'][0]['id'],
           vacancy_name = data_vacancy['vacancy'][0]['vacancy_name'],
           id_category=data_vacancy['vacancy'][0]['id_category'],
           text_description = data_vacancy['vacancy'][0]['text_description'],
           about_company=data_vacancy['vacancy'][0]['about_company'],
           skills=data_vacancy['vacancy'][0]['skills']),

    Vacancy(id=data_vacancy['vacancy'][1]['id'],
           vacancy_name=data_vacancy['vacancy'][1]['vacancy_name'],
           id_category=data_vacancy['vacancy'][1]['id_category'],
           text_description = data_vacancy['vacancy'][1]['text_description'],
           about_company=data_vacancy['vacancy'][1]['about_company'],
           skills=data_vacancy['vacancy'][1]['skills']),

    Vacancy(id = data_vacancy['vacancy'][2]['id'],
           vacancy_name = data_vacancy['vacancy'][2]['vacancy_name'],
           id_category=data_vacancy['vacancy'][2]['id_category'],
           text_description = data_vacancy['vacancy'][2]['text_description'],
           about_company=data_vacancy['vacancy'][2]['about_company'],
           skills=data_vacancy['vacancy'][2]['skills']),
]
)

session.commit()
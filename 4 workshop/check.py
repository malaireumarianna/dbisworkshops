from sql_connection import engine
from classes import Categories, Vacancy, Users_users, Opinion_of_workers, Base
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc, update
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def check_user_exist(username):

    try:
        if bool(session.query(Users_users.id).filter_by(id = '1').first()) is False:

            row = Users_users(id = '1',user_username = username)
            session.add(row)
            session.commit()
            search_query = (session.query(Users_users).filter_by(id = '1').one()).user_username

            print('Hello,', search_query)

        else:
            if bool(session.query(Users_users.user_username).filter_by(user_username = username).first()) is True:
                print('User already exist')

            else:
                id_value = session.query(Users_users.id).count()
                row = Users_users(id=id_value+1, user_username=username)
                session.add(row)
                session.commit()

    except:
        print('This user already exsist')




def opinion_of_workers(id,grade,values,id_user,vacancy_id,text):
    if grade > 5:
        print('Max value is 5')
    else:
        row = Opinion_of_workers(id=id, grade_value=values,user_id = id_user,vacancy_id = vacancy_id,text_reviw = text)
        session.add(row)
        session.commit()

def check_is_vacancy_exist(vacancy_name):
    if bool(session.query(Vacancy.vacancy_name).filter_by(vacancy_name= vacancy_name).first()) is False:
        print('This vacancy not exist in our database')
    else:
        result = session.query(Vacancy).filter(Vacancy.vacancy_name == vacancy_name).one().text_description
        print("Vacancy:", result)
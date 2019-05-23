import cx_Oracle
from example.Tereshchenko_Igor.workshop4.source.dao.credentials import *

# Help
# https://www.oracle.com/technetwork/articles/prez-stored-proc-084100.html

def getSkillData(skill_name=None):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    if not skill_name:
        query = 'select * from table(user_skillS.GetSkillData())'
        cursor.execute(query)
    else:
        query = 'select * from table(user_skillS.GetSkillData(:skill_name))'
        cursor.execute(query, skill_name=skill_name)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result



def getUserId(user_email, user_password):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    user_id = cursor.callfunc("USER_AUTH.GET_USER_ID", cx_Oracle.NATIVE_INT, [user_email, user_password])

    cursor.close()
    connection.close()

    return user_id


def newUser(USER_STUDYBOOK, USER_YEAR, USER_NAME, USER_EMAIL, USER_BIRTHDAY, USER_PASSWORD):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    user_id = cursor.var(cx_Oracle.NATIVE_INT)
    status = cursor.var(cx_Oracle.STRING)

    cursor.callproc("USER_AUTH.NEW_USER", [user_id, status, USER_STUDYBOOK, USER_YEAR, USER_NAME, USER_EMAIL, USER_BIRTHDAY, USER_PASSWORD])
    cursor.close()
    connection.close()

    return user_id.getvalue(), status.getvalue()



def getUsers():
    connection = cx_Oracle.connect(username, password, databaseName)

    cursor = connection.cursor()


    query = 'SELECT * FROM "user"'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# Run this module Ctrl+Shift+F10

if __name__ == "__main__":
    print(getSkillData('Java'))
    print(getSkillData())

    # [('Java', 1)]
    # [('Oracle', 1), ('Java', 1)]



    print(getUserId('PETRO@GMAIL.COM','222'))
    # 2


    print(newUser('KM5555', '10-OCT-17', 'Kate', 'KATE@GMAIL.COM', '21-OCT-97','555'))



    print(getUsers())
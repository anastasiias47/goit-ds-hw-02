import faker
from random import randint, choice
import sqlite3

number_users = 20
number_tasks = 10

def generate_fake_data(number_users, number_tasks):
    fake_fullname = []
    fake_email=[]
    fake_title = []
    fake_description = []

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_fullname.append(fake_data.name())
        fake_email.append(fake_data.email())
    
    for _ in range(number_tasks):
        fake_title.append(fake_data.text()[:20])
        fake_description.append(fake_data.text())
    
    return fake_fullname, fake_email, fake_title, fake_description

def prepare_data(fullname,email,title, description):
    for_users = []
    for_tasks = []
     
    for user, email in zip(fullname, email):
        for_users.append((user,email))

    for title, description in zip(title, description):
        for_tasks.append((title, description, randint(1,3), randint(1,20)))

    for_status = [('new',), ('in progress',), ('completed',)]

    return for_users, for_status, for_tasks

def load_data_to_db(users, status, tasks):

    with sqlite3.connect("database1.db") as con:
        cur = con.cursor()

        sql_to_users = 'INSERT INTO users(fullname, email) VALUES(?,?)'

        cur.executemany(sql_to_users, users)

        sql_to_status = 'INSERT INTO status(status) VALUES(?)'
    
        cur.executemany(sql_to_status, status)

        sql_to_tasks = 'INSERT INTO tasks(title, description, status_id, user_id ) VALUES(?,?,?,?)'

        cur.executemany(sql_to_tasks, tasks)
        
        con.commit()

if __name__ == "__main__":
    users, status, tasks = prepare_data(*generate_fake_data(number_users, number_tasks))
    load_data_to_db(users, status, tasks)
    






from flask_script import Manager
from app import app, mydb, TimelinePost

manager = Manager(app)

@manager.command
def initdb():
    mydb.connect()
    mydb.create_tables([TimelinePost])
    mydb.close()
    print('Initialized the database.')

if __name__ == '__main__':
    manager.run()


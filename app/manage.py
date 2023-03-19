# Import the necessary libraries
from flask_script import Manager
from app import mydb, TimelinePost

# Create an instance of the Manager class
manager = Manager(app)

# Define a new command for the Manager class called "initdb"
@manager.command
def initdb():
    """
    Initializes the database by connecting to it, creating the necessary tables, and then closing the connection.
    """
    # Connect to the database
    mydb.connect()

    # Create the necessary tables
    mydb.create_tables([TimelinePost])

    # Close the connection to the database
    mydb.close()

    # Print a message to indicate that the database has been initialized
    print('Initialized the database.')

# If this script is being run as the main program...
if __name__ == '__main__':
    # ...run the manager
    manager.run()


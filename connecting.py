from configparser import ConfigParser
import psycopg2

def config(filename='creds/credentials.ini', section='postgresql'):
    """Method for reading configs from a config file
    stored in ./creds/credentials.ini (as default)
    """

    # creating a parser object
    parser = ConfigParser()
    # reading creds from the file
    parser.read(filename)

    db = {}

    # checking if the .ini file has our psql section
    # throwing exception if it does not
    # else iterating through its content
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section \'{0}\' not found in the \'{1}\' file.".format(section, filename))

    return db


'''def connect():
    """Method used for connecting to an arbitrary pSQL database
    """

    conn = None

    try:
        # getting creds
        params = config()

        # connecting...
        print("Trying to connect...")
        conn = psycopg2.connect(**params)

        # Creating a cursor
        cur = conn.cursor()
'''

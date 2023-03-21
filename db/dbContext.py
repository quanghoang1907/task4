from mysql.connector import MySQLConnection, Error

def connect():
    db_config = {
            'host': 'localhost',
            'database': 'pythondb',
            'user': 'root',
            'password': '19072002hoangnunnnnn'
        }
    conn = None
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            return conn
    except Error as error:
        print(error)
        return conn

def disconnect(conn: MySQLConnection):
    if conn is not None:
        conn.rollback()
        conn.close()

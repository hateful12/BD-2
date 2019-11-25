import psycopg2


# Function that returns connection to DB
def makeConnect():
    return psycopg2.connect(
        user="postgres",
        password="1",
        host="localhost",
        port="5432",
        database="postgres",
    )


# Function that closes connection to DB
def closeConnect(connection):
    connection.commit()
    connection.close()

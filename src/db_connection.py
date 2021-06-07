import psycopg2

def get_connection():
    return psycopg2.connect(
        user = "postgres",
        password = "1234",
        host = "postgres",
        port = "5432",
        database = "postgres"
    )


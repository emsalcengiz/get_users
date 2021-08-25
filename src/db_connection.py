import psycopg2

def get_connection():
    return psycopg2.connect(
        user = "postgres",
        password = "****",
        host = "xyz",
        port = "5432",
        database = "postgres"
    )


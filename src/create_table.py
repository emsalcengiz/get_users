from db_connection import get_connection


def create_tables():
    try:
        db = get_connection()
        imlec = db.cursor()
        drop_user = """ drop table if exists users;"""
        query_users = """
                CREATE TABLE users (
                    id serial primary key,
                    userid VARCHAR(255),
                    location VARCHAR(255)
                )
                """     
        drop_job = """ drop table if exists jobs;"""  
        query_jobs = """
                CREATE TABLE jobs(
                    id serial primary key,
                    userid VARCHAR(255),
                    location VARCHAR(255),
                    servicename VARCHAR(255),
                    revenue Bigint,
                    jobstatus VARCHAR(255),
                    jobidentifier Bigint,
                    jobdate timestamp,
                    jobcreatedate timestamp)   
          
              """
        imlec.execute(drop_user)
        imlec.execute(query_users)
        imlec.execute(drop_job)
        imlec.execute(query_jobs)
        imlec.close()
        db.commit()
    except Exception as e:
        print(e)
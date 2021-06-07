from create_table import create_tables
from readjson import *
from db_connection import get_connection

create_tables()
users = read_users()
jobs  = read_jobs()
conn = get_connection()
imlec = conn.cursor()
for user in users:
    imlec.execute(
        f"""
        insert into users(userid, location) values({user.get('userid')},{user.get('location')})""")

for job in jobs:
    imlec.execute(
        f"""
        insert into jobs(userid, location,servicename,revenue,jobstatus,jobidentifier,jobdate,jobcreatedate) values({job.get('userid')},
                                {job.get('location')},
                                {job.get('servicename')},
                                {job.get('revenue')},
                                '{job.get('jobstatus')}',
                                {job.get('jobidentifier')},
                                '{job.get('jobdate')}',
                                '{job.get('jobcreatedate')}')""")
imlec.close()
conn.commit()






    
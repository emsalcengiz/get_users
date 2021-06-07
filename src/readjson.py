import json
from datetime import datetime


def read_users():
    data = []
    with open('users.json') as f:
        for line in f:
            res = json.loads(line)
            userid = res.get('USERID')
            location = res.get('LOCATION').split("_")[1]
            
            data.append({
                'userid' : userid,
                'location' : location
            })
            
    return data

def read_jobs():
    data = []
    with open('jobs.json') as f:
        for line in f:
            res = json.loads(line)
            userid = res.get('USERID')
            location = res.get('LOCATION').split("_")[1]
            servicename = res.get('SERVICENAME').split("_")[1]
            revenue = res.get('REVENUE')
            jobstatus = res.get('JOBSTATUS')
            jobidentifier = res.get('JOBIDENTIFIER')
            jobdate = res.get('JOBDATE').split(".")[0]
            jobcreatedate = res.get('JOBCREATEDATE').split(".")[0]
            
            data.append({
                'userid' : userid,
                'location' : location,
                'servicename': servicename,
                'revenue':revenue,
                'jobstatus':jobstatus,
                'jobidentifier':jobidentifier,
                'jobdate':jobdate,
                'jobcreatedate':jobcreatedate
            })
            
    return data

if __name__ == "__main__":
    print(read_users())
    print(read_jobs()[0])
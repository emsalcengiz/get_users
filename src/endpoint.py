from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from model.users import User
from model.jobs import Job
from sqlalchemy import func, desc, and_
from init import *


DB_URL = 'postgresql://postgres:****@postgres:5432/postgres'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

app.app_context().push()


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    userdata = []
    for user in users:
        userdata.append({
            'id': user.id,
            'userid': user.userid,
            'location': user.location
        })

    return jsonify(userdata)

   
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    jobdata = []
    for job in jobs:
        jobdata.append({
            'id': job.id,
            'userid': job.userid,
            'location': job.location,
            'servicename': job.servicename,
            'revenue': job.revenue,
            'jobstatus': job.jobstatus,
            'jobidentifier': job.jobidentifier,
            'jobdate': job.jobdate,
            'jobcreatedate': job.jobcreatedate
        })
    return jsonify(jobdata)


@app.route('/top_users/<location>', methods=['GET'])
def get_max_revenue_users(location):
    find_user_query = db.session.query(func.sum(Job.revenue).label("total_revenue"), Job.userid) \
    .join(User, Job.userid == User.userid ) \
    .filter(User.location != location).filter(and_(Job.location == location)) \
    .group_by(Job.userid).order_by(desc('total_revenue')).limit(5).all()
    users = []
    for user in find_user_query:
        users.append({
         'userid': int(user[1])
        })
    return jsonify(users)



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)

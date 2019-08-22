from app import db

class User(db.Model):
    __tablename__ = 'user'	
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    taskname = db.Column(db.String(120),nullable=True)
    tasktime = db.Column(db.String(120),nullable=True)

    def __init__(self, username, taskname ,tasktime):
        self.username = username
        self.taskname = taskname
        self.tasktime = tasktime
    def __repr__(self):
        return '<User %r>' % self.username

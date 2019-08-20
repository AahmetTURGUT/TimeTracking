from app import app,db
from flask import redirect,render_template, flash, url_for,request , jsonify,json ,Markup
from flask_sqlalchemy import SQLAlchemy
from app.models import User
import sys ,time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    text = request.form['text']
    user = User.query.filter_by(username=text).first()
    if user is None:
        return redirect(url_for('reopen',name=text))
    return redirect(url_for('reopen',name=text))

@app.route('/bar/<name>/')
def bar(name):
    time.sleep(0.5)
    datas=User.query.filter_by(username=name).first()
    top=0;
    if datas.taskname:
        labels = datas.taskname.split(" ");
        values = datas.tasktime.split(" ");
        labels.insert(0,"SUM")
        for i in range(len(labels)):
            labels[i]="TASK:"+""+labels[i].upper()
        for item in values:
                top+=int(item)
        values.insert(0,top)
        title="Report:"+""+name.upper()
        return render_template('chart.html', title=title, max=top, labels=labels, values=values)
    return  render_template('chart.html', title=title+" "+"NO RECORD", max=100, labels=[0,0,0], values=[0,0,0])

@app.route('/process',methods= ['POST'])
def process():
    names = request.form['name']
    times = request.form['time']
    pathname = request.form['pathname']
    mylist = pathname.split("/")
    saveusername=mylist[2]
    if names:
        user = User.query.filter_by(username=saveusername).first()
        if user is None:
            u = User(username=saveusername,taskname=names,tasktime=times)
            db.session.add(u)
            db.session.commit()
            return jsonify({'output':names+" "+times})
        user.taskname=names
        user.tasktime=times
        db.session.commit()
        return jsonify({'output':names+" "+times})
    return jsonify({'error' : 'Missing data!'})

@app.route('/api/<name>/')
def api_get_data(name):
    datas=User.query.filter_by(username=name).first()
    if datas is None:
        return jsonify({'error' : 'Missing data!'})
    return json.jsonify({
        'taskname': datas.taskname,
        'tasktime': datas.tasktime,
    })

@app.route('/delete',methods= ['POST'])
def delete():
    pathname = request.form['pathname']
    mylist = pathname.split("/")
    deletename=mylist[2]
    user = User.query.filter_by(username=deletename).first()
    if user is None:
        u = User(username=deletename,taskname=None,tasktime=None)
        db.session.add(u)
        db.session.commit()
        return jsonify({'output':u})
    user.taskname=None
    user.tasktime=None
    db.session.commit()
    return jsonify({'output':deletename})

@app.route('/projectdelete',methods= ['POST'])
def projectdelete():
    pathname = request.form['pathname']
    mylist = pathname.split("/")
    deletename=mylist[2]
    user = User.query.filter_by(username=deletename).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({'output':deletename})

@app.route('/Project/<name>')
def reopen(name):
    return render_template('reopen.html')

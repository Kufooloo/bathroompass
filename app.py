from flask import Flask, render_template, request, redirect
import os
import time 
import datetime
import time
import csv

app = Flask(__name__)
@app.route('/credits')
def default():
 return "hello World"
@app.route('/back')
def back():
 now = datetime.datetime.now().strftime("%H:%M:%S")
 return render_template('back.html', variable=now)
@app.route('/')
def home():
 date_today = datetime.datetime.now().strftime("%Y-%m-%d")
 date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 path = os.getcwd()
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'
 open(f, mode='a+')
 if os.stat(f).st_size !=0:
  with open(f, mode='a+') as signout:
   signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

   signout_writer.writerow([date,str("returned")])

 return render_template('home.html')
 
@app.route('/', methods=['POST'])
def my_form_post():
 fname = request.form['fname']
 lname = request.form['lname']
 lname_up = lname.upper()
 fname_up = fname.upper()
 date_today = datetime.datetime.now().strftime("%Y-%m-%d")
 date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 path = os.getcwd()
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'

 with open(f, mode='a+') as signout:
  signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  signout_writer.writerow([fname_up,lname_up,date,str("left")])

 return redirect('http://127.0.0.1:5000/back')
 
 
if __name__ == '__main__':
 ip = '127.0.0.1'
 port = int(os.environ.get('PORT', 5000))
 app.run(host=ip, port=port, debug=True)

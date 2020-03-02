from flask import Flask, render_template, request, redirect
import os
import datetime
import csv
fname = "error"
lname = "error"
timeleft = datetime.datetime.now()
app = Flask(__name__)
@app.route('/credits')
def default():
 return "hello World"
@app.route('/back')
def back():
 global fname
 global lname
 
 now = datetime.datetime.now().strftime("%H:%M:%S")
 return render_template('back.html', variable=now, fnamew=fname, lnamew=lname)
@app.route('/')
def home():
 global fname
 global lname
 global timeleft 
 
 date_today = datetime.datetime.now().strftime("%Y-%m-%d")
 date = datetime.datetime.now().strftime("%H:%M:%S")
 now = datetime.datetime.now()
 timereturn = now-timeleft
 path = os.getcwd()
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'
 open(f, mode='a+')
 if fname != "error" or lname != "error":
  with open(f, mode='a+') as signout:
   signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

   signout_writer.writerow([fname.upper(), lname.upper(), date,str("returned"), str("total time out: ") + str(timereturn)])

 return render_template('home.html' )
 
@app.route('/', methods=['POST'])
def my_form_post():
 global fname
 global lname
 global timeleft
 fname = request.form['fname']
 lname = request.form['lname']
 lname_up = lname.upper()
 fname_up = fname.upper()
 date_today = datetime.datetime.now().strftime("%Y-%m-%d")
 date = datetime.datetime.now().strftime("%H:%M:%S")
 path = os.getcwd()
 f = path+'//signoutsheets//'+date_today+'signoutlog'+'.csv'
 timeleft = datetime.datetime.now()
 if fname != 'error' or lname != 'error':
  with open(f, mode='a+') as signout:
   signout_writer = csv.writer(signout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   signout_writer.writerow([fname_up,lname_up,date,str("left")])

 return redirect('http://127.0.0.1:5000/back')
 
 
if __name__ == '__main__':
 ip = '127.0.0.1'
 port = int(os.environ.get('PORT', 5000))
 app.run(host=ip, port=port, debug=True)

from flask import Flask, render_template
app = Flask(__name__)
import datetime
from time import localtime

@app.route('/')
@app.route("/")

def home():
    today = datetime.datetime.now()
    l_t = localtime()
    t_z = int(l_t.tm_gmtoff/(60*60))

    iso = today.isoformat()
    dat = iso[:-7]

    if t_z < 0:
        dat += '-'
    else: 
        dat += '+'
    
    if t_z < 10:
        dat += '0'

    dat += str(t_z) + ':00'

    return '<body>' + dat + '</body>' 

if __name__ == '__main__':
   app.run()

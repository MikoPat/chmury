from flask import Flask, render_template
app = Flask(__name__)
import datetime
from time import localtime

@app.route('/')
@app.route("/")

def home():
    today = datetime.datetime.now()
    lt = localtime()
    tz = int(lt.tm_gmtoff/(60*60))

    iso = today.isoformat()
    dat = iso[:-7]

    if tz < 0:
        dat += '-'
    else: 
        dat += '+'
    
    if tz < 10: 
        dat += '0'

    dat += str(tz) + ':00'

    return '<body>' + dat + '</body>' 

if __name__ == '__main__':
   app.run()
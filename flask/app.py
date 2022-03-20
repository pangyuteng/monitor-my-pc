import os
import sys
import subprocess
import datetime

from flask import (
    Flask, render_template, jsonify,
)

app = Flask(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates',
)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/')
def home():
    
    mydict = {}

    cmd_list_of_list = [
        ['nvidia-smi'],
        ['free','-mh'],
        ['sensors'],
        ['mpstat','-u','-P','ALL','1','1'],
    ]
    for cmd_list in cmd_list_of_list:
        key = ' '.join(cmd_list)
        output = subprocess.check_output(cmd_list).decode('utf-8')
        mydict[key] = output

    return render_template('monitor.html', mydict=mydict)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=5000)
    args = parser.parse_args()
    app.run(debug=True,host="0.0.0.0",port=args.port)

import os
from datetime import datetime, timedelta
import numpy as np
import math

import ujson

from flask import Flask, render_template, request, jsonify, after_this_request



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    
    @app.route('/request', methods=['GET'])
    def request():
        @after_this_request
        def add_header(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        #jsonResp = {'time1': time.strftime("%c"), 'time2': time.strftime("%c")}
        #jsonResp = {'time1': c1, 'time2': time.strftime("%c")}

        #print(jsonResp)

        #eclipseCircumstances = {'C1':c1, 'C2':c2, 'MID':mid, 'C3':c3, 'C4':c4}


        with open('/home/dmitrykolesnikov/CODE/EclipseProject/skyfield/ec.json', "r") as jf:
            ec = ujson.load(jf)

        now = datetime.now()

        ec['now'] = {'year': int(now.year), 'month': int(now.month), 'day': int(now.day), 'hour': int(now.hour), 'minute': int(now.minute), 'second': float(now.second)}
        
        c1 = datetime(ec['c1']['year'], ec['c1']['month'], ec['c1']['day'], ec['c1']['hour'], ec['c1']['minute'], int(math.floor(ec['c1']['second'])), int((ec['c1']['second']%1)*1e6))
        c2 = datetime(ec['c2']['year'], ec['c2']['month'], ec['c2']['day'], ec['c2']['hour'], ec['c2']['minute'], int(math.floor(ec['c2']['second'])), int((ec['c2']['second']%1)*1e6))
        mid = datetime(ec['mid']['year'], ec['mid']['month'], ec['mid']['day'], ec['mid']['hour'], ec['mid']['minute'], int(math.floor(ec['mid']['second'])), int((ec['mid']['second']%1)*1e6))
        c3 = datetime(ec['c3']['year'], ec['c3']['month'], ec['c3']['day'], ec['c3']['hour'], ec['c3']['minute'], int(math.floor(ec['c3']['second'])), int((ec['c3']['second']%1)*1e6))
        c4 = datetime(ec['c4']['year'], ec['c4']['month'], ec['c4']['day'], ec['c4']['hour'], ec['c4']['minute'], int(math.floor(ec['c4']['second'])), int((ec['c4']['second']%1)*1e6))
        
        ec['countdown_c1'] = {'days': (c1-now).days,
                              'hours': (c1-now).seconds//3600,
                              'minutes': ((c1-now).seconds % 3600) // 60,
                              'seconds': ((c1-now).seconds % 60) + ((c1-now).microseconds/1e6)
        }
        # ec['countdown_c2'] = now-c2
        # ec['countdown_mid'] = now-mid
        # ec['countdown_c3'] = now-c3
        # ec['countdown_c4'] = now-c4

        print("******",  ec['countdown_c1'])
        
        
        return jsonify(ec)

    
    @app.route('/time')
    def hello():
        return render_template('time.html')
        
        
    return app

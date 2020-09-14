import os
import time
import numpy as np
from skyfield.api import load
from skyfield.api import Topos
from . import eclipseTimes
from flask import Flask, render_template, request, jsonify, after_this_request


planets = load('de421.bsp')
r_moon = 1737.4 #km
r_sun = 696000.0 #km

p = Topos('39.88836 S', '69.87577 W', elevation_m=449)
date = load.timescale().utc(2020, 12, 14)

c1 = eclipseTimes.t_c1(date, p, r_moon, r_sun, 1e-5).utc
c2 = eclipseTimes.t_c2(date, p, r_moon, r_sun, 1e-5).utc
mid = eclipseTimes.t_center(date, p, 1e-4).utc
c3 = eclipseTimes.t_c3(date, p, r_moon, r_sun, 1e-5).utc
c4 = eclipseTimes.t_c4(date, p, r_moon, r_sun, 1e-5).utc

#print("***********", type(c1.year), c1.year)

# eclipseCircumstances = {'C1':c1[0], 'C2':c2[0], 'MID':mid[0], 'C3':c3[0], 'C4':c4[0]}

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

        
        EC = {'C1': {'year': float(c1.year), 'month': float(c1.month), 'day': float(c1.day), 'hour': float(c1.hour), 'minute': float(c1.minute), 'second': float(c1.second)},
              'C2': {'year': float(c2.year), 'month': float(c2.month), 'day': float(c2.day), 'hour': float(c2.hour), 'minute': float(c2.minute), 'second': float(c2.second)},
              'mid': {'year': float(mid.year), 'month': float(mid.month), 'day': float(mid.day), 'hour': float(mid.hour), 'minute': float(mid.minute), 'second': float(mid.second)},
              'C3': {'year': float(c3.year), 'month': float(c3.month), 'day': float(c3.day), 'hour': float(c3.hour), 'minute': float(c3.minute), 'second': float(c3.second)},
              'C4': {'year': float(c4.year), 'month': float(c4.month), 'day': float(c4.day), 'hour': float(c4.hour), 'minute': float(c4.minute), 'second': float(c4.second)},
        }
        return jsonify(EC)

    
    @app.route('/time')
    def hello():
        return render_template('time.html', time=time.strftime("%c"))
        
        
    return app

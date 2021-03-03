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



        delta_utc = 3    
        now = datetime.utcnow() - timedelta(hours=delta_utc)
        
        
        ec['now'] = {'year': int(now.year), 'month': int(now.month), 'day': int(now.day), 'hour': int(now.hour), 'minute': int(now.minute), 'second': float(now.second + now.microsecond*1e-6)}

        #print('********', ec['now'])
        
        c1 = datetime(ec['c1']['year'], ec['c1']['month'], ec['c1']['day'], ec['c1']['hour'], ec['c1']['minute'], int(math.floor(ec['c1']['second'])), int((ec['c1']['second']%1)*1e6))
        c2 = datetime(ec['c2']['year'], ec['c2']['month'], ec['c2']['day'], ec['c2']['hour'], ec['c2']['minute'], int(math.floor(ec['c2']['second'])), int((ec['c2']['second']%1)*1e6))
        mid = datetime(ec['mid']['year'], ec['mid']['month'], ec['mid']['day'], ec['mid']['hour'], ec['mid']['minute'], int(math.floor(ec['mid']['second'])), int((ec['mid']['second']%1)*1e6))
        c3 = datetime(ec['c3']['year'], ec['c3']['month'], ec['c3']['day'], ec['c3']['hour'], ec['c3']['minute'], int(math.floor(ec['c3']['second'])), int((ec['c3']['second']%1)*1e6))
        c4 = datetime(ec['c4']['year'], ec['c4']['month'], ec['c4']['day'], ec['c4']['hour'], ec['c4']['minute'], int(math.floor(ec['c4']['second'])), int((ec['c4']['second']%1)*1e6))


        if c1 >= now:
            ec['countdown_c1'] = {'sign': '+',
                                  'days': (c1-now).days,
                                  'hours': (c1-now).seconds//3600,
                                  'minutes': ((c1-now).seconds % 3600) // 60,
                                  'seconds': ((c1-now).seconds % 60) + ((c1-now).microseconds/1e6)
            }
        elif c1 < now:
            ec['countdown_c1'] = {'sign': '-',
                                  'days': (now-c1).days,
                                  'hours': (now-c1).seconds//3600,
                                  'minutes': ((now-c1).seconds % 3600) // 60,
                                  'seconds': ((now-c1).seconds % 60) + ((now-c1).microseconds/1e6)
            }


            
        if c2 >= now:
            ec['countdown_c2'] = {'sign': '+',
                                  'days': (c2-now).days,
                                  'hours': (c2-now).seconds//3600,
                                  'minutes': ((c2-now).seconds % 3600) // 60,
                                  'seconds': ((c2-now).seconds % 60) + ((c2-now).microseconds/1e6)
            }
        elif c2 < now:
            ec['countdown_c2'] = {'sign': '-',
                                  'days': (now-c2).days,
                                  'hours': (now-c2).seconds//3600,
                                  'minutes': ((now-c2).seconds % 3600) // 60,
                                  'seconds': ((now-c2).seconds % 60) + ((now-c2).microseconds/1e6)
            }

        if mid >= now:
            ec['countdown_mid'] = {'sign': '+',
                                  'days': (mid-now).days,
                                  'hours': (mid-now).seconds//3600,
                                  'minutes': ((mid-now).seconds % 3600) // 60,
                                  'seconds': ((mid-now).seconds % 60) + ((mid-now).microseconds/1e6)
            }
        elif mid < now:
            ec['countdown_mid'] = {'sign': '-',
                                  'days': (now-mid).days,
                                  'hours': (now-mid).seconds//3600,
                                  'minutes': ((now-mid).seconds % 3600) // 60,
                                  'seconds': ((now-mid).seconds % 60) + ((now-mid).microseconds/1e6)
            }
            
        if c3 >= now:
            ec['countdown_c3'] = {'sign': '+',
                                  'days': (c3-now).days,
                                  'hours': (c3-now).seconds//3600,
                                  'minutes': ((c3-now).seconds % 3600) // 60,
                                  'seconds': ((c3-now).seconds % 60) + ((c3-now).microseconds/1e6)
            }
            
        elif c3 < now:
            ec['countdown_c3'] = {'sign': '-',
                                  'days': (now-c3).days,
                                  'hours': (now-c3).seconds//3600,
                                  'minutes': ((now-c3).seconds % 3600) // 60,
                                  'seconds': ((now-c3).seconds % 60) + ((now-c3).microseconds/1e6)
            }

            
        if c4 >= now:
            ec['countdown_c4'] = {'sign': '+',
                                  'days': (c4-now).days,
                                  'hours': (c4-now).seconds//3600,
                                  'minutes': ((c4-now).seconds % 3600) // 60,
                                  'seconds': ((c4-now).seconds % 60) + ((c4-now).microseconds/1e6)
            }
        elif c4 < now:
            ec['countdown_c4'] = {'sign': '-',
                                  'days': (now-c4).days,
                                  'hours': (now-c4).seconds//3600,
                                  'minutes': ((now-c4).seconds % 3600) // 60,
                                  'seconds': ((now-c4).seconds % 60) + ((now-c4).microseconds/1e6)
            }

        
        
        return jsonify(ec)

    
    @app.route('/time')
    def hello():
        return render_template('time.html')
        
        
    return app

#!/usr/bin/python3
"""Package containing HBNB api blueprint"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    threaded = True
    app.run(host=host, port=port, threaded=threaded)


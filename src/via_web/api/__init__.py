import os

import bottle

from via import settings
from .journeys import *
from .info import *


@bottle.route('/')
def send_index():
    return render_page('index.tpl')


@bottle.route('/static/resources/:filename#.*#')
def get_static_resource(filename):
    return bottle.static_file(filename, root='static/resources/')


@bottle.route('/static/templates/:filename#.*#')
def render_page(filename):
    return bottle.template(
        os.path.join('static', 'templates', filename),
        initial_coords=[settings.VIZ_INITIAL_LAT, settings.VIZ_INITIAL_LNG],
        initial_zoom=settings.VIZ_INITIAL_ZOOM
    )


@bottle.route('/favicon.ico')
def get_favicon():
    return get_static_resource('favicon.ico')


print('loaded api routes...')

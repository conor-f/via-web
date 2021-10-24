import bottle

from via import settings


@bottle.route('/info')
def get_info():
    return {
        **{
            name: str(getattr(settings, name)) for name in dir(settings) if name.isupper()
        }
    }

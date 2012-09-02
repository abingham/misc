from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = UnencryptedCookieSessionFactoryConfig('password')
    config = Configurator(
        settings=settings,
        session_factory=session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('start', '/')
    config.add_route('question', '/question')
    config.add_route('respond', '/respond')
    config.scan()
    return config.make_wsgi_app()

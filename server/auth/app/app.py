from apistar import Include, Route, http
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls


def welcome(name=None):
    if name is None:
        return {'message': 'This is a test'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)

if __name__ == '__main__':
    app.main()

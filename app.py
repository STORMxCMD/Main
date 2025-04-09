from webob import Request, Response

class FrameWorkApp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, req):
        res = Response()

        for path, handler in self.routes.items():
            lst = req.path.split("/")

            if path == "/u/id" and len(lst) > 2:
                handler(req, res, lst[2])

            if path == req.path:
                handler(req, res)

        return res
    
    
    def default_response(self, response):
        response.status_code=404
        response.text="URL hatolik bor, topilmadi"
        
    def route(self, path):
        def wrapper(handler):
            self.routes[path]=handler
            return handler
        
        return wrapper
    
    

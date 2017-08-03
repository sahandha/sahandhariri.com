import os.path
import tornado.ioloop
import tornado.web
import os, uuid
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("static/index.html")

class SIRHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("static/SIR.html")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/SIR.html", SIRHandler),
            (r"/SIR", SIRHandler),
            # Add more paths here
            #(r"/KillTornado/", StopTornado),
            #(r"/tables/", ReturnQuery),
            (r"/tables/localhost8888", MainHandler)
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

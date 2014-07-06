#!/usr/local/bin/python
# coding: utf-8
__author__ = 'bruno'

from tornado import ioloop, web, httpserver
from tornado.options import define, options
import os

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(web.RequestHandler):

    def get(self):
        self.render("home.html", user=self._current_user)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret='8563f0f27e4c1201eef07d01c9ad3854f496c86e374fdbfcbfd64906c6725a1b',
            expires_days=None,
        )
        web.Application.__init__(self, handlers, **settings)


def main():
    options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
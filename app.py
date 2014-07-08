#!/usr/local/bin/python
# coding: utf-8
__author__ = 'bruno'

from tornado import ioloop, web, httpserver
from tornado.options import define, options
import os
from random import randint, choice

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(web.RequestHandler):

    def get(self):
        lvl = 16

        clases = []
        for i in range(1, (lvl/randint(2, 4))):
            cl = [i, randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50)]
            clases.append(cl)

        boxes = []
        for i in range(0, lvl):
            box = {
                'id': randint(1, 100000),
                'val': randint(1, lvl),
                'class': choice(["rad"+str(a[0]) for a in clases])
            }
            boxes.append(box)
        self.render("home.html", clases=clases, boxes=boxes)


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
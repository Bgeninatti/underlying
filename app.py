#!/usr/local/bin/python
# coding: utf-8
__author__ = 'bruno'

from tornado import ioloop, web, httpserver, escape
from tornado.options import define, options
import os
from random import randint, choice


define("port", default=8888, help="run on the given port", type=int)


class GameApiHandler(web.RequestHandler):

    def get(self, lvl=None):
        boxes = []
        if lvl is not None:
            lvl = 16
            for i in range(1, 17):
                box = {
                    'id': i,
                    'val': randint(1, 16),
                    'class': choice(["rad"+str(a) for a in range(1, 10)])
                }
                boxes.append(box)
        else:
            for i in range(1, 17):
                box = {
                    'id': i,
                    'val': 'U',
                    'class': "nolevel " + choice(["rad"+str(a) for a in range(1, 10)]),
                    'target': i+4
                }
                if box['target'] > 16:
                    box['target'] -= 16
                boxes.append(box)

        self.write(escape.json_encode(boxes))
        self.set_header("Content-Type", "application/json")


class MainHandler(web.RequestHandler):

    def get(self):

        clases = []
        for i in range(1, 10):
            cl = [i, randint(1, 50), randint(1, 50), randint(1, 50), randint(1, 50)]
            clases.append(cl)

        self.render("home.html", clases=clases)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/game", GameApiHandler),
            (r"/game/([0-9]+)", GameApiHandler),
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
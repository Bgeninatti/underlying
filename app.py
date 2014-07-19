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
        if lvl == 'simple_lvl':
            target_fila = randint(1, 4)
            target_columna = randint(1, 4)
            operation, inverse_operation = self._set_operations()
            for i in range(1, 17):
                box = {
                    'id': i,
                    'val': i,
                    'class': choice(["rad"+str(a) for a in range(1, 10)]),
                    'target': self._set_target(target_fila, target_columna, i),
                    'operation': operation,
                    'inverse': inverse_operation
                }
                if box['target'] > 16:
                    box['target'] -= 16
                boxes.append(box)
            boxes = self._random_permutations(boxes)
        else:
            for i in range(1, 17):
                box = {
                    'id': i,
                    'val': 'U',
                    'class': "nolevel " + choice(["rad"+str(a) for a in range(1, 10)]),
                    'target': None,
                    'operation': None,
                    'inverse': None,
                }
                boxes.append(box)

        self.write(escape.json_encode(boxes))
        self.set_header("Content-Type", "application/json")

    @staticmethod
    def _set_target(f, c, id):
        targ_num = (f * 4) + c + id
        target = targ_num if targ_num <= 16 else targ_num - 16
        return target

    @staticmethod
    def _set_operations():
        sign = choice(["+", "-"])
        inverse_sign = "-" if sign == "+" else "+"
        perm_value = randint(1, 5)
        operation = "{target} "+str(sign)+" "+str(perm_value)
        inverse_operation = "{target} "+str(inverse_sign)+" "+str(perm_value)
        return operation, inverse_operation

    @staticmethod
    def _random_permutations(boxes):
        for i in range(1, 21):
            op_type = choice(["operation", "inverse"])
            box = randint(1, 16) - 1
            target = boxes[box]['target'] - 1
            boxes[box]['val'] += 1
            boxes[target]['val'] = eval(boxes[box][op_type].replace("{target}", str(boxes[target]['val'])))
        return boxes


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
            (r"/game/([0-9a-z_]+)", GameApiHandler),
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
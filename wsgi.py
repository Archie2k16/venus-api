#!/usr/bin/env python
# encoding:utf-8
# me@archie.cc
import termcolor
from wsgiref.simple_server import make_server
from tools.dotdict import dot_dict
import simplejson as json

cprint = termcolor.cprint


def venus(env, response):
    data = {'path': env['PATH_INFO']}
    response_body = json.dumps({'code': 200, 'msg': 'ok', 'data': data})
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    response(status, headers)
    return [response_body]


def run():
    config = dot_dict({'host': '0.0.0.0',
                       'port': 8080,
                       })
    httpd = make_server(config.host, config.port, venus)
    cprint('Started HTTP Server at http://{}:{}...'.format(config.host, config.port), 'red')

    double_hit = False
    while 1:
        try:
            httpd.handle_request()
        except KeyboardInterrupt:
            if double_hit:
                exit()
            else:
                cprint('Hit "Ctrl+C" again to exit...', 'green')
                double_hit = True

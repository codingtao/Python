
from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 9123, application)
print('Serving HTTP on port 9123...')

httpd.serve_forever()
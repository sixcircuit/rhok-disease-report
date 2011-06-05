#!/usr/bin/python

import os
import tornado.ioloop
import tornado.web

settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world")

class IndexHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

class DiseaseReportHandler(tornado.web.RequestHandler):
  def post(self):
    print(self.request.arguments)    


application = tornado.web.Application([
  (r"/", IndexHandler),
  (r"/index", IndexHandler),
  (r"/report", DiseaseReportHandler)
], **settings)

if __name__ == "__main__":
  application.listen(80)
  print("Server listening on all addresses, port 80")
  tornado.ioloop.IOLoop.instance().start()


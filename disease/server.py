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


application = tornado.web.Application([
  (r"/", IndexHandler),
  (r"/index", IndexHandler)
], **settings)

if __name__ == "__main__":
  application.listen(80)
  tornado.ioloop.IOLoop.instance().start()


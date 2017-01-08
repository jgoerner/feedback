import web

urls = ('/(.*)', 'hello')

app = web.application(urls, globals())

class hello:
    def GET(self, _):
        return("Hello World - Awesome App will soon be here")

if __name__ == "__main__":
    app.run()

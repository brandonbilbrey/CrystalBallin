import web
import

urls = (
        '/(.*)', 'hello'
        )
app = web.application(urls, globals())

class hello:
    def GET(self, team1, team2):
        if not name:
            name = 'world'
    return 'Hello, ' + name + '!'

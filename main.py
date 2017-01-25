import webapp2
import caeser


class MainHandler(webapp2.RequestHandler):
    def get(self):
        message ="hello" 
	#encrypted_message = encrypt(message, rot)
	textarea = "<textarea>" + message + "</textarea>"
	submit = "<input type='submit'/>"
	form = "<form>" + textarea + "<br>" + submit + "</form>"
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

import webapp2
import cgi
import caeser

def build_page(textarea_content):
    
    header = "<h1>Web Caeser</h1>"
    rot_label = "<label>Rotate by:</label>"
    message_label = "<label>Type a message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    rotation_area = "<input type='number' name='rotation'/>"
    submit = "<input type='submit' value='Submit'/>"
    form = ("<form method='post'>" 
            + message_label + "<br>" + textarea + "<br>"
            + rot_label + "<br>" + rotation_area + "<br>" 
            + submit + "</form>")

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
	content = build_page("")
        self.response.write(content)
    
    def post(self):
	
        message = self.request.get("message")
	if self.request.get("rotation").isdigit():
	    rot = self.request.get("rotation") 
        else:
	    rot = 0
	encrypted_message = caeser.encrypt(message, rot)
        escaped_message = cgi.escape(encrypted_message) 
	content= build_page(escaped_message)

        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

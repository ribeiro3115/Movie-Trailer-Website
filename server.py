import SimpleHTTPServer
import SocketServer
import os
import data
import cgi

# This file has the responsability to create a small server in python

# Port of server
PORT = 7000

#
curdir = os.curdir
sep = os.sep


# Function to send response to the client of the GET requests
def do_GET(self):

	# Detect if is the Main Request
	if self.path.endswith("/"):
		# Send the HTMl file to client
		html_data = data.open_movies_page()
		
	else:
		# Send another files to client like files .css or .jpg
		file = open(curdir + sep + self.path)
		html_data = file.read()
	

	# Construc response to client
	self.send_response(200)
	self.end_headers()
	self.wfile.write(html_data)
	return


# Function to send response to the client of the POST requests
def do_POST(self):

		# Read the parameters from client
		form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
		
		# Construc response to client
		self.send_response(200)
		self.end_headers()
		self.wfile.write(data.get_movies_HTMl(form["id_page"].value));
		return



# Create Server in Python
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#Define Function of GET and POST
Handler.do_GET = do_GET
Handler.do_POST = do_POST
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
httpd.server_close()
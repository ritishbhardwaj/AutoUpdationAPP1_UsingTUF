import http.server
import socketserver,json
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the path from the request
        path = self.translate_path(self.path)
        print(path)
        
        # Check if the path is a file
        if os.path.isfile(path):
            # Serve the file if it exists
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            # Return a 404 error if the file does not exist
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b''' <h1> Directory Listing is Disabled</h1>
             "message": "This server does not allow directory listing." ''')
    

PORT = 5000
DIRECTORY = "temp_my_app/repository"
ol=os.path.abspath(DIRECTORY)
print('-------------------',ol)
os.chdir(ol)

# Start the server with the custom handler
with socketserver.TCPServer(("127.0.0.1", PORT), CustomHandler) as httpd:
    print("Server running at port", PORT)
    httpd.serve_forever()




















# else:
#     # Return a custom JSON response
#     self.send_response(400)
#     self.send_header('Content-type', 'application/json')
#     self.end_headers()
#     json_response = {
#         "error": "Directory Listing is Disabled",
#         "message": "This server does not allow directory listing."
#     }
#     # Serialize the JSON response
#     json_data = json.dumps(json_response)
#     self.wfile.write(json_data.encode('utf-8'))
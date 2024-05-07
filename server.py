from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the IP address, port, and directory to serve files from
host = '127.0.0.1'
port = 8000
directory = 'temp_my_app/repository'

# Create a custom request handler to disable directory listing
class NoListingHTTPRequestHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        # Override to prevent directory listing
        self.send_error(403, "Directory listing is disabled")

# Create the HTTP server
server_address = (host, port)
httpd = HTTPServer(server_address, NoListingHTTPRequestHandler)

# Print the server information
print(f"Serving directory '{directory}' at http://{host}:{port}/")

# Start serving requests indefinitely
httpd.serve_forever()

from waitress import serve
from server2_flask_server import app  # Replace with your actual app import
print('Yesssss')
serve(app, host='127.0.0.1', port=5000)

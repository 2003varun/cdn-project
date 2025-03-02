import os
import requests
from flask import Flask, send_from_directory, abort

app = Flask(__name__)
CACHE_DIR = 'cache'
ORIGIN_SERVER = 'http://localhost:5000/static/'  # Origin server URL

os.makedirs(CACHE_DIR, exist_ok=True)

@app.route('/static/<path:filename>')
def serve_file(filename):
    local_file = os.path.join(CACHE_DIR, filename)
    if os.path.exists(local_file):
        return send_from_directory(CACHE_DIR, filename)
    else:
        response = requests.get(ORIGIN_SERVER + filename, stream=True)
        if response.status_code == 200:
            with open(local_file, 'wb') as f:
                f.write(response.content)
            return send_from_directory(CACHE_DIR, filename)
        else:
            abort(404)

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # For edge_server_1

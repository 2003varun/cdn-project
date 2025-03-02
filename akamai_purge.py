import os
import shutil
from flask import Flask

app = Flask(__name__)

CACHE_DIRS = ['../edge_server_1/cache', '../edge_server_2/cache']

@app.route('/purge')
def purge_cache():
    for cache_dir in CACHE_DIRS:
        shutil.rmtree(cache_dir, ignore_errors=True)
        os.makedirs(cache_dir, exist_ok=True)
    return "Cache purged successfully from all edge servers."

if __name__ == '__main__':
    app.run(port=5004, debug=True)

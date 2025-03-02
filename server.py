from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    print("Serving index.html")
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

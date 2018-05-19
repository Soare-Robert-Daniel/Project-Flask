from flask import *
app = Flask(__name__)

from home import *
from page import *
from datebase import *
import os

@app.route("/")
def main():
    # index_path = os.path.join(app.static_folder, 'templates/main_page.html')
    rows = getRows()
    return render_template("main_page.html", rows=rows)

@app.route('/<path:path>')
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

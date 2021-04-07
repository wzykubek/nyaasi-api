import requests
from NyaaPy import Nyaa
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def api():
    requestArgs = request.args

    if "q" in requestArgs:
        query = requestArgs.get('q')
    else:
        query = ""

    if "category" in requestArgs:
        try:
            category = int(requestArgs.get('category'))
        except ValueError:
            return "Category argument must be integer number.", 400
    else:
        category = 0

    if "subcategory" in requestArgs:
        try:
            subcategory = int(requestArgs.get('subcategory'))
        except ValueError:
            return "Sub-category argument must be integer number.", 400
    else:
        subcategory = 0

    if "page" in requestArgs:
        try:
            page = int(requestArgs.get('page'))
            if page > 100 or page < 0:
                return "Page must be a integer number between 0 and 100."
        except ValueError:
            return "Page argument must be integer number.", 400
    else:
        page = 1

    try:
        pageTorrent = Nyaa.search(
            keyword=query,
            category=category,
            subcategory=subcategory,
            page=page,
        )
        return jsonify(pageTorrent), 200
    except requests.exceptions.ConnectionError:
        return "Trouble reaching nyaa.si", 404


@app.route("/view/<int:view_id>", methods=["GET"])
def view(view_id):
    try:
        viewTorrent = Nyaa.get(view_id)
        return jsonify(viewTorrent), 200
    except IndexError:
        return "Torrent not found", 400
    except requests.exceptions.ConnectionError:
        return "Trouble reaching nyaa.si", 404


if __name__ == "__main__":
    app.run(debug=True)

import requests
from flask import Flask, request, Response, json

from NyaaPy.nyaa import Nyaa

nyaa = Nyaa()
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

    if "sort" in requestArgs:
        sort = str(requestArgs.get('sort'))
    else:
        sort = "id"

    if "order" in requestArgs:
        order = str(requestArgs.get('order'))
    else:
        order = "desc"

    if "filters" in requestArgs:
        filters = str(requestArgs.get('filters'))
    else:
        filters = 0

    try:
        pageTorrent = nyaa.search(
            keyword=query,
            category=category,
            subcategory=subcategory,
            page=page,
            filters=filters,
            sort=sort,
            order=order
        )

        pageTorrentJson = json.dumps(pageTorrent, ensure_ascii=False)
        if pageTorrentJson == "[]":
            response = {'error': 'No results'}
            responseJson = json.dumps(response, indent=4)
            return responseJson, 400
        else:
            response = Response(pageTorrentJson, content_type="application/json; charset=utf-8")
            return response, 200
    except requests.exceptions.ConnectionError:
        response = {'error': 'Trouble reaching nyaa.si'}
        responseJson = json.dumps(response, indent=4)
        return responseJson, 404


@app.route("/view/<int:view_id>", methods=["GET"])
def view(view_id):
    try:
        viewTorrent = nyaa.get(view_id)
        viewTorrentJson = json.dumps(viewTorrent, ensure_ascii=False)
        response = Response(viewTorrentJson, content_type="application/json; charset=utf-8")
        if viewTorrentJson == "[]":
            response = {'error': 'No results'}
            responseJson = json.dumps(response, indent=4)
            return responseJson, 400
        else:
            return response, 200
    except IndexError:
        response = {'error': 'Torrent not found'}
        responseJson = json.dumps(response, indent=4)
        return responseJson, 400
    except requests.exceptions.ConnectionError:
        response = {'error': 'Trouble reaching nyaa.si'}
        responseJson = json.dumps(response, indent=4)
        return responseJson, 404


@app.route("/user/<username>", methods=["GET"])
def user(username):
    try:
        viewTorrent = nyaa.get_user(username)
        viewTorrentJson = json.dumps(viewTorrent, ensure_ascii=False)
        response = Response(viewTorrentJson, content_type="application/json; charset=utf-8")
        if viewTorrentJson == "[]":
            response = {'error': 'No results'}
            responseJson = json.dumps(response, indent=4)
            return responseJson, 400
        else:
            return response, 200
    except IndexError:
        response = {'error': 'Torrent not found'}
        responseJson = json.dumps(response, indent=4)
        return responseJson, 400
    except requests.exceptions.ConnectionError:
        response = {'error': 'Trouble reaching nyaa.si'}
        responseJson = json.dumps(response, indent=4)
        return responseJson, 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import request, jsonify
from NyaaPy import Nyaa
from . import app


@app.route("/", methods=["GET"])
def api():
    if "q" in request.args:
        if "category" in request.args:
            try:
                category = int(request.args["category"])
            except ValueError:
                return "Category argument must be integer number."
        else:
            category = 0

        if "subcategory" in request.args:
            try:
                subcategory = int(request.args["subcategory"])
            except ValueError:
                return "Subategory argument must be integer number."
        else:
            subcategory = 0

        if "page" in request.args:
            try:
                page = int(request.args["page"])
                if page > 1000 or page < 0:
                    return "Page must be a integer number between 0 and 1000."
            except ValueError:
                return "Page argument must be integer number."
        else:
            page = 1

        return jsonify(
            Nyaa.search(
                keyword=request.args["q"],
                category=category,
                subcategory=subcategory,
                page=page,
            )
        )
    else:
        return "Please specify required query argument."

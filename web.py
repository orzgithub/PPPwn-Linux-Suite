from flask import render_template, Blueprint, url_for, redirect

import global_var
import utils

web = Blueprint("web", __name__)


@web.route("/")
def index():
    lang = global_var.lang_dict[
        utils.get_config()["language"] if "language" in utils.get_config() else "en_US"
    ]
    return render_template("index.html", lang=lang), 200


@web.route("/payloads/")
def payloads():
    lang = global_var.lang_dict[
        utils.get_config()["language"] if "language" in utils.get_config() else "en_US"
    ]
    return render_template("payloads.html", lang=lang), 200


@web.route("/document/cs/ps4/index.html")
def document_redirect():
    return redirect(url_for("web.index"))

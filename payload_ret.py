from flask import Blueprint, send_file

payload_ret = Blueprint("payloads", __name__)


@payload_ret.route("/<fw_version>/<payload_name>")
def get_payload(fw_version, payload_name):
    return send_file("payloads/" + fw_version + "/" + payload_name)

import configparser
import os
import time
from threading import Thread

from flask import Flask, request, jsonify, Blueprint

from global_var import *

import utils
import tasks
import warnings

api = Blueprint("api", __name__)


@api.route("/start_pppwn", methods=["POST"])
def start_pppwn():
    if utils.check_port_enabled("192.168.1.2", 3232):
        return {}, 200

    def start_pppwn_process():
        config = utils.get_config()
        if tasks_save["pppoe"] is not None:
            tasks_save["pppoe"].terminate()
            tasks_save["pppoe"] = None
            os.system("killall pppoe-server")
            utils.reset_interface()
        tasks_save["pppwn"] = Process(target=tasks.pppwn_server, args=())
        tasks_save["pppwn"].start()
        tasks_save["pppwn"].join()
        tasks_save["pppwn"] = None
        utils.reset_interface()
        tasks_save["pppoe"] = Process(target=tasks.pppoe_server, args=())
        tasks_save["pppoe"].start()
        if "plugins_load_boot" in config and config["plugins_load_boot"]:
            while not utils.check_port_enabled("192.168.2.1", 3232):
                time.sleep(1)
            tasks.inject_payloads_auto()

    thread = Thread(target=start_pppwn_process)
    thread.start()
    return {}, 203


@api.route("/install_trainer", methods=["POST"])
def install_trainer():
    thread = Thread(target=tasks.install_trainer)
    thread.start()
    return {}, 203


@api.route("/save_config", methods=["POST"])
def save_config():
    save_config = request.get_json()
    print(save_config)
    for key in save_config:
        utils.set_config(key, save_config[key])
    return {}, 200


@api.route("/get_config", methods=["GET"])
def get_config():
    return utils.get_config(), 200


@api.route("/get_payloads", methods=["GET"])
def get_payloads():
    config = utils.get_config()
    return (
        payload_list[config["fw_version"]]
        if (config["fw_version"] if "fw_version" in config else 1100) in payload_list
        else {}
    ), 200


@api.route("/switch_payload", methods=["POST"])
def switch_payload():
    switch_payload = request.get_json()
    config = utils.get_config()
    plugins_load_boot = (
        config["plugins_load_boot"] if "plugins_load_boot" in config else []
    )
    for key in switch_payload:
        if key in plugins_load_boot:
            plugins_load_boot.remove(key)
        else:
            plugins_load_boot.append(key)
    utils.set_config("plugins_load_boot", plugins_load_boot)
    return {}, 200


@api.route("/enable_payload", methods=["POST"])
def enable_payload():
    enable_payload = request.get_json()
    config = utils.get_config()
    plugins_load_boot = (
        config["plugins_load_boot"] if "plugins_load_boot" in config else []
    )
    for key in enable_payload:
        if key not in plugins_load_boot:
            plugins_load_boot.append(key)
    utils.set_config("plugins_load_boot", plugins_load_boot)
    return {}, 200


@api.route("/disable_payload", methods=["POST"])
def disable_payload():
    disable_payload = request.get_json()
    config = utils.get_config()
    plugins_load_boot = (
        config["plugins_load_boot"] if "plugins_load_boot" in config else []
    )
    for key in disable_payload:
        if key in plugins_load_boot:
            plugins_load_boot.remove(key)
    utils.set_config("plugins_load_boot", plugins_load_boot)
    return {}, 200


@api.route("/get_fw_ver", methods=["GET"])
def get_os_ver_list():
    return fw_versions, 200


@api.route("/get_interface", methods=["GET"])
def get_interface_list():
    return utils.get_network_interfaces(), 200


@api.route("/get_lang", methods=["GET"])
def get_lang_list():
    return {lang_key: lang_dict[lang_key].LANG for lang_key in lang_dict}


@api.route("/load_payload", methods=["POST"])
def load_payload():
    load_payload = request.get_json()
    payload = load_payload["payload"]
    thread = Thread(target=utils.load_payload(payload))
    thread.start()
    return {}, 203

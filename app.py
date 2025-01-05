import os
import time
import atexit
from threading import Thread

from flask import Flask

import global_var
import utils
import tasks
from api import api
from payload_ret import payload_ret
from web import web
from global_var import *


def setup():
    config: dict[str:any] = utils.get_config()
    if "start_on_boot" in config and config["start_on_boot"]:
        tasks_save["pppwn"] = Process(target=tasks.pppwn_server, args=())
        tasks_save["pppwn"].start()
        tasks_save["pppwn"].join()
        tasks_save["pppwn"] = None
        utils.reset_interface()
    tasks_save["pppoe"] = Process(target=tasks.pppoe_server, args=())
    tasks_save["pppoe"].start()
    time.sleep(3)
    if (
        "start_on_boot" in config
        and "plugins_load_boot" in config
        and config["start_on_boot"]
        and config["fw_version"] in global_var.payload_list
    ):
        while not utils.check_port_enabled("192.168.2.1", 3232):
            time.sleep(1)
        thread = Thread(target=tasks.inject_payloads_auto())
        thread.start()


def cleanup():
    os.system("killall pppwn")
    os.system("killall pppoe-server")


class PPPwnFlask(Flask):
    def __init__(self, *args, **kwargs):
        setup()
        atexit.register(cleanup)
        super(PPPwnFlask, self).__init__(*args, **kwargs)


app: Flask = PPPwnFlask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(payload_ret, url_prefix="/payloads")
app.register_blueprint(web, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

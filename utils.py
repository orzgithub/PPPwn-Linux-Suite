import os
import time

import psutil
import json
import requests
import socket


def check_port_enabled(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False


def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    interface_list = []
    for interface in interfaces.items():
        interface_list.append(interface[0])
    return interface_list


def get_config():
    with open("config.json", "r") as json_file:
        config = json.load(json_file)
    return config


def set_config(key, value):
    config = get_config()
    config[key] = value
    with open("config.json", "w") as json_file:
        json_file.write(json.dumps(config))
    return config


def reset_interface():
    config = get_config()
    os.system(
        f"""
        ifconfig {config["interface"]} down
        sleep 1
        ifconfig {config["interface"]} up
        sleep 1
    """
    )


def load_payload(payload):
    try:
        while True:
            response = requests.post(url="http://192.168.1.2:9090/status")
            response_json = response.json()
            if response_json["status"] == "ready":
                break
            else:
                time.sleep(1)
        response = requests.post(
            url="http://192.168.1.2:9090", data=open(payload, "rb").read()
        )
        return 0
    except requests.exceptions.ConnectionError as e:
        print("Binloader server not enabled or device not connected.")
        return 1
    except Exception as e:
        print("Unexpected error:", e)
        return 2

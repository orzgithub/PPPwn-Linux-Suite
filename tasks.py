import os

import global_var
import utils
import warnings
import ftplib


def pppoe_server():
    print("starting pppoe server")
    config = utils.get_config()
    if "interface" in config:
        cmd = f"pppoe-server -I {config['interface']} -T 60 -N 1 -C isp -S isp -L 192.168.1.1 -R 192.168.1.2 -N 1"
        os.system(cmd)
    else:
        warnings.warn("interface not configured")


def pppwn_server():
    print("starting pppwn server")
    config = utils.get_config()
    if "interface" in config and "fw_version" in config:
        cmd = f"./pppwn --interface {config['interface']} --fw {config['fw_version']} --stage1 stage1/{config['fw_version']}.bin --stage2 stage2/{config['fw_version']}.bin"
        if "timeout" in config:
            cmd += f" --timeout {config['timeout']}"
        if "wait_after_pin" in config:
            cmd += f" --wait-after-pin {config['wait_after_pin']}"
        if "groom_delay" in config:
            cmd += f" --groom-delay {config['groom_delay']}"
        if "buffer_size" in config:
            cmd += f" --buffer-size {config['buffer_size']}"
        if "auto_retry" in config and config["auto_retry"]:
            cmd += f" --auto-retry"
        if "no_wait_padi" in config and config["no_wait_padi"]:
            cmd += f" --no-wait-padi"
        if "real_sleep" in config and config["real_sleep"]:
            cmd += f" --real-sleep {config['real_sleep']}"
        if "old_ipv6" in config and config["old_ipv6"]:
            cmd += f" --old-ipv6 {config['old_ipv6']}"
        os.system(cmd)
    else:
        warnings.warn("interface or fw_version not configured")


def inject_payloads_auto():
    config = utils.get_config()
    for plugin in config["plugins_load_boot"]:
        if plugin in global_var.payload_list[config["fw_version"]]["General"]:
            utils.load_payload(
                global_var.payload_list[config["fw_version"]]["General"][plugin]
            )


def install_trainer():
    ftp = ftplib.FTP()
    ftp.connect("192.168.1.2", 2121)
    ftp.login()

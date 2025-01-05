from multiprocessing import Process

from lang.zh_CN import zh_CN
from lang.en_US import en_US

tasks_save: dict[str, (Process | None)] = {
    "pppoe": None,
    "pppwn": None,
}

payload_list: dict[int, dict[str, dict[str, str]]] = {
    900: {
        "General": {
            "App2USB": "payloads/900/app2usb.bin",
            "AppDumper": "payloads/900/app-dumper.bin",
            "PkgBackup": "payloads/900/pkg-backup.bin",
            "BackupDB": "payloads/900/backupdb.bin",
            "RestoreDB": "payloads/900/restoredb.bin",
            "DisableASLR": "payloads/900/disableaslr.bin",
            "EnableUpdates": "payloads/900/enableupdates.bin",
            "DisableUpdates": "payloads/900/disableupdates.bin",
            "EnableBrowser": "payloads/900/enablebrowser.bin",
            "EnableToDex": "payloads/900/todex-enable.bin",
            "DisableToDex": "payloads/900/todex-disable.bin",
            "ExitIDU": "payloads/900/exitidu.bin",
            "FTPServer": "payloads/900/ftp.bin",
            "HistoryBlocker": "payloads/900/historyblocker.bin",
            "KernelDumper": "payloads/900/kerneldumper.bin",
            "ModuleDumper": "payloads/900/mdumper.bin",
            "OrbisToolBox": "payloads/900/Orbis-Toolbox-900.bin",
            "PermanentUART": "payloads/900/permanentuart.bin",
            "PS4Debug": "payloads/900/ps4debug.bin",
            "WebRTE": "payloads/900/WebRTE.bin",
            "RifRenamer": "payloads/900/rifrenamer.bin",
            "DumperG": "payloads/900/DumperG.bin",
            "DumperU": "payloads/900/DumperU.bin",
            "DumperMGU": "payloads/900/DumperMGU.bin",
            "DumperSGU": "payloads/900/DumperSGU.bin",
        },
        "FanController": {
            "Default": "payloads/900/fanDefault.bin",
            "50%": "payloads/900/fan50.bin",
            "55%": "payloads/900/fan55.bin",
            "60%": "payloads/900/fan60.bin",
            "65%": "payloads/900/fan65.bin",
            "70%": "payloads/900/fan70.bin",
            "75%": "payloads/900/fan75.bin",
            "80%": "payloads/900/fan80.bin",
        },
        "LinuxLoader": {
            "PS-1G": "payloads/900/LinuxLoader-900-1gb.bin",
            "PS-2G": "payloads/900/LinuxLoader-900-2gb.bin",
            "PS-3G": "payloads/900/LinuxLoader-900-3gb.bin",
            "PS-4G": "payloads/900/LinuxLoader-900-4gb.bin",
            "PSPro-1G": "payloads/900/LinuxLoaderPro-900-1gb.bin",
            "PSPro-2G": "payloads/900/LinuxLoaderPro-900-2gb.bin",
            "PSPro-3G": "payloads/900/LinuxLoaderPro-900-3gb.bin",
            "PSPro-4G": "payloads/900/LinuxLoaderPro-900-4gb.bin",
        },
    },
    1100: {
        "General": {
            "App2USB": "payloads/1100/app2usb.bin",
            "AppDumper": "payloads/1100/appdumper.bin",
            "Backup": "payloads/1100/backup.bin",
            "Restore": "payloads/1100/restore.bin",
            "DisableASLR": "payloads/1100/disableaslr.bin",
            "EnableUpdates": "payloads/1100/enableupdates.bin",
            "DisableUpdates": "payloads/1100/disableupdates.bin",
            "EnableBrowser": "payloads/1100/enablebrowser.bin",
            "ToDex": "payloads/1100/todex.bin",
            "ExitIDU": "payloads/1100/exitidu.bin",
            "FTPServer": "payloads/1100/ftp.bin",
            "HistoryBlocker": "payloads/1100/historyblocker.bin",
            "KernelDumper": "payloads/1100/kerneldumper.bin",
            "ModuleDumper": "payloads/1100/moduledumper.bin",
            "PermanentUART": "payloads/1100/permanentuart.bin",
            "PS4Debug": "payloads/1100/ps4debug.bin",
            "WebRTE": "payloads/1100/WebRTE.bin",
            "RifRenamer": "payloads/1100/rifrenamer.bin",
        },
        "LinuxLoader": {
            "PS-1G": "payloads/1100/LinuxLoader-1100-1gb.bin",
            "PS-2G": "payloads/1100/LinuxLoader-1100-2gb.bin",
            "PS-3G": "payloads/1100/LinuxLoader-1100-3gb.bin",
            "PS-4G": "payloads/1100/LinuxLoader-1100-4gb.bin",
            "PSPro-1G": "payloads/1100/LinuxLoaderPro-1100-1gb.bin",
            "PSPro-2G": "payloads/1100/LinuxLoaderPro-1100-2gb.bin",
            "PSPro-3G": "payloads/1100/LinuxLoaderPro-1100-3gb.bin",
            "PSPro-4G": "payloads/1100/LinuxLoaderPro-1100-4gb.bin",
        },
    },
}

fw_versions = {
    900: "9.00",
    960: "9.60",
    1000: "10.00",
    1001: "10.01",
    1050: "10.50",
    1070: "10.70",
    1071: "10.71",
    1100: "11.00",
}

lang_dict = {
    "zh_CN": zh_CN,
    "en_US": en_US,
}

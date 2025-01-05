import lang.Base


class en_US(lang.Base.LangBase):
    LANG = "English(US)"
    BUTTON_START_PPPWN = "Start PPPwn"
    BUTTON_SETTINGS = "Settings"
    BUTTON_LOAD_CHEATS = "Load Cheats"
    BUTTON_PAYLOADS = "Payloads"
    BUTTON_SAVE = "Save"
    BUTTON_CANCEL = "Cancel"
    BUTTON_CLOSE = "Close"
    SETTING_LANGUAGE = "Language"
    SETTING_INTERFACE = "Interface"
    SETTING_FW_VERSION = "Fimware Version"
    SETTING_TIMEOUT = "Timeout"
    SETTING_WAIT_AFTER_PIN = "Wait After Pin"
    SETTING_GROOM_DELAY = "Groom Delay"
    SETTING_BUFFER_SIZE = "Buffer Size"
    SETTING_START_ON_BOOT = "Start on Boot"
    SETTING_AUTO_RETRY = "Auto Retry"
    SETTING_NO_WAIT_PADI = "Don't wait for PADI"
    SETTING_REAL_SLEEP = "Real Sleep"
    SETTING_OLD_IPV6 = "IPv6"
    TEXT_WAIT_BACKEND = "Waiting for backend..."
    TEXT_TITLE_HOME = "PPPwn Suite for PS4"
    TEXT_TITLE_PAYLOAD = "PPPwn Suite for PS4 - Payloads"
    ALERT_PPPWN_STARTING = "PPPwn is starting...\nBefore it finished WebUI will be temporarily unavailable."
    ALERT_INSTALL_CHEAT_STARTING = "Installing Cheats..."
    ALERT_NO_BIN_SERVER = (
        "BinLoader server is disabled...\nPlease enable it in system settings."
    )
    ALERT_NO_FTP_SERVER = (
        "FTP server is disabled...\nPlease enable it in system settings."
    )
    ALERT_BIN_SERVER_BUSY = (
        "BinLoader server is busy and can't load the payload.\nPlease try again later."
    )
    ALERT_SEND_PAYLOAD_FINISHED = "Payload load finished."
    ALERT_SEND_PAYLOAD_FAILED = "Payload load failed."
    ALERT_SAVED = "Saved."

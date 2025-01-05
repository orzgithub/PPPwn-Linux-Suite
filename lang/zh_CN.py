import lang.Base


class zh_CN(lang.Base.LangBase):
    LANG = "简体中文"
    BUTTON_START_PPPWN = "启动PPPwn"
    BUTTON_SETTINGS = "设置"
    BUTTON_LOAD_CHEATS = "安装金手指"
    BUTTON_PAYLOADS = "加载项"
    BUTTON_SAVE = "保存"
    BUTTON_CANCEL = "取消"
    BUTTON_CLOSE = "关闭"
    SETTING_LANGUAGE = "语言"
    SETTING_INTERFACE = "接口"
    SETTING_FW_VERSION = "固件版本"
    SETTING_TIMEOUT = "超时"
    SETTING_WAIT_AFTER_PIN = "在CPU固定后等待"
    SETTING_GROOM_DELAY = "Groom延迟"  # 有更好的翻译吗？
    SETTING_BUFFER_SIZE = "缓冲区大小"
    SETTING_START_ON_BOOT = "开机自动PPPwn"
    SETTING_AUTO_RETRY = "失败后自动重试"
    SETTING_NO_WAIT_PADI = "不等待PS4的PADI"
    SETTING_REAL_SLEEP = "真实Sleep"
    SETTING_OLD_IPV6 = "使用IPv6"
    TEXT_WAIT_BACKEND = "等待后端响应…"  # 事实上如果后端不响应，你多半也看不到页面？
    TEXT_TITLE_HOME = "PS4 PPPwn套件"
    TEXT_TITLE_PAYLOAD = "PS4 PPPwn套件 - 加载项"
    ALERT_PPPWN_STARTING = "PPPwn启动中…\n在它完成前WebUI将会暂时不可用。"
    ALERT_NO_BIN_SERVER = "BinLoader服务器未启用…\n请在系统设置中启用它。"
    ALERT_NO_FTP_SERVER = "FTP服务器未启用…\n请在系统设置中启用它。"
    ALERT_BIN_SERVER_BUSY = "BinLoader服务器正忙，无法载入加载项.\n请稍后再试。"
    ALERT_SEND_PAYLOAD_FINISHED = "加载项载入成功。"
    ALERT_SEND_PAYLOAD_FAILED = "加载项载入失败。"
    ALERT_SAVED = "已保存。"

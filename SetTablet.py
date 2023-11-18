from ctypes import windll
from pystray import Icon, MenuItem as item
from PIL import Image
from winreg import OpenKeyEx, SetValueEx, QueryValueEx, REG_DWORD, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS
from win11toast import toast as win11_toast
from threading import Thread
from time import sleep
from sys import exit
global monitor_thread

def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    class TabletManager:
        def __init__(self):
            self.expected_value = 0
            self.icon = self.create_tray_icon()

        def create_tray_icon(self):
            image = Image.open(r"C:\Program Files\SetTablet\SetTablet.png")
            menu = (item('平板模式', self.on_activate), item('非平板模式', self.on_activate), item('退出', self.exit_program))
            return Icon("name", image, "title", menu)

        def get_tablet_mode(self):
            key = OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", 0, KEY_ALL_ACCESS)
            value, _ = QueryValueEx(key, "ConvertibleSlateMode")
            key.Close()
            return value

        def set_tablet_mode(self, mode):
            old_value = self.get_tablet_mode()
            key = OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\PriorityControl", 0, KEY_ALL_ACCESS)
            SetValueEx(key, "ConvertibleSlateMode", 0, REG_DWORD, self.expected_value)
            key.Close()

            new_value = self.get_tablet_mode()
            if old_value != new_value:
                notification_text = f"ConvertibleSlateMode 已更改: {old_value} -> {new_value}"
                if mode:
                    win11_toast("SetTablet", notification_text, icon=r"C:\Program Files\SetTablet\SetTablet.ico")

        def on_activate(self, icon, item):
            if item.text == '平板模式':
                self.expected_value = 0
                self.set_tablet_mode(True)
            elif item.text == '非平板模式':
                self.expected_value = 1
                self.set_tablet_mode(True)
            elif item.text == '退出':
                self.exit_program()

        def exit_program(self):
            self.stop_threads=False

        def monitor_tablet_mode(self):
            while self.stop_threads:
                print("当前设置：", self.expected_value)
                print("当前值：", self.get_tablet_mode())
                current_value = self.get_tablet_mode()
                if current_value != self.expected_value:
                    print(f"检测到外部程序更改。正在恢复为 {self.expected_value}")
                    self.set_tablet_mode(False)
                sleep(5)
            self.icon.stop()
            exit(0)

    def main():
        tablet_manager = TabletManager()
        tablet_manager.stop_threads=True
        monitor_thread = Thread(target=tablet_manager.monitor_tablet_mode, daemon=True)
        monitor_thread.start()
        tablet_manager.icon.run()

    if __name__ == "__main__":
        main()
else:
    windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(['"--noconsole"', '"' + sys.argv[0] + '"'] + sys.argv[1:]), None, 1)
    exit("非管理员")

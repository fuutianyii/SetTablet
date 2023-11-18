# SetTablet

**描述:** SetTablet 是一个用于管理 Windows 11 平板模式的 Python 脚本。平板模式是一种优化触摸设备用户界面的功能。该脚本允许您通过系统托盘图标轻松切换平板模式和非平板模式，为您的设备提供方便的配置方式。

**特点:**

- 在平板模式和非平板模式之间切换。
- 提供系统托盘图标以便快速访问。
- 监视平板模式的外部更改并恢复所需的模式。

**要求:**

- Python 3.x
- 库：`ctypes`、`pystray`、`PIL`、`winreg`、`win11toast`、`threading`、`time`、`sys`
- 将脚本及相关文件移动至 `C:\Program Files\SetTablet` 目录下

## 安装

1. 将脚本及相关文件移动至 `C:\Program Files\SetTablet` 目录下。

2. 确保系统上安装了 Python。

3. 使用以下命令安装所需的库：

   ```
   bashCopy code
   pip install pystray Pillow win11toast
   ```

## 用法

1. 以管理员身份运行脚本，以确保具有必要的权限。

   ```
   bashCopy code
   python "C:\Program Files\SetTablet\SetTablet.py"
   ```

2. 脚本将创建一个系统托盘图标，提供设置平板模式、非平板模式或退出程序的选项。

**注意:**

- 该脚本持续监视平板模式，并在检测到外部更改时将其调整为所需设置。

**文件结构:**

- `C:\Program Files\SetTablet\SetTablet.py`: 主要脚本。
- `C:\Program Files\SetTablet\SetTablet.png`: 用于系统托盘的图标。
- `C:\Program Files\SetTablet\SetTablet.ico`: 通知图标。

**免责声明:** 该脚本按原样提供，不附带任何保修或担保。请自行承担风险使用，并注意修改系统设置可能会产生意外后果。

**作者:** fuutianyii
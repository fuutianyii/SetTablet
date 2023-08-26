'''
Author: fuutianyii
Date: 2023-08-26 20:58:43
LastEditors: fuutianyii
LastEditTime: 2023-08-26 21:01:17
github: https://github.com/fuutianyii
mail: fuutianyii@gmail.com
QQ: 1587873181
'''
# 本程序仅仅适配win11
#将次目录移动到C:\Program Files\并命名为SetTablet即可
from winreg import OpenKeyEx,SetValueEx,QueryValueEx,REG_DWORD,HKEY_LOCAL_MACHINE,KEY_ALL_ACCESS
from win11toast import toast

key=OpenKeyEx(HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\PriorityControl",0,KEY_ALL_ACCESS)
SetValueEx(key,"ConvertibleSlateMode",0,REG_DWORD,0x0)
value=QueryValueEx(key,"ConvertibleSlateMode")
if value[0]== 0:
    toast("SetTablet","已设置为平板模式",icon=r"C:\Program Files\SetTablet\SetTablet.ico")
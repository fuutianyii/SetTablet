# encoding:utf-8
from winreg import OpenKeyEx,SetValueEx,QueryValueEx,REG_DWORD,HKEY_LOCAL_MACHINE,KEY_ALL_ACCESS
from win11toast import toast

key=OpenKeyEx(HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\PriorityControl",0,KEY_ALL_ACCESS)
SetValueEx(key,"ConvertibleSlateMode",0,REG_DWORD,0x0)
value=QueryValueEx(key,"ConvertibleSlateMode")
if value[0]== 0:
    toast("SetTablet","已设置为平板模式",icon=r"C:\Program Files\SetTablet\SetTablet.ico")

 


# -*- coding: utf-8 -*-
#http://www.cyberforum.ru/python/thread1953161.html

import winreg

# откроем раздел
key_reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "foo")

# откроем получим даные о первом и единственном параметре в этом ключе
t = winreg.EnumValue(key_reg, 0)

# ну и выведем эти даные, сперва имя
print(t[0])

# и значение, кстати, t [1] имеет тип str
print(t[1])


if __name__ == "__main__":
    pass

#!/usr/bin/python3
# ДАННЫЙ ПРИМЕР ВЫВОДИТ НАПРАВЛЕНИЯ ДЖОЙСТИКА В ГРАДУСАХ:

from time import sleep
from math import atan2, pi

# Подключаем библиотеку для работы с джойстиком I2C-flash.
from pyiArduinoI2Cjoystick import *

# Объявляем объект joy для работы с библиотекой, указывая адрес модуля на шине.
j = pyiArduinoI2Cjoystick(0x09)

# Сохраняем текущую калибровку джойстика
xa, xb, xc = j.getCalibration_X()
ya, yb, yc = j.getCalibration_Y()

# Меняем направления осей
j.setCalibration_X(4095, 2048, 0)
j.setCalibration_Y(4095, 2048, 0)

try:

    print("Выводим положение джойстика в полярной системе координат.")
    print("Для выхода нажмите <ctrl+c>")

    while True:

        # Получаем текущие координаты
        x, y = j.x, j.y

        # Вычисляем радианы
        rad = atan2(y,x)
        deg = rad * (180 / pi)

        if deg < 0:
            deg = deg + 360

        # Выводим градусы
        print(round(deg))

        sleep(.1)
except:

    # Возвращаем калибровку джойстика в исходную
    j.setCalibration_X(xa, xb, xc)
    j.setCalibration_Y(ya, yb, yc)

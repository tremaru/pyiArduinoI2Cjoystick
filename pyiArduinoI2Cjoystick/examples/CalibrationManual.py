#!/usr/bin/python3
# ПРИМЕР РУЧНОЙ КАЛИБРОВКИ КООРДИНАТ ДЖОЙСТИКА:
"""
    Примечание:
    Значения АЦП у разных джойстиков могут отличаться
    Точные показания АЦП для каждого положения Вашего
    джойстика Вы можете узнать из примера «GetADC».

"""
from curses import wrapper
from time import sleep

#   Подключаем библиотеку для работы с джойстиком I2C-flash.
from pyiArduinoI2Cjoystick import *

# Объявляем объект для работы с библиотекой, указывая адрес модуля на шине I2C.
j = pyiArduinoI2Cjoystick(0x09)

#   Если объявить объект без указания адреса,
# то адрес будет найден автоматически.
#j = pyiArduinoI2Cjoystick()

#  Калибровка осей указанием значений АЦП:
#   Калибруем ось X указывая АЦП крайнего левого  положения (0),
# АЦП центра (2047), АЦП крайнего правого  положения (4095).
j.setCalibration_X(0, 2047, 4095)

#   Калибруем ось Y указывая АЦП крайнего нижнего положения (0),
# АЦП центра (2047), АЦП крайнего верхнего положения (4095).
j.setCalibration_Y(0, 2047, 4095)

#   Если направление оси требуется изменить,
# то поменяйте местами крайние значения АЦП оси (0 <-> 4095).

def main(stdscr):
    stdscr.clear()
    print("Текущие координаты: (нажмите <ctrl+c> для выхода)", end="\r\n")
    print( "X:Y=" + str(j.x) + ":" + str(j.y), end="\r\n")

    sleep(.1)
    stdscr.refresh()


while True:
    wrapper(main)
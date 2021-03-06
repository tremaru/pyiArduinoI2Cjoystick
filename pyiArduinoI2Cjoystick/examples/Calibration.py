#!/usr/bin/python3
# ДАННЫЙ ПРИМЕР ВЫПОЛНЯЕТ КАЛИБРОВКУ ДЖОЙСТИКА:

from curses import wrapper
from time import time, sleep

# Подключаем библиотеку для работы с джойстиком I2C-flash.
from pyiArduinoI2Cjoystick import *

# Объявляем объект joy для работы с библиотекой, указывая адрес модуля на шине I2C.
j = pyiArduinoI2Cjoystick(0x09)

#   Если объявить объект без указания адреса, то адрес будет найден автоматически.
# j = pyiArduinoI2Cjoystick()


def nillis():
    return int(round(time() * 1000))

start = nillis()

def millis():
    return nillis() - start

x=0
adc_X_min=4096
adc_X_cen=0
adc_X_max=0

y=0
adc_Y_min=4096
adc_Y_cen=0
adc_Y_max=0

# Устанавливаем незначительное усреднение показаний АЦП.
j.setAveraging(2)

# Устанавливаем мёртвую зону центрального положения в 7%.
j.setDeadZone(7.0)

# Готовимся определить центральное положение джойстика:                         #
print()
print("КАЛИБРОВКА ДЖОЙСТИКА:")
print("Отпустите джойстик.")
print( "Он должен самостоятельно установиться в центральное положение.")

print("Ждём.", end='')

# Даём время пользователю отпустить джойстик.
for i in range(5):

    sleep(1)
    print(".", end='')

# Получаем значения АЦП соответствующие центральному положению:

# Выполняем цикл чтения 10 раз.
for i in range(10):

    x, y = j.getADC()
    print()

    # Получаем текущие значения АЦП в указанные переменные.
    print("АЦП = " + str(x) + ":" + str(y))

    # Получаем АЦП центра, прибавляя его к предыдущему значению.
    adc_X_cen += x
    adc_Y_cen += y

    sleep(.2)

# Получаем среднее арифметическое значение АЦП центра.

adc_X_cen /= 10
adc_Y_cen /= 10

# Готовимся определить крайние положения джойстика:

print("\r\nГотово!")
print("------------------------------------------------")
print("")
print("Теперь медленно поворачивайте джойстик по кругу,")
print("со скоростью 1 полный оборот за 2-3 секунды,")
print("на максимальном удалении джойстика от центра.", end='')

# Получаем значения АЦП соответствующие крайним положениям:

# Определяем время завершения снятия показаний.
tmrStop = millis() + 10000

# Выполняем цикл пока не достигнем времени tmrStop...
while millis() < tmrStop:

    # Получаем текущие значения АЦП в указанные переменные.
    x, y = j.getADC()

    # Получаем минимальные значение АЦП
    if x < adc_X_min: adc_X_min = x
    if y < adc_Y_min: adc_Y_min = y

    # Получаем максимальные значение АЦП по оси X.
    if x > adc_X_max: adc_X_max = x
    if y > adc_Y_max: adc_Y_max = y

    # Выводим точку в stdout, один раз в секунду.
    if millis() % 1000 < 10: sleep(.01),  print(".", end='')

# Выводим результат:

print("\r\nГотово!")
print("------------------------------------------------")
print( "")

print(
        "АЦП по оси X меняется от " + str(adc_X_min)
        + " до " + str(adc_X_max) + ", с центром в "
        + str(int(round(adc_X_cen)))
     )
print(
        "АЦП по оси Y меняется от " + str(adc_Y_min)
        + " до " + str(adc_Y_max) + ", с центром в "
        + str(int(round(adc_Y_cen)))
     )

print( "================================================")


# Калибруем джойстик (данные сохранятся в его flash памяти):

# Калибруем координаты по оси X.

j.setCalibration_X(adc_X_min, adc_X_cen, adc_X_max)

# Калибруем координаты по оси Y.
j.setCalibration_Y(adc_Y_min, adc_Y_cen, adc_Y_max)


# Готовимся к выводу координат после калибровки:

print("Приготовтесь проверить результат калибровки.")
print("Сейчас будут выводиться координаты джойстика...")
print("Ждём.", end = '')

# Даём время пользователю прочитать результат, до начала вывода координат.
for i in range(5):
    sleep(1)
    print(".", end='')

print("\r\nВыводим координаты:")


# Выводим координаты:
def output(stdscr):
    stdscr.clear()

    print("Нажмите <ctrl+c> для выхода", end="\r\n")
    x, y = j.getPosition()

    # Выводим координаты X:Y.
    print("X:Y="+str(x)+":"+str(y)+" ", end='' )
    x, y = j.getADC()

    # Выводим значения АЦП.
    print("(АЦП="+str(x)+":"+str(y)+")." )

    print()

    sleep(.1)

    stdscr.refresh()


while True:
    wrapper(output)

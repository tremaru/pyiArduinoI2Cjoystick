// ПРИМЕР РУЧНОЙ КАЛИБРОВКИ КООРДИНАТ ДЖОЙСТИКА:  //
 /*  Примечание:
 *  Значения АЦП у разных джойстиков могут отличаться
 *  Точные показания АЦП для каждого положения Вашего
 *  джойстика Вы можете узнать из примера «GetADC».
 */
                                                 //
#include <iostream>
#include <ncurses.h>
#define print std::cout<<
#include "../iarduino_I2C_Joystick.h"             //   Подключаем библиотеку для работы с джойстиком I2C-flash.
iarduino_I2C_Joystick joy(0x09);                  //   Объявляем объект joy для работы с функциями и методами библиотеки iarduino_I2C_Joystick, указывая адрес модуля на шине I2C.
                                                  //   Если объявить объект без указания адреса (iarduino_I2C_Joystick joy;), то адрес будет найден автоматически.
void setup(){                                     //
    joy.begin();                                  //   Инициируем работу с джойстиком.
//  Калибровка осей указанием значений АЦП:       //
    joy.setCalibration_X(0, 2047, 4095);          //   Калибруем ось X указывая АЦП крайнего левого  положения (0), АЦП центра (2047), АЦП крайнего правого  положения (4095).
    joy.setCalibration_Y(0, 2047, 4095);          //   Калибруем ось Y указывая АЦП крайнего нижнего положения (0), АЦП центра (2047), АЦП крайнего верхнего положения (4095).
}                                                 //   Если направление оси требуется изменить, то поменяйте местами крайние значения АЦП оси (0 <-> 4095).
                                                  //

int main()
{
        setup();
        std::cout << "Нажмите <ctrl+c> для выхода." << '\n' << std::flush;
        std::cout << "Положение джойстика:" << '\n' << std::flush;
        std::cout << 'X' << '\t' << 'Y' << '\n' << std::flush;
        for(;;) {
                int x = joy.getPosition_X();
                int y = joy.getPosition_Y();
                clrtoeol();
                std::cout << "                                              " << '\r' << std::flush;

                std::cout << x << '\t' << y << '\r' << std::flush;
                delay(1);
        }
}

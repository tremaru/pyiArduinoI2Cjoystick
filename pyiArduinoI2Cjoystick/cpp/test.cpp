#include "../iarduino_I2C_Joystick.h"
#include <iostream>

int main() {

	unsigned long then = millis();

	for (;;) {
		unsigned long now = millis() - then;
		std::cout << now << '\r';
	}
}

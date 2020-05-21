EDEPS=../iarduino_I2C_Joystick.cpp Includes/WString.cpp Includes/dtostrf.cpp Includes/itoa.cpp
LDFLAGS=-lncurses
all: FindDevices NewAddress Calibration CalibrationManual

FindDevices             :FindDevices.cpp ../iarduino_I2C_Joystick.cpp
NewAddress              :NewAddress.cpp ../iarduino_I2C_Joystick.cpp
Calibration             :Calibration.cpp $(EDEPS) $(LDFLAGS)
CalibrationManual       :CalibrationManual.cpp $(EDEPS) $(LDFLAGS)

clean:
	rm -f FindDevices NewAddress Calibration CalibrationManual

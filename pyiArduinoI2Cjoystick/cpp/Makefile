EDEPS=../iarduino_I2C_Joystick.cpp Includes/WString.cpp Includes/dtostrf.cpp Includes/itoa.cpp
LDFLAGS=-lncurses
all: FindDevices NewAddress Calibration CalibrationManual ChangeAxisDir GetADC GetDirection GetPosition

FindDevices             :FindDevices.cpp ../iarduino_I2C_Joystick.cpp
NewAddress              :NewAddress.cpp ../iarduino_I2C_Joystick.cpp
Calibration             :Calibration.cpp $(EDEPS) $(LDFLAGS)
CalibrationManual       :CalibrationManual.cpp $(EDEPS) $(LDFLAGS)
ChangeAxisDir           :ChangeAxisDir.cpp ../iarduino_I2C_Joystick.cpp
GetADC                  :GetADC.cpp ../iarduino_I2C_Joystick.cpp
GetDirection            :GetDirection ../iarduino_I2C_Joystick.cpp
GetPosition             :GetPosition.cpp ../iarduino_I2C_Joystick.cpp

clean:
	rm -f FindDevices NewAddress Calibration CalibrationManual ChangeAxisDir GetADC GetDirection GetPosition

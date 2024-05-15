
from time import sleep
from roboclaw_3 import Roboclaw


""" Constants related to Roboclaw"""
	
MOTOR_DRIVER_PORT = '/dev/ttyACM0'
MOTOR_DRIVER_BAUDRATE = 38400

SPEED = 1000
DISTANCE = 4000


FRONT_MOTORS_DRIVER = 0x80
# BACK_MOTORS_DRIVER = 0x81
FR_BR_WHEEL_ENCODER = 'M1'
FL_BL_WHEEL_ENCODER = 'M2'


md = Roboclaw(MOTOR_DRIVER_PORT, MOTOR_DRIVER_BAUDRATE)
md.Open()

# print("running SpeedM1, M2 +- Front Motors")
# md.SpeedM1(FRONT_MOTORS_DRIVER, SPEED)
# sleep(2)
# md.SpeedM1(FRONT_MOTORS_DRIVER, -SPEED)
# sleep(2)
# md.SpeedM1(FRONT_MOTORS_DRIVER, 0)

# md.SpeedM2(FRONT_MOTORS_DRIVER, SPEED)
# sleep(2)
# md.SpeedM2(FRONT_MOTORS_DRIVER, -SPEED)
# sleep(2)
# md.SpeedM2(FRONT_MOTORS_DRIVER, 0)

# print("running SpeedM1, M2 +- Back Motors")
# md.SpeedM1(BACK_MOTORS_DRIVER, SPEED)
# sleep(2)
# md.SpeedM1(BACK_MOTORS_DRIVER, -SPEED)
# sleep(2)
# md.SpeedM1(BACK_MOTORS_DRIVER, 0)

# md.SpeedM2(BACK_MOTORS_DRIVER, SPEED)
# sleep(2)
# md.SpeedM2(BACK_MOTORS_DRIVER, -SPEED)
# sleep(2)
# md.SpeedM2(BACK_MOTORS_DRIVER, 0)

# print("running all Motors together +-")
# print("forward")
# md.SpeedM1(FRONT_MOTORS_DRIVER, SPEED)
# md.SpeedM2(FRONT_MOTORS_DRIVER, SPEED)
# md.SpeedM1(BACK_MOTORS_DRIVER, SPEED)
# md.SpeedM2(BACK_MOTORS_DRIVER, SPEED)

# sleep(2)

# print("Backward")
# md.SpeedM1(FRONT_MOTORS_DRIVER, -SPEED)
# md.SpeedM2(FRONT_MOTORS_DRIVER, -SPEED)
# md.SpeedM1(BACK_MOTORS_DRIVER, -SPEED)
# md.SpeedM2(BACK_MOTORS_DRIVER, -SPEED)

# sleep(5)

# md.SpeedM1(FRONT_MOTORS_DRIVER, 0)
# md.SpeedM2(FRONT_MOTORS_DRIVER, 0)
# md.SpeedM1(BACK_MOTORS_DRIVER, 0)
# md.SpeedM2(BACK_MOTORS_DRIVER, 0)

# print("running SpeedDistance on all wheels")

# md.SpeedDistanceM1(FRONT_MOTORS_DRIVER, SPEED, DISTANCE, 1)
# md.SpeedDistanceM2(FRONT_MOTORS_DRIVER, SPEED, DISTANCE, 0)
# md.SpeedDistanceM1(BACK_MOTORS_DRIVER, SPEED, DISTANCE, 0)
# md.SpeedDistanceM2(BACK_MOTORS_DRIVER, SPEED, DISTANCE, 0)

# sleep(2)

# md.SpeedDistanceM1(FRONT_MOTORS_DRIVER, -SPEED, DISTANCE, 0)
# md.SpeedDistanceM2(FRONT_MOTORS_DRIVER, -SPEED, DISTANCE, 0)
# md.SpeedDistanceM1(BACK_MOTORS_DRIVER, -SPEED, DISTANCE, 0)
# md.SpeedDistanceM2(BACK_MOTORS_DRIVER, -SPEED, DISTANCE, 0)

# sleep(5)

# # final stop incase stuff fails
# md.SpeedM1(FRONT_MOTORS_DRIVER, 0)
# md.SpeedM2(FRONT_MOTORS_DRIVER, 0)
# md.SpeedM1(BACK_MOTORS_DRIVER, 0)
# md.SpeedM2(BACK_MOTORS_DRIVER, 0)
# sleep(5)
# md.ReadCurrents(0x80)
# print(md.ReadEncM1(0x80))
# print(md.ReadCurrents(0x80))
# print(md.ReadEncoderModes(0x80))
# print(md.ReadMainBatteryVoltage(0x80))
print(md.DutyM1(10001))


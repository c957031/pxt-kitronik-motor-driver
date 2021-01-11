Lys = 0

def on_button_pressed_a():
    global Lys
    while True:
        Lys = pins.analog_read_pin(AnalogPin.P1)
        if Lys > 500:
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                kitronik_motor_driver.MotorDirection.FORWARD,
                30)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                kitronik_motor_driver.MotorDirection.FORWARD,
                30)
        else:
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                kitronik_motor_driver.MotorDirection.REVERSE,
                40)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                kitronik_motor_driver.MotorDirection.REVERSE,
                40)
            basic.pause(1000)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                kitronik_motor_driver.MotorDirection.FORWARD,
                80)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                kitronik_motor_driver.MotorDirection.REVERSE,
                80)
            basic.pause(randint(450, 1450))
        basic.pause(10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Lys
    Lys = pins.analog_read_pin(AnalogPin.P1)
    basic.show_number(Lys)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
        kitronik_motor_driver.MotorDirection.FORWARD,
        80)
    kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
        kitronik_motor_driver.MotorDirection.REVERSE,
        80)
    basic.pause(1350)
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
input.on_button_pressed(Button.B, on_button_pressed_b)

let Lys = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    while (true) {
        Lys = pins.analogReadPin(AnalogPin.P1)
        if (Lys > 500) {
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 30)
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Forward, 30)
        } else {
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Reverse, 40)
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Reverse, 40)
            basic.pause(1000)
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 80)
            kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Reverse, 80)
            basic.pause(randint(450, 1450))
        }
        
        basic.pause(10)
    }
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Lys = pins.analogReadPin(AnalogPin.P1)
    basic.showNumber(Lys)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 80)
    kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Reverse, 80)
    basic.pause(1350)
    kitronik_motor_driver.motorOff(kitronik_motor_driver.Motors.Motor1)
    kitronik_motor_driver.motorOff(kitronik_motor_driver.Motors.Motor2)
})

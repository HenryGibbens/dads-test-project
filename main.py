def turnServo():
    global p2max
    p2max = 180
    index = 0
    while index <= p2max:
        bitbot.bb_set_servo(BBServos.P2, index)
        basic.pause(100)
        index += 1
    index2 = 0
    while index2 <= p2max:
        bitbot.bb_set_servo(BBServos.P2, p2max - index2)
        basic.pause(100)
        index2 += 1
def readDistance():
    global distance
    basic.pause(2000)
    distance = bitbot.sonar(BBPingUnit.CENTIMETERS)
    serial.write_value("distance", distance)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def moveTalon():
    bitbot.set_talon(0)
    basic.pause(200)
    bitbot.set_talon(80)
    basic.pause(200)
    bitbot.set_talon(1)
    basic.pause(200)

def on_button_pressed_b():
    turnServo()
input.on_button_pressed(Button.B, on_button_pressed_b)

distance = 0
p2max = 0
bitbot.select_model(BBModel.XL)
bitbot.bb_set_servo(BBServos.P2, 0)

def on_forever():
    pass
basic.forever(on_forever)

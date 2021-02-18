function turnServo () {
    p2max = 180
    while (index <= p2max) {
        bitbot.bbSetServo(BBServos.P2, index)
        basic.pause(100)
        index += 1
    }
    while (index2 <= p2max) {
        bitbot.bbSetServo(BBServos.P2, p2max - index2)
        basic.pause(100)
        index2 += 1
    }
}
function readDistance () {
    basic.pause(2000)
    distance = bitbot.sonar(BBPingUnit.Centimeters)
    serial.writeValue("distance", distance)
}
input.onButtonPressed(Button.A, function () {
    moveTalon()
})
function moveTalon () {
    bitbot.setTalon(0)
    basic.pause(200)
    bitbot.setTalon(80)
    basic.pause(200)
    bitbot.setTalon(1)
    basic.pause(200)
}
input.onButtonPressed(Button.B, function () {
    turnServo()
})
let distance = 0
let index2 = 0
let index = 0
let p2max = 0
bitbot.select_model(BBModel.XL)
bitbot.bbSetServo(BBServos.P2, 0)
basic.forever(function () {
    readDistance()
})

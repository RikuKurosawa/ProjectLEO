import smbus2
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from sys import stdin
from smbus2 import SMBus, i2c_msg

def main():
    print("Imported Doing")
    sm = 6

    cs = ColorSensor()
    ts = TouchSensor()
    uss = UltrasonicSensor()
    spkr = Sound()

    leds = Leds()

    #print("Press the touch sensor to change the LED color!")

    with SMBus(sm) as bus:#かっこ内は、ポートに２をたす
        # Write a byte to address 80, offset 0
        bus.write_byte_data(0x01, 0x27, 0x002)
        bus.write_byte_data(0x01, 0x25, 0x00)

    mct = 0

    #while True:
        #print("sound")


    spkr.play_file('enter.wav',100,0)
    if mct != 1:
        with SMBus(sm) as bus:

            bus.write_i2c_block_data(0x01, 0x45, [100,100,-100,-100])#制御モード
        mct = 1

    time.sleep(2)
    while True:
        dis = uss.distance_centimeters_continuous
        cl = cs.color
        print(cl)
        if cl != 5:#0=None,1=Black,5=Red
            if dis >=50:
                spkr.play_file('railway2.wav',100,1)

                if mct != 1:
                    with SMBus(sm) as bus:

                        bus.write_i2c_block_data(0x01, 0x45, [100,100,-100,-100])#制御モード
                    mct = 1
            else:
                while True:
                    if mct != 2:
                        with SMBus(sm) as bus:
                            bus.write_i2c_block_data(0x01, 0x45, [00,00,00,00])
                        mct = 2
                    spkr.play_tone(800,1)
                    if ts.is_pressed:#復位
                        spkr.play_file('correct.wav',100,0)

                        break

        else:
            if mct != 2:
                with SMBus(sm) as bus:
                    bus.write_i2c_block_data(0x01, 0x45, [00,00,00,00])
                mct = 2
                break

    spkr.play_file('pori.wav',100,0)
    import config
    config.x=1

"""
while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
"""

"""
def main():
    with SMBus(6) as bus:#かっこ内は、ポートに２をたす
        # Write a byte to address 80, offset 0
        bus.write_byte_data(0x01, 0x27, 0x002)
        bus.write_byte_data(0x01, 0x25, 0x00)
    while True:

        with SMBus(6) as bus:#かっこ内は、ポートに２をたす
            # Write a byte to address 80, offset 0


            bus.write_i2c_block_data(0x01, 0x45, [-100,-100,100,100])#制御モード
            #bus.write_i2c_block_data(0x01, 0x45, [00,00,00,00])
"""


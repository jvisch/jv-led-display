import serial
import time
import math

with serial.Serial("COM4", baudrate=115200) as s:
    
    time.sleep(2)

    SLEEPY = .015
    
    BLACK = [0x00, 0x00, 0x00]
    RED = [0xFF, 0x00, 0x00]
    GREEN = [0x00, 0xFF, 0x00]
    BLEU = [0x00, 0x00, 0xFF]

    YELLOW = [0xFF, 0xFF, 0x00]
    PURPLE = [0x00, 0xFF, 0xFF]


    while True:
        line = RED + GREEN + BLEU + PURPLE + YELLOW
        line *= math.ceil( (256*3)/len(line) )
        line = line[:256*3]


        s.write(line)
        time.sleep(SLEEPY)
        
        # print("oeps")

        line = BLACK * 256
        s.write(line)
        time.sleep(SLEEPY)

        # print('done')

# with serial.Serial("COM4", baudrate=9600) as s:
    # while True:
    #     if s.in_waiting > 0:
    #         output = s.read_all()
    #         if output:
    #             print(output.decode(), end='')
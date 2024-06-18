import hal.hal_led as led
import time
from time import sleep
import hal.hal_input_switch as switch

led.init()
switch.init()
while(True):
    if switch.read_slide_switch()==1:
            led.set_output(24,5)
            time.sleep(0.2)
            led.set_output(24,0)
            time.sleep(0.2)
    elif switch.read_slide_switch()==0:
          led.set_output(24,5)
          time.sleep(0.1)
          led.set_output(24,0)
          time.sleep(0.1)
import i2c7segment as display
import time
import RPi.GPIO as io

switch_pin = 17
io.setmode(io.BCM)
io.setup(switch_pin, io.IN, pull_up_down=io.PUD_UP)
disp = display.Adafruit7Segment()

time_mode, seconds_mode, date_mode = range(3)
disp_mode = time_mode

def display_time():
    h = time.localtime().tm_hour
    m = time.localtime().tm_min
    disp.print_int(h * 100 + m)
    disp.draw_colon(True)
    disp.write_display()
    time.sleep(0.5)
    disp.draw_colon(False)
    disp.write_display()
    time.sleep(0.5)

def disply_date():
    d = time.localtime().tm_mday
    m = time.localtime().tm_mon
    #disp.print_int(d * 100 + m) # World format
    disp.print_int(m * 100 + d)  # US format
    disp.draw_colon(True)
    disp.write_display()
    time.sleep(0.5)

def display_seconds():
    s = time.localtime().tm_sec
    disp.print_str('----')
    disp.print_int(s)
    disp.draw_colon(True)
    disp.write_display()
    time.sleep(0.5)

while True:
    key_pressed = not io.input(switch_pin)
    if key_pressed:
        disp_mode = disp_mode + 1
        if disp_mode > date_mode:
            disp_mode = time_mode
    if disp_mode == time_mode:
        display_time()
    elif disp_mode == seconds_mode:
        display_seconds()
    elif disp_mode == date_mode:
        disply_date()
    

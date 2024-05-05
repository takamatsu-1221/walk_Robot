from machine import PWM,Pin
import time,utime

#Pin
#yellow
foot_right = PWM(Pin(0))
foot_left = PWM(Pin(1))
#green
body_right = PWM(Pin(2))
body_left = PWM(Pin(3))

#PWM signal
foot_right.freq(50)
foot_left.freq(50)
body_right.freq(50)
body_left.freq(50)

#initial degree
ini_foot_right = 90
ini_foot_left = 90
ini_body_right = 90
ini_body_left = 90

#adbance and back move
slope_twofoot = 63
slope_onefoot = 50
rotate_body = 20
delay = 0.006
delta_angle = 0.5
alfa_body = -4

#left and right move
rotate_body_side = 10
kick_angle = 40

#wait time
delay_move = 0.01
delay_action = 0.05
delay_move_side = 0.4
delay_action_side = 0.4

#move signal
do = 0

#Pin trigger
trig_reset = Pin(20, Pin.IN, Pin.PULL_DOWN)
trig_advance = Pin(19, Pin.IN, Pin.PULL_DOWN)
trig_back = Pin(18, Pin.IN, Pin.PULL_DOWN)
trig_left = Pin(17, Pin.IN, Pin.PULL_DOWN)
trig_right = Pin(16, Pin.IN, Pin.PULL_DOWN)

#Pin LED
led = Pin(25, Pin.OUT)


def main():
    led.value(1)
    reset()
    while True:
        if do==0:
            while True:
                reset()
                time.sleep(0.1)
                if do!=0:
                    break
        elif do==1:
            move_advance()
        elif do==2:
            move_back()
        elif do==3:
            move_left()
        elif do==4:
            move_right()
        print(do)
        time.sleep(0.3)
        
    
def reset():
    foot_right.duty_u16(servo_value(ini_foot_right))
    foot_left.duty_u16(servo_value(ini_foot_left))
    body_right.duty_u16(servo_value(ini_body_right))
    body_left.duty_u16(servo_value(ini_body_left))

def move_advance():
    #first action
    #foot
    servo_move(ini_foot_left, (ini_foot_left - slope_twofoot), delta_angle, delay, 1)
    servo_move(ini_foot_right, (ini_foot_right - slope_onefoot - 2), delta_angle, delay, 0)
    servo_move((ini_foot_left - slope_twofoot), ini_foot_right, delta_angle, delay, 1)
    time.sleep(delay_move)
    #body
    servo_move(ini_body_right, (ini_body_right + rotate_body + alfa_body), delta_angle, delay, 2)
    servo_move(ini_body_left, (ini_body_left + rotate_body), delta_angle, delay, 3)
    time.sleep(delay_move)
    #foot
    servo_move((ini_foot_right - slope_onefoot), ini_foot_left, delta_angle, delay, 0)
    time.sleep(delay_action)
    
    while True:
        if do!=1:
            break
        #second action
        #foot
        servo_move(ini_foot_right, (ini_foot_right + slope_twofoot), delta_angle, delay, 0)
        servo_move(ini_foot_left, (ini_foot_left + slope_onefoot), delta_angle, delay, 1)
        servo_move((ini_foot_right + slope_twofoot), ini_foot_right, delta_angle, delay, 0)
        time.sleep(delay_move)
        #body
        servo_move((ini_foot_left + rotate_body), (ini_body_left - rotate_body), delta_angle, delay, 3)
        servo_move((ini_foot_right + rotate_body + alfa_body), (ini_body_right - rotate_body - alfa_body), delta_angle, delay, 2)
        time.sleep(delay_move)
        #foot
        servo_move((ini_foot_left + slope_onefoot), ini_foot_left, delta_angle, delay, 1)
        time.sleep(delay_action)
        
        if do!=1:
            break
        #third action
        #foot
        servo_move(ini_foot_left, (ini_foot_left - slope_twofoot), delta_angle, delay, 1)
        servo_move(ini_foot_right, (ini_foot_right - slope_onefoot), delta_angle, delay, 0)
        servo_move((ini_foot_left - slope_twofoot), ini_foot_left, delta_angle, delay, 1)
        time.sleep(delay_move)
        #body
        servo_move((ini_foot_right - rotate_body - alfa_body), (ini_body_right + rotate_body + alfa_body), delta_angle, delay, 2)
        servo_move((ini_foot_left - rotate_body), (ini_body_left + rotate_body), delta_angle, delay, 3)
        time.sleep(delay_move)
        #foot
        servo_move((ini_foot_right - slope_onefoot), ini_foot_right, delta_angle, delay, 0)
        time.sleep(delay_action)
        
    reset()
    
        
def move_back():    
    #first action
    #foot
    servo_move(ini_foot_left, (ini_foot_left - slope_twofoot), delta_angle, delay, 1)
    servo_move(ini_foot_right, (ini_foot_right - slope_onefoot), delta_angle, delay, 0)
    servo_move((ini_foot_left - slope_twofoot), ini_foot_right, delta_angle, delay, 1)
    time.sleep(delay_move)
    #body
    servo_move(ini_body_right, (ini_body_right - rotate_body + alfa_body), delta_angle, delay, 2)
    servo_move(ini_body_left, (ini_body_left - rotate_body), delta_angle, delay, 3)
    time.sleep(delay_move)
    #foot
    servo_move((ini_foot_right - slope_onefoot), ini_foot_left, delta_angle, delay, 0)
    time.sleep(delay_action)
    
    while True:
        if do!=2:
            break
        #second action
        #foot
        servo_move(ini_foot_right, (ini_foot_right + slope_twofoot), delta_angle, delay, 0)
        servo_move(ini_foot_left, (ini_foot_left + slope_onefoot), delta_angle, delay, 1)
        servo_move((ini_foot_right + slope_twofoot), ini_foot_right, delta_angle, delay, 0)
        time.sleep(delay_move)
        #body
        servo_move((ini_foot_left - rotate_body), (ini_body_left + rotate_body), delta_angle, delay, 3)
        servo_move((ini_foot_right - rotate_body + alfa_body), (ini_body_right + rotate_body - alfa_body), delta_angle, delay, 2)
        time.sleep(delay_move)
        #foot
        servo_move((ini_foot_left + slope_onefoot), ini_foot_left, delta_angle, delay, 1)
        time.sleep(delay_action)
        
        if do!=2:
            break
        #third action
        #foot
        servo_move(ini_foot_left, (ini_foot_left - slope_twofoot), delta_angle, delay, 1)
        servo_move(ini_foot_right, (ini_foot_right - slope_onefoot), delta_angle, delay, 0)
        servo_move((ini_foot_left - slope_twofoot), ini_foot_left, delta_angle, delay, 1)
        time.sleep(delay_move)
        #body
        servo_move((ini_foot_right + rotate_body - alfa_body), (ini_body_right - rotate_body + alfa_body), delta_angle, delay, 2)
        servo_move((ini_foot_left + rotate_body), (ini_body_left - rotate_body), delta_angle, delay, 3)
        time.sleep(delay_move)
        #foot
        servo_move((ini_foot_right - slope_onefoot), ini_foot_right, delta_angle, delay, 0)
        time.sleep(delay_action)
        
    reset()
        


def move_left():
    body_right.duty_u16(servo_value(ini_body_right - 10))
    body_left.duty_u16(servo_value(ini_body_left - 10))
    
    while True:
        foot_left.duty_u16(servo_value(ini_foot_left + kick_angle))
        time.sleep(0.15)
        foot_right.duty_u16(servo_value(ini_foot_right - kick_angle))
        foot_left.duty_u16(servo_value(ini_foot_left - kick_angle))
        time.sleep(delay_action_side)
        
        foot_right.duty_u16(servo_value(ini_foot_right))
        foot_left.duty_u16(servo_value(ini_foot_left))
        time.sleep(delay_move_side)
        
        if do!=3:
            break
    
    reset()
    
def move_right():
    body_left.duty_u16(servo_value(ini_body_left + rotate_body_side))
    body_right.duty_u16(servo_value(ini_body_right - rotate_body_side))
    
    while True:
        foot_right.duty_u16(servo_value(ini_foot_right - kick_angle))
        time.sleep(0.1)
        foot_left.duty_u16(servo_value(ini_foot_left + kick_angle))
        foot_right.duty_u16(servo_value(ini_foot_right + kick_angle))
        time.sleep(delay_action_side)
        
        foot_left.duty_u16(servo_value(ini_foot_right))
        foot_right.duty_u16(servo_value(ini_foot_right))
        time.sleep(delay_move_side)
        
        if do!=4:
            break
    
    reset()
    


    
#Move servo function
#servo_move(start, target, delta, delay, pin)
def servo_move(current, target, delta, time, pin):
    servo = PWM(Pin(pin))
    servo.freq(50)
    if current < target:
        while current < target:
            servo.duty_u16(servo_value(current))
            current += delta
            utime.sleep(time)
    else:
        while target < current:
            servo.duty_u16(servo_value(current))
            current -= delta
            utime.sleep(time)


def servo_value(degree):
    return int((degree * 9.5 / 180 + 2.5) * 65535 / 100)


#robot control system
def signal_reset(p):
    global do
    do = 0
    
def signal_advance(p):
    global do
    do = 1
    
def signal_back(p):
    global do
    do = 2
    
def signal_left(p):
    global do
    do = 3

def signal_right(p):
    global do
    do = 4

    
trig_reset.irq(trigger=Pin.IRQ_RISING, handler=signal_reset)
trig_advance.irq(trigger=Pin.IRQ_RISING, handler=signal_advance)
trig_back.irq(trigger=Pin.IRQ_RISING, handler=signal_back)
trig_left.irq(trigger=Pin.IRQ_RISING, handler=signal_left)
trig_right.irq(trigger=Pin.IRQ_RISING, handler=signal_right)


if __name__=="__main__":
    main()




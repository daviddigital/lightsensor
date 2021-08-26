from microbit import *
display.show(Image.HAPPY)
sleep(2000)
for i in range(20):
    sleep(1000)
    time = running_time()
    temp = temperature()
    lightlevel = display.read_light_level()
    display.scroll(i+1)
    display.show(Image.SQUARE)
    print(str(time) + "," + str(temp) + "," + str(lightlevel))
    sleep(500)
    display.show(Image.YES)

display.clear()
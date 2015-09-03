import os
from subprocess import call
from multiprocessing import *

#function which launches a robot
def launchrobot(portnumber):
    call(["/opt/KapowKatalyst_9.4.6_x64/bin/RoboServer", "-p "+ portnumber])


#read in port numbers we wish to spawn robots from
robots = []
with open('/opt/KapowKatalyst_9.4.6_x64/config/robots.conf', 'rb') as f:
    for i in f:
        robots.append(i)


#for each port in robots.conf launch a robot under a seperate process
for robot in robots:
    p = Process(target=launchrobot, args=(robot,))
    p.start()


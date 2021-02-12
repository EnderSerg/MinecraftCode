from mcpi.minecraft import Minecraft
from time import sleep
from random import randint

mc = Minecraft.create()
sleep  (10)
rz = randint(0,1000)
rx = randint(0,1000)
h = mc.getHeight(rx,rz)
mc.player.setPos(rx,h+1,rz)

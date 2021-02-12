from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)
mc.setBlocks(x,y,z,x+15,y+4,z-15,46)

from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,80)
sleep(5)
mc.setBlock(x,y+1,z,80)
sleep(5)
mc.setBlock(x,y+2,z,86)

from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)

mc.setBlocks(x,y,z,x+10,y+1,z+10,80)
sleep(5)
mc.setBlocks(x,y+2,z,x+10,y+2,z+10,86)


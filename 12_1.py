from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)

mc.setBlocks(x,y,z,x,y+8,z,201)
sleep(5)
mc.setBlocks(x,y+8,z,x,y+8,z,8)
sleep(5)
mc.setBlocks(x,y+9,z,x,y+9,z,11)

sleep(5)


sleep(5)
mc.setBlocks(x,y+10,z,x,y+10,z,8)
sleep(5)
mc.setBlocks(x,y+11,z,x,y+11,z,11)

sleep(5)


sleep(5)
mc.setBlocks(x,y+12,z,x,y+12,z,8)
sleep(5)
mc.setBlocks(x,y+13,z,x,y+13,z,11)

sleep(5)
mc.setBlocks(x,y+14,z,x,y+14,z,8)

from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)



mc.setBlocks(x,y,z,x,y-40,z,8)
sleep(5)
mc.setBlock(x,y-41,z,213)

sleep(5)



mc.setBlocks(x+4,y,z,x+4,y-40,z,8)
sleep(5)
mc.setBlock(x+4,y-41,z,88)

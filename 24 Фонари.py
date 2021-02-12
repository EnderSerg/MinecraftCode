from mcpi.minecraft import Minecraft
from time import sleep

print("hi ok")
mc = Minecraft.create() 
x,y,z = mc.player.getTilePos()
sleep(10)
size = 0
for meow in range(5):
    mc.setBlocks(x+size,y,z,x+size,y+1,z,139)
    mc.setBlock(x+size,y+2,z,169)
    size += 10

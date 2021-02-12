from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 
x,y,z = mc.player.getTilePos()
print(x)
sleep(10)
size = 10
for meow in range(15):   
    mc.setBlocks(x-size,y+meow,z-size,x+size,y+meow,z+size,57)
    size -= 1
    mc.setBlocks(x-size,y+meow,z-size,x+size,y+meow,z+size,0)
mc.setBlock(x,y+10,z,138)
mc.postToChat('tfhfhrrfhf')


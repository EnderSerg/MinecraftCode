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
def roof():
    size = 10
    lenght = 5
    for meow in range(size):   
        mc.setBlocks(x-size,y+meow,z-lenght,x+size,y+meow,z+lenght,57)
        size -= 1
        mc.setBlocks(x-size,y+meow,z-lenght,x+size,y+meow,z+lenght,0)
    mc.setBlocks(x,y+10,z-lenght,x,y+10,z+lenght,57)
roof()
mc.postToChat('tfhfhrrfhf')


from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(10)

for meow in range(300):
    sleep(1)
    mc.setBlock(x,y,z,meow)

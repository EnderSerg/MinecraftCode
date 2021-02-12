from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(10)
rz = randint(0,255)
for a in range(15):
    size -= 4
    rz = randint(0,255)
    sleep(1)
    #mc.setBlock(x,y,z,meow)
    md.drawHorizontalCircle(x,y+meow,z,10,rz)

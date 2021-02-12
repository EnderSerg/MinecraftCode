from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(5)
#md.drawHollowSphere(x,y,z,10,24)
md.drawSphere(x,y,z,10,0)

md.drawHollowSphere(x,y+20,z,10,24)

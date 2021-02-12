from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(5)
h = randint(1,258)
md.drawHollowSphere(x,y,z,10,80)

md.drawHollowSphere(x,y+12,z,8,80)

md.drawHollowSphere(x,y+22,z,7,80)

#mc.setBlocks(x,y+2,z,x+10,y+2,z+10,86)

md.drawHollowSphere(x,y+22,z,6,h)


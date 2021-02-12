from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(5)
#md.drawHorizontalCircle(x,y,z,10,21)

#md.drawCircle(x,y,z,10,21)

#md.drawHollowSphere(x,y,z,9,20)
md.drawCircle(x+10,y-1,z,10,67)

md.drawCircle(x+10,y-1,z+5,7,23)

md.drawCircle(x+10,y-1,z+10,5,45)

md.drawCircle(x+10,y-1,z+15,3,89)

md.drawCircle(x+10,y-1,z+20,1,37)

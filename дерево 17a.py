from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 

x,y,z = mc.player.getTilePos()
sleep(10)

for efsgt in range(5):   
       
    xw = randint(0,250)
    wx = randint(0,250)

    rz = randint(0,50)
    rx = randint(0,50)
    h = mc.getHeight(rx,rz)
    md.drawHollowSphere(rx,h+4,rz,3,wx)

    mc.setBlocks(rx,h,rz,rx,h+4,rz,xw)
    mc.postToChat(rx)
    mc.postToChat(rz)
    mc.player.setPos(rx+2,h,rz)
mc.postToChat('tfhfhrrfhf')

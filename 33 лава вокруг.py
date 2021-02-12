from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 
while True:
    x,y,z = mc.player.getTilePos()
    blocks = mc.events.pollBlockHits()
    for block in blocks:
        bx,by,bz = block.pos
        x,y,z = mc.player.getTilePos()
        sleep(5)

        md.drawHollowSphere(x,y,z,8,166)
        md.drawHollowSphere(x,y,z,9,10)
        md.drawHollowSphere(x,y,z,10,166)

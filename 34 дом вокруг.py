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
        size = 0
        rc = randint(0,15)
        mc.postToChat("hi ok ")
        for meow in range(rc):
          
          
            mc.setBlocks(bx,by+size,bz,bx+5,by+size,bz+5,35,rc)
            mc.setBlocks(bx,by+1+size,bz,bx+5,by+1+size,bz+5,35,rc)
            mc.setBlocks(bx+1,by+1+size,bz+1,bx+4,by+1+size,bz+4,0)
            mc.setBlocks(bx,by+2+size,bz,bx+5,by+2+size,bz+5,20)
            mc.setBlocks(bx+1,by+2+size,bz+1,bx+4,by+2+size,bz+4,0)
            size = size+3
          

from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
x,y,z = mc.player.getTilePos()
while True:
    x,y,z = mc.player.getTilePos()
    blocks = mc.events.pollBlockHits()
    for block in blocks:
        bx,by,bz = block.pos
        by+=1
        mc.setBlock(bx,by,bz,41)
        mc.setBlocks(bx,by,bz,bx,by+1,bz,139)
        mc.setBlock(bx,by+2,bz,169)
        

from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()

def setColona():
    
    mc.setBlocks(bx,by,bz,bx,by+2,bz,155,1)
    mc.setBlock(bx,by+3,bz,169)
    mc.setBlock(bx+1,by,bz,156,1)                
    mc.setBlock(bx-1,by,bz,156,0)
    mc.setBlock(bx,by,bz+1,156,3)
    mc.setBlock(bx,by,bz-1,156,2)
    mc.setBlocks(bx,by,bz-1,bx,by+2,bz-5,22)
    
    mc.setBlocks(bx,by,bz-5,bx,by+2,bz-5,155,1) 
    mc.setBlock(bx,by+3,bz-5,89)
    mc.setBlock(bx+1,by,bz-5,156,1)                
    mc.setBlock(bx-1,by,bz-5,156,0)
    mc.setBlock(bx,by,bz+1-5,156,3)
    mc.setBlock(bx,by,bz-1-5,156,2)
    
sleep(1)
x,y,z = mc.player.getTilePos()
while True:
    x,y,z = mc.player.getTilePos()
    blocks = mc.events.pollBlockHits()
    for block in blocks:
        bx,by,bz = block.pos
        by+=1#не под землей, а над ней
        
        for meow in range(10):
            setColona()
            bz+=5

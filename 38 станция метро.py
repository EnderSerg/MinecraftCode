from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 
x,y,z = mc.player.getTilePos()
def setColona(bx,by,bz):#объявляем функцию
    
    mc.setBlocks(bx,by,bz,bx,by+2,bz,155,1)
    mc.setBlock(bx,by+3,bz,57)
    mc.setBlock(bx+1,by,bz,156,1)                
    mc.setBlock(bx-1,by,bz,156,0)
    mc.setBlock(bx,by,bz+1,156,3)
    mc.setBlock(bx,by,bz-1,156,2)

sleep(10)
xSize=5
zSize=10
mc.setBlocks(x-xSize,y-1,z-zSize,x+xSize,y-1,z+zSize,45)
mc.setBlocks(x-xSize,y+4,z-zSize,x+xSize,y+4,z+zSize,45)
for meow in range(5):
  setColona(x-xSize+1,y,z-zSize+meow*4)
  setColona(x+xSize-1,y,z-zSize+meow*4)
mc.postToChat('tfhfhrrfhf')

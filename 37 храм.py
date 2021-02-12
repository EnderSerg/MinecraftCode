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
def roof():
    size = 10
    lenght = 5
    for meow in range(size):   
        mc.setBlocks(x-size,y+meow,z-lenght,x+size,y+meow,z+lenght,57)
        size -= 1
        mc.setBlocks(x-size,y+meow,z-lenght,x+size,y+meow,z+lenght,0)
    mc.setBlocks(x,y+10,z-lenght,x,y+10,z+lenght,57)
sleep(10)
mc.setBlocks(x-10,y-1,z-5,x+10,y-1,z+5,45)
for meow in range(3):
  setColona(x-8,y,z-5+meow*4)
  setColona(x+8,y,z-5+meow*4)
y+=3
roof()
mc.postToChat('tfhfhrrfhf')


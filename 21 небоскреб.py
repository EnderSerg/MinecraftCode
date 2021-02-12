from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff import MinecraftDrawing  
print("hi ok")
mc = Minecraft.create()
md = MinecraftDrawing(mc) 
x,y,z = mc.player.getTilePos()
print(x)
sleep(10)
size = 1
for meow in range(15):
  
  
  mc.setBlocks(x,y+size,z,x+5,y+size,z+5,35)
  mc.setBlocks(x,y+1+size,z,x+5,y+1+size,z+5,35)
  mc.setBlocks(x+1,y+1+size,z+1,x+4,y+1+size,z+4,0)
  mc.setBlocks(x,y+2+size,z,x+5,y+2+size,z+5,20)
  mc.setBlocks(x+1,y+2+size,z+1,x+4,y+2+size,z+4,0)
  size = size+3

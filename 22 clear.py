from mcpi.minecraft import Minecraft
from time import sleep

print("hi ok")
mc = Minecraft.create() 
x,y,z = mc.player.getTilePos()
sleep(10)

#def zRoad(x1,y1,z1,lenght):
  #ks(x1-3,y1+1,z1,x1-3,y1+1,z1+lenght,44)#левый бордюр
  #mc.setBlocks(x1+3,y+1,z,x1+3,y1+1,z1+lenght,44)#правый бордюр
  #for meow in range(lenght//4):
    #mc.setBlocks(x1,y1,z1+size,x1,y1,z1+2+size,33)
    #size += 4
#zRoad(269,68,289,10)


def xRoad(x1,y1,z1,lenght):
  size = 0
  mc.setBlocks(x1,y1,z1-3,x1+lenght,y1,z1+3,22)#дорога
  mc.setBlocks(x1,y1+1,z1-3,x1+lenght,y1+1,z1-3,44)#левый бордюр
  mc.setBlocks(x1,y1+1,z1+3,x1+lenght,y1+1,z1+3,44)#правый бордюр
  for meow in range(lenght//4):
    mc.setBlocks(x1+size,y1,z1,x1+2+size,y1,z1,33)
    size += 4
xRoad(x,y,z,240)

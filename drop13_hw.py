from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)
c = randint(0,1000)
u = randint(0,500)
mc.dropItem(x,y,z,c)

#mc.spawnEntity(x,y,z,53)

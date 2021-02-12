from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
print("hi ok")
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
sleep(5)

mc.dropItem(x,y,z,123)

mc.spawnEntity(x,y,z,25)

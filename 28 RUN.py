from mcpi.minecraft import Minecraft
from time import sleep
print("hi ok")
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
print()
sleep(1)
mc.spawnEntity(x-50,y,z,53)

for meow in range(20):
  x,y,z = mc.player.getTilePos()
  mc.spawnEntity(x-10,y,z,3)
  mc.spawnEntity(x-10,y,z,26)
  mc.spawnEntity(x+10,y,z,104)
  mc.spawnEntity(x+20,y,z,105)

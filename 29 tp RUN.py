from mcpi.minecraft import Minecraft
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
while True:
    x,y,z = mc.player.getTilePos()
    block = mc.getBlock(x,y-1,z)
    if block==85:
        mc.postToChat(' ха ха ха ')
        mc.player.setPos(194,97,256)
        mc.setBlock(x,y-1,z,0)
        sleep(10)
        mc.spawnEntity(x,y-1,z,54)
        mc.spawnEntity(x,y-1,z,65)
        mc.spawnEntity(x,y-1,z,65)
        mc.spawnEntity(x,y-1,z,54)

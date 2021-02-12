from mcpi.minecraft import Minecraft
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
while True:
    x,y,z = mc.player.getTilePos()
    block = mc.getBlock(x,y-1,z)
    if block==91:
        mc.postToChat('Хэллоуин ха ха ха ')
        mc.setBlock(x,y-1,z,0)
        mc.spawnEntity(x,y-1,z,65)
        mc.spawnEntity(x,y-1,z,65)
        mc.spawnEntity(x,y-1,z,65)
        mc.spawnEntity(x,y-1,z,65)

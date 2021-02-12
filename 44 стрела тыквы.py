from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
while True:
    sleep(5)
    x,y,z = mc.player.getTilePos()#кординаты игрока
    blocks = mc.events.pollProjectileHits()#блоки в которых стрела
    for block in blocks:
        print(block)
        bx,by,bz = block.pos#кординаты блока
        blockid = mc.getBlock(bx-1,by,bz)#айди блока
        print(blockid)
        if blockid==91:
            mc.spawnEntity(bx,by,bz,20)

from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
t1x = 315
t1y = 70
t1z = 102

t2x = 312
t2y = 70
t2z = 102

t3x = 318
t3y = 70
t3z = 102

t4x = 315
t4y = 73
t4z = 102
while True:
    sleep(5)
    x,y,z = mc.player.getTilePos()#кординаты игрока
    blocks = mc.events.pollProjectileHits()#блоки в которых стрела
    for block in blocks:
        print(block)
        bx,by,bz = block.pos#кординаты блока со стрелой

        if bx==t1x and by==t1y and bz==t1z:
            mc.postToChat('попал ура')
            mc.setBlock(bx,by,bz-1,35,13)
            sleep(5)
            mc.setBlock(bx,by,bz-1,35,14)

        elif bx==t2x and by==t2y and bz==t2z:
            mc.postToChat('попал ура')
            mc.setBlock(bx,by,bz-1,35,13)
            sleep(5)
            mc.setBlock(bx,by,bz-1,35,14)

        elif bx==t3x and by==t3y and bz==t3z:
            mc.postToChat('попал ура')
            mc.setBlock(bx,by,bz-1,35,13)
            sleep(5)
            mc.setBlock(bx,by,bz-1,35,14)

        elif bx==t4x and by==t4y and bz==t4z:
            mc.postToChat('попал ура')
            mc.setBlock(bx,by,bz-1,35,13)
            sleep(5)
            mc.setBlock(bx,by,bz-1,35,14)

        else:
            mc.postToChat('не попал')






from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
while True:
    sleep(5)
    x,y,z = mc.player.getTilePos()
    blocks = mc.events.pollProjectileHits()
    for block in blocks:
        print(block)
        bx,by,bz = block.pos
        mc.spawnEntity(bx,by,bz,20)

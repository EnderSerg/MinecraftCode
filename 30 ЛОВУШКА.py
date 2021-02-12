from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
x,y,z = mc.player.getTilePos()
wa = randint(0,255)
aw = randint(0,5)+x
ra = randint(0,5)+z
gd = randint(0,255)
ar = randint(0,5)+x
dg = randint(0,5)+z
while True:
    x,y,z = mc.player.getTilePos()
    if x==aw and z==ra:
        mc.setBlock(aw,y-1,ra,wa)
    if x==ar and z==dg:
        mc.setBlock(ar,y-1,dg,gd)

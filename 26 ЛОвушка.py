from mcpi.minecraft import Minecraft
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
while True:
    wa = randint(0,255)
    aw = randint(0,100)
    ra = randint(0,10)
    x,y,z = mc.player.getTilePos()
    if x==158 and z==140:
        mc.setBlock(158,69,140,5)

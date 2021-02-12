from mcpi.minecraft import Minecraft
from time import sleep
print("hi ok")
mc = Minecraft.create()
print()
sleep(1)
while True:
    x,y,z = mc.player.getTilePos()
    if x==398 and z==319:
        mc.postToChat('добро пожаловать в пирамиду')

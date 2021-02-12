from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
sleep  (10)
h = mc.getHeight(127,80)
mc.player.setPos(127,h+1,80)

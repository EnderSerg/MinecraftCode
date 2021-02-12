from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle

mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)
diamond.setx(0)
diamond.sety(56)
diamond.setz(-47)
diamond.left(90)
diamond.penblock(50)
diamond.forward(51)

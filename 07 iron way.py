from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle
print("hi ok")
mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)
diamond.setx(177)
diamond.sety(69)
diamond.setz(78)

diamond.speed(10)
diamond.penblock(152)
diamond.forward(1000)
diamond.left(180)
diamond.sety(70)
diamond.penblock(27)

diamond.forward(1000)

from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle
print("hi ok")
mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)
diamond.setx(177)
diamond.sety(88)
diamond.setz(79)

diamond.speed(10)
diamond.penblock(152)
diamond.forward(1468)
diamond.left(90)
diamond.forward(217)
diamond.left(180)
diamond.sety(89)
diamond.penblock(27)
diamond.forward(217)
diamond.right(90)
diamond.forward(1468)

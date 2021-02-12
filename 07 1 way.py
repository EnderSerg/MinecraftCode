from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle
print("hi ok")
mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)
diamond.setx(201)
diamond.sety(71)
diamond.setz(102)

diamond.speed(10)
diamond.penblock(152)
diamond.forward(5)




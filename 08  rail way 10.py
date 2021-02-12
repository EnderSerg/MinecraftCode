from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle
print("hi ok")
mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)
diamond.setx(181)
diamond.sety(65)
diamond.setz(68)
diamond.up(34)
diamond.speed(10)

dlina = 150

#ступеньки
diamond.penblock(89)
diamond.forward(dlina)

#факела
diamond.setposition(181, 66, 68)
diamond.penblock(50)
diamond.forward(dlina)

#воздух
diamond.setposition(181, 67, 68)
diamond.penblock(0)
diamond.forward(dlina)

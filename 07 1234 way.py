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
#diamond.left(90)

diamond.up(35)
diamond.forward(10)
diamond.right(90)
diamond.forward(7)
diamond.right(90)
diamond.forward(15)
diamond.down(35)
diamond.forward(15)

diamond.left(180)
diamond.sety(89)
diamond.penblock(27)
diamond.forward(217)
diamond.right(90)
diamond.forward(1468)

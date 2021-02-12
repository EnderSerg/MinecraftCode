from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
from minecraftstuff  import MinecraftTurtle
print("hi ok")
mc = Minecraft.create()
diamond =  MinecraftTurtle(mc)

#орога
diamond.setx(201)
diamond.sety(71)
diamond.setz(102)

diamond.speed(10)
diamond.penblock(152)
diamond.forward(5)
#diamond.left(90)

diamond.up(35)# вверх
diamond.forward(10)
diamond.right(90)
diamond.forward(7)
diamond.right(90)
diamond.forward(15)
diamond.down(35)# ровно
diamond.down(35)#вниз
diamond.forward(34)
diamond.right(90)
diamond.up(35)# ровно
diamond.up(35)# вверх

diamond.forward(6)
diamond.right(90)
diamond.forward(15)
diamond.down(35)# ровно
diamond.down(35)#вниз
diamond.forward(18)
diamond.up(35)# ровно


#рельсы
diamond.setx(201)
diamond.sety(72)
diamond.setz(102)

diamond.speed(10)
diamond.penblock(27)
diamond.forward(5)
#diamond.left(90)

diamond.up(35)# вверх
diamond.forward(10)
diamond.right(90)
diamond.forward(7)
diamond.right(90)
diamond.forward(15)
diamond.down(35)# ровно
diamond.down(35)#вниз
diamond.forward(34)
diamond.right(90)
diamond.up(35)# ровно
diamond.up(35)# вверх

diamond.forward(6)
diamond.right(90)
diamond.forward(15)
diamond.down(35)# ровно
diamond.down(35)#вниз
diamond.forward(18)
diamond.up(35)# ровно


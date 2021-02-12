from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
x,y,z = mc.player.getTilePos()
while True:
    sleep(5)
    x,y,z = mc.player.getTilePos()
    posts = mc.events.pollChatPosts()
    for post in posts:
        text = post.message
        text = text.lower()
        print(post)
        if text == 'wowhello':
             rc = randint(0,15)
             size = 4
             for meow in range(rc):
          
          
                 mc.setBlocks(x,y+size,z,x+5,y+size,z+5,35,rc) 
                 mc.setBlocks(x,y+1+size,z,x+5,y+1+size,z+5,35,rc)
                 mc.setBlocks(x+1,y+1+size,z+1,x+4,y+1+size,z+4,0)
                 mc.setBlocks(x,y+2+size,z,x+5,y+2+size,z+5,20)
                 mc.setBlocks(x+1,y+2+size,z+1,x+4,y+2+size,z+4,0)
                 size = size+3


        if text == 'snowman':
            mc.player.setPos(230,106,174)
 

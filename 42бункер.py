from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
doorX = 241
doorZ = 104
x,y,z = mc.player.getTilePos()
while True:
    sleep(5)
    x,y,z = mc.player.getTilePos()
    posts = mc.events.pollChatPosts()
    for post in posts:
        text = post.message
        text = text.lower()#все буквы маленькие
        print(post)
        if text == 'open':
            if x==doorX and z==doorZ+1 or z==doorZ-1:
                mc.setBlocks(doorX,y,doorZ,doorX,y+1,doorZ,0)
                sleep(5)
                mc.setBlocks(doorX,y,doorZ,doorX,y+1,doorZ,1,4)

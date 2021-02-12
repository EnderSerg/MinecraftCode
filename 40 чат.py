from mcpi.minecraft import Minecraft
from random import randint
from time import sleep
print("hi ok")
mc = Minecraft.create()
sleep(1)
x,y,z = mc.player.getTilePos()
while True:
    sleep(5)
    #x,y,z = mc.player.getTilePos()
    posts = mc.events.pollChatPosts()
    for post in posts:
        print(post)
        if post.message == 'Hello':
            mc.postToChat('Hello and WHAT')

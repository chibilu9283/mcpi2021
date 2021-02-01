from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+' '+'Y:'+str(y)+' '+'Z:'+str(z))

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x+2,y,z+2,x-2,y,z-2,20)
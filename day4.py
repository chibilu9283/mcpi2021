from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import random

x,y,z=mc.player.getTilePos()

for a in range(20):
    r=random.randint(1,4)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z=z-4
        
for a in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+a
    
    for b in range(10):
        r=random.randint(0,15)
        z=z+1
        mc.setBlock(x,y,z,35,r)
        
r=random.randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data==r:
            mc.postToChat('可惡被找到了')
            mc.setBlock(hit.pos,57)
            break
        
        elif data<r:
            mc.postToChat('大一點啊')
            
        elif data>r:
            mc.postToChat('小一點啊')
            
myID=mc.getPlayerEntityId('Chibilu')
mc.postToTitle(myID,'hihi')














from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlocks(x,y,z,x+4,y+4,z+4,20)
mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3,0)

while True:
    x,y,=mc.player.getTilePos()
    mc.setBlocks(x,y-1,z,x+1,y,z+1,20)
    
import time 
   
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(10)
    
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,20)
    time.sleep(0.001)
    
    
x,y,z=mc.player.getTilePos()
a=0

while a<10:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z=z+5
    a=a+1
    
x,y,z=mc.player.getTilePos()

a=int(input('想放什麼方塊呢?'))
mc.setBlock(x,y,z,a)

name=input('請輸入名字:')
message=input('輸入訊息:')  
mc.postToChat('<'+name+'>'+message)

x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,1,'','hiihi','','')

while True:
    x,y,z=mc.player.getTilePos()
    
    a=mc.getBlockWithData(x,y-1,z)
    if a.data==15:
        mc.postToChat('哈哈笑你')
        
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits) >0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        #mc.postToChat('方塊id:'+str(block))
        block=mc.getBlock(x,y,z,)
        
        if block==1:
            mc.setBlock(x,y,z,41)
            
x,y,z=mc.player.getPos()
mc.spawnEntity(x,y,z,92)
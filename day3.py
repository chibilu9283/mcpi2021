from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import random
import time

while True:
    x,y,z=mc.player.getTilePos()
    x=x+random.randrange(-10,10)
    y=y+30
    z=z+random.randrange(-10,10)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.2)
    
while True:
    hits=mc.events.pollProjectileHits()
    
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.createExplosion(x,y,z)
        
while True:
    hits=mc.events.pollProjectileHits()
    
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.player.setPos(x,y,z)
        
x,y,z=mc.player.getTilePos()

for a in range(10):
    mc.setBlock(x+a,y,z,7)
    
for b in range(10):
    mc.setBlocks(x,y,z+b,x+2,y,z+b,7)
    
def plantree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z=mc.player.getTilePos()
    
for c in range(8):
    for d in range(6):
        plantree(x+c*5,y+d*c+d*c,z)
    

    
            
    

            
    

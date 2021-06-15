# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:33:57 2021

@author: User
"""

from vpython import *
size = 0.1          #球半徑 0.1 m

scene = display(width=800, height=800,  background=(0.5,0.5,0))             	#畫面設定
b1 = sphere(radius = size,  color=color.yellow)         				#畫球1
b2 = sphere(radius = size,  color=color.green)          				#畫球2
floor = box(length=2, height=0.01, width=10, color=color.blue)       

b1.pos = vector( 0.1 , 1, 0)                        	#球1初位置
b2.pos = vector( 0 ,  0.5, 0)                           	#球2初位置
b1.v = vector(0, -1, 0)                              	#球1初速
b2.v = vector(0 , 0, 0)                                	#球2初速

dt = 0.001                                                          
while True:
    rate(1000)
					
    b1.pos += b1.v * dt 
    b2.pos += b2.v * dt
#dot(b1.v, b2.v) == msg(b1.v)*msg(b2.v)*cos(diff_angle(b1.v,b2.v))
# 其實單純看 cos也行 基本上正負只看cos hackmd有交
    
    
    if mag(b1.pos - b2.pos)<=2*size and dot(b1.v, b2.v) <= 0 :
        v1prime = b1.v - (b1.pos-b2.pos)  * dot (b1.v-b2.v, b1.pos-b2.pos) / mag(b1.pos-b2.pos)**2
        v2prime = b2.v - (b2.pos-b1.pos)  * dot (b2.v-b1.v, b2.pos-b1.pos) / mag(b2.pos-b1.pos)**2
        
        b1.v=v1prime
        
        b2.v=v2prime
       
    if(b2.pos.y<=0+size):
        b2.v=vector(0,0,0)
    if(b1.pos.y<=0+size):
        b1.v=vector(0,0,0)  

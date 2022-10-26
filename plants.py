# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:55:41 2022

@author: maiwe
"""

class plants:
    def __init__(self,quality,position):
        self.quality=quality
        self.position=position
    
    def get_position(self):
        return self.position
    
    def get_quality(self):
        return self.quality
    
    def quality(self,delta):
        self.quality=(1-delta)*self.quality
    
    def position(self,newposition):
        self.position=newposition  
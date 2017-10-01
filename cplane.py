#!/usr/bin/env python3

from abscplane import AbsComplexPlane

class ListComplexPlane(AbsComplexPlane):
    #list of lists in plane structure
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.plane = []
        self.fs = []
        
        dx = (xmax - xmin)/(xlen-1)
        dy = (ymax - ymin)/(ylen-1)
        
    
    def refresh(self):
        
        
    def apply(self, f):
        
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        
    #params are user input. can be reset with zoom
    
    
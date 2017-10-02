#!/usr/bin/env python3

from abscplane import AbsComplexPlane

class ListComplexPlane(AbsComplexPlane):
    #initializing the attributes
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = float(xmin)
        self.xmax = float(xmax)
        self.xlen = int(xlen)
        self.ymin = float(ymin)
        self.ymax = float(ymax)
        self.ylen = int(ylen)
        self.plane = __create_plane(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        self.fs = []
        
    ##creates plane of complex points    
    def __create_plane(xmin, xmax, xlen, ymin, ymax, ylen)
        
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        
        #lists of points on the x and y axis
        xpoints = []
        ypoints = []
        
        #appends points to the x axis
        xpoints.append(xmin)
        
        while i in (1...xlen):
            xpoints.append(xmin + i*dx)
            
        #appends points to the y axis
        ypoints.append(ymin)
    
        while i in (1...ylen):
            ypoints.append(ymin + i*dy)
        
        #create plane
        plane = []
        
        for x in xpoints:
            for y in ypoints:
                plane.append([x + ])
                
        
    
    def refresh(self):
        
        x = self.xmin
        y = self.ymin
        xl = self.xlen
        yl = self.ylen
        self.plane = []
        self.fs = []
        
        dx = (xmax - x)/(xl-1)
        dy = (ymax - y)/(yl-1)
        
        
    def apply(self, f):
        
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        
    #params are user input. can be reset with zoom
    
    
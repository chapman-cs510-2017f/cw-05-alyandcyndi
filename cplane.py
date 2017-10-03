#!/usr/bin/env python3

###
# Name: Aly Baughman, Cynthia Parks
# Student ID: 1923165, 2303535
# Email: baugh107@mail.chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

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
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        self.fs = []
        
    ##creates plane of complex points    
    def __create_plane(self, xmin, xmax, xlen, ymin, ymax, ylen):
        
        dx = (xmax - xmin)/(xlen - 1)
        dy = (ymax - ymin)/(ylen - 1)
        
        #lists of points on the x and y axis
        xpoints = []
        ypoints = []
        
        #appends points to the x axis
        xpoints.append(xmin)
        
        for i in range(1, xlen):
            xpoints.append(xmin + i*dx)
            
        #appends points to the y axis
        ypoints.append(ymin)
    
        for i in range(1,ylen):
            ypoints.append(ymin + i*dy)
        
        plane = []
        
        for x in xpoints:
            for y in ypoints:
                plane.append([x + y*1j])
        print(plane)
        return plane
                
        
    
    def refresh(self):

        self.plane = self.__create_plane(self, xmin, xmax, xlen, ymin, ymax, ylen)
        self.fs = []

    def apply(self, f):
        
        self.fs.append(f)
        self.f = f
        for i in range(self.xlen):
            for j in range(self.ylen):
                self.plane[i][j] = f(self.plane[i][j])
        
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        
        for f in self.fs:
            self.apply(f)
            
        return self.plane
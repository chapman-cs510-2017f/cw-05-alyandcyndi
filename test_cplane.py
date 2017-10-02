#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Aly Baughman, Cynthia Parks
# Student ID: 1923165, 2303535
# Email: baugh107@mail.chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 5
###

import cplane

def test_cplane():
    result=cplane.ListComplexPlane(0,2,2,0,4,2)
    correct=[[0,4j],[2,2+4j]]
    assert result==correct
    
def test_apply():
    result=cplane.ListComplexPlane(0,2,2,0,4,2)
    correct=[[0,4j],[2,2+4j]] 
    assert result==correct

    result2=result.apply(f)
    correct2=[[2,2+4j],[4,4+4j]]
    assert result2==correct2

def test_zoom():
    result=cplane.ListComplexPlane(0,2,2,0,4,2)
    result.apply(f)
    result.zoom(1,2,2,1,2,2)
    correct=[[3+1j,3+2j],[4+1j,4+2j]]
    assert result==corect

def test_refresh():
    result=cplane.ListComplexPlane(0,2,2,0,4,2)
    result.apply(f)
    result.refresh()
    correct=[[0,4j],[2,2+4j]]
    assert result==correct


    

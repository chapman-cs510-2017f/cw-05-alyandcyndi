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
    result=cplane.ListComplexPlane(0,10,2,0,8,2)
    correct=[[[0j], [8j]], [[(10+0j)], [(10+8j)]]]
    assert result==correct
    
def f(z):
    return z+1
    
def test_apply():
    result=cplane.ListComplexPlane(0,10,2,0,8,2)
    correct=[[[0j], [8j]], [[(10+0j)], [(10+8j)]]]
    assert result==correct

    result1=result.apply(f)
    correct1=[[[1+1j], [1+9j]], [[(11+1j)], [(11+9j)]]]
    assert result1==correct1



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:15:18 2021

@author: justinkaufman
"""



## COMMENT ABOUT CODE/OUTPUT -> initial position does not change to blue everything else does once new square is clicked ##


import tkinter as tk
from tkinter import *

root=tk.Tk()


    
locPrev=1
previously_clicked=None

def clicker(event, n):
    
    
    global locPrev
    #print(locPrev)
    #print ("you clicked on", event.widget)
    #print (len(str(event.widget)))
    if len(str(event.widget))<20: 
        loc2=1
    elif len(str(event.widget))==20:
        loc=str(event.widget)[-1]
        loc2=int(loc)
    elif len(str(event.widget))>20:
        loc=str(event.widget)[-2:]
        loc2=int(loc)
    #print(loc2)

    
    global previously_clicked
    
    
    
    #right 2 down 1
    #left 2 down 1
    if (locPrev+n+2==loc2 or locPrev+n-2==loc2):
        color="orange"
        event.widget.config(bg=color)
        locPrev=loc2
        if previously_clicked:
            previously_clicked['bg'] = "blue"
        previously_clicked = event.widget
            
    #right 2 up 1
    #left 2 up 1
    elif (locPrev-n+2==loc2 or locPrev-n-2==loc2):
        color="orange"
        event.widget.config(bg=color)
        locPrev=loc2
        if previously_clicked:
            previously_clicked['bg'] = "blue"
        previously_clicked = event.widget
        
    #up 2 right 1
    #up 2 left 1
    elif (locPrev-2*n+1==loc2 or locPrev-2*n-1==loc2):
        color="orange" 
        event.widget.config(bg=color)
        locPrev=loc2
        if previously_clicked:
            previously_clicked['bg'] = "blue"
        previously_clicked = event.widget
        
    #down 2 right 1
    #down 2 left 1
    elif (locPrev+2*n+1==loc2 or locPrev+2*n-1==loc2):
        color="orange"
        event.widget.config(bg=color)
        locPrev=loc2
        if previously_clicked:
            previously_clicked['bg'] = "blue"
        previously_clicked = event.widget

    


def knights_tour(n):

    frame = LabelFrame(root, bg="white")
    frame.pack(fill="both",expand=True)

    hw=n

    
    for i in range(n):
        for j in range(n):
            
            
            f=tk.Label(frame,height=hw,width=hw*2,borderwidth=1,relief="solid",background="white")
            if i ==0 and j ==0:
                f.grid(row=0, column =0)
                f.configure(bg="orange")


            f.grid(row=i, column =j)

            f.bind('<Button-1>' , lambda event, n=n: clicker(event, n))
            
 
    

         
         
         
if __name__=="__main__":
    knights_tour(5)
    root.mainloop()






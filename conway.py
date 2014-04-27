
"""
Conway's Game of Life

In progress! Not sure boundary conditions are working

Ronan Murphy 2014
"""

import sys
import pygame
import numpy as np
import random as rd

pygame.init()

m=100 #number of sites
n=m*5
X = np.zeros((m,m)) #initialize matrix
Y = np.zeros((m,m)) #'iterate' matrix

#variables
SCREEN_SIZE = n,n
WHITE = (255,255,255)
BLACK = (0,0,0)
SQUARE = 5
initial_percent = 15 #'percentage density' of initial population

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)
clock = pygame.time.Clock()

			
class Evolve:
	
	def initialize_matrices():
		#set up random distribution of live cells
		global X
		global Y
		for i in range (0,m-1):
			for j in range (0,m-1):
				if rd.randint(0,100) < initial_percent:
					X[i,j]=1
					
	
	def iterate_population():
		global X
		global Y
		#non-edge cells
		for i in range (1,m-2):
			for j in range (1,m-2):
				S = X.item(i-1,j) + X.item(i+1,j) + X.item(i-1,j-1) + X.item(i,j-1) + X.item(i+1,j-1) + X.item(i-1,j+1) + X.item(i,j+1) + X.item(i+1,j+1)
				if S < 2:
					Y[i,j]=0
				if S == 2:
					Y[i,j]=X.item(i,j)
				if S == 3:
					Y[i,j]=1
				if S > 3:
					Y[i,j]=0
				
		#edges, excluding corners
		for k in range (1,m-2):			
			#top
			S = X.item(0,k-1) + X.item(0,k+1) + X.item(1,k-1) + X.item(1,k) + X.item(1,k+1) + X.item(m-1,k-1) + X.item(m-1,k) + X.item(m-1,k+1)
			if S < 2:
				Y[0,k]=0
			if S == 2:
				Y[0,k]=X.item(0,k)
			if S == 3:
				Y[0,k]=1
			if S > 3:
				Y[0,k]=0
			#bottom	
			S = X.item(m-1,k-1) + X.item(m-1,k+1) + X.item(m-2,k-1) + X.item(m-2,k) + X.item(m-2,k+1) + X.item(0,k-1) + X.item(0,k) + X.item(0,k+1)
			if S < 2:
				Y[m-1,k]=0
			if S == 2:
				Y[m-1,k]=X.item(m-1,k)
			if S == 3:
				Y[m-1,k]=1
			if S > 3:
				Y[m-1,k]=0		
			#left
			S = X.item(k-1,0) + X.item(k+1,0) + X.item(k-1,1) + X.item(k,1) + X.item(k+1,1) + X.item(k-1,m-1) + X.item(k,m-1) + X.item(k+1,m-1)
			if S < 2:
				Y[k,0]=0
			if S == 2:
				Y[k,0]=X.item(k,0)
			if S == 3:
				Y[k,0]=1
			if S > 3:
				Y[k,0]=0
			#right
			S = X.item(k-1,m-1) + X.item(k+1,m-1) + X.item(k-1,m-2) + X.item(k,m-2) + X.item(k+1,m-2) + X.item(k-1,0) + X.item(k,0) + X.item(k+1,0)
			if S < 2:
				Y[k,m-1]=0
			if S == 2:
				Y[k,m-1]=X.item(k,m-1)
			if S == 3:
				Y[k,m-1]=1
			if S > 3:
				Y[k,m-1]=0
		#corners
		#top left	
		S = X.item(0,1) + X.item(0,m-1) + X.item(1,0) + X.item(1,1) + X.item(1,m-1) + X.item(m-1,0) + X.item(m-1,1) + X.item(m-1,m-1)
		if S < 2:
			Y[0,0]=0
		if S == 2:
			Y[0,0]=X.item(0,0)
		if S == 3:
			Y[0,0]=1
		if S > 3:
			Y[0,0]=0
		
		#top right	
		S = X.item(0,0) + X.item(1,0) + X.item(m-1,0) + X.item(1,m-1) + X.item(0,m-2) + X.item(1,m-2) + X.item(m-1,m-1) + X.item(m-1,m-2)
		if S < 2:
			Y[0,m-1]=0
		if S == 2:
			Y[0,m-1]=X.item(0,m-1)
		if S == 3:
			Y[0,m-1]=1
		if S > 3:
			Y[0,m-1]=0
			
		#bottom left	
		S = X.item(0,0) + X.item(0,1) + X.item(1,m-1) + X.item(m-2,0) + X.item(m-2,1) + X.item(m-1,1) + X.item(m-2,m-1) + X.item(m-1,m-1)
		if S < 2:
			Y[m-1,0]=0
		if S == 2:
			Y[m-1,0]=X.item(m-1,0)
		if S == 3:
			Y[m-1,0]=1
		if S > 3:
			Y[m-1,0]=0
		
		#bottom right	
		S = X.item(0,0) + X.item(0,m-2) + X.item(0,m-1) + X.item(m-2,0) + X.item(m-1,0) + X.item(m-2,m-2) + X.item(m-2,m-1) + X.item(m-1,m-2)
		if S < 2:
			Y[m-1,m-1]=0
		if S == 2:
			Y[m-1,m-1]=X.item(m-1,m-1)
		if S == 3:
			Y[m-1,m-1]=1
		if S > 3:
			Y[m-1,m-1]=0
					
		X=Y
		Y = np.zeros((m,m))

	def draw_population():
		for i in range (0,m-1):
			for j in range (0,m-1):
				colour=(WHITE)
				if X.item(i,j)==1:
					colour=BLACK
				pygame.draw.rect(screen,colour,[SQUARE*i,SQUARE*j,SQUARE,SQUARE])
				
	def run_sim():
		#iterate infinitely - ctrl+c to exit
		while 1:
			clock.tick(60)
		
			Evolve.iterate_population()
	
			screen.fill(WHITE)
	
			Evolve.draw_population()
			
			
		 
			pygame.display.flip()
		


#run program
Evolve.initialize_matrices()
Evolve.run_sim()
		

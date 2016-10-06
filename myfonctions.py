#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
from math import sqrt
from pprint import pprint

"""Fonction qui cree une matrice carrée et linitialise a la matrice nulle"""
def CreeMatCar(n):
	return [ [0.0 for j in range(0,n)] for i in range(0,n) ]

"""Fonction qui cree une matrice identite"""
def CreeMatId(n):
	I=CreeMatCar(n)
	for i in range(0,n):
		I[i][i]=1.0
	return I

"""Fonction qui copie une matrice ds une autre matrice"""
def CopyMatr(A):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			B[i][j]=A[i][j]
	return B

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
	for k in range(len(M)-1,-1,-1):
		(M[k][j],M[k][i])=(M[k][i],M[k][j])

"""Fonction qui triangule une matrice carre--triangulaire supérieure--"""
def Triangule(M):
	sign=1
	n=len(M) -1
	for i in range(n,0,-1):#A partir de  la derniere jusqua la 2eme ligne 
		for j in range(0,i):#Mij=0 si j<i
			if M[i][j+1] !=0.0:#Si c'est nulle, jai qu'a faire une permutation pour avoir 0
				q=(M[i][j])/(M[i][j+1]) 
				if q!=0.0:#Si c'est nulle, pas besoin de le rendre nulle
					for k in range(n,-1,-1):#A chaque combinaison, c'est les éléments de toute la colonne qui doivent changer
						M[k][j]= M[k][j] - q*M[k][j+1]
			else:
				PermCol(M,j+1,j)
				sign=sign*(-1)#le determinant est multipli par -1 si on permute deux colonnes de la matrice
	return M,sign


"""Fonction qui calcule le determinant une matrice carre"""
def Determinant(M):
	(Mtriang,sign)=Triangule(M)
	return round(sign*ProdDiag(Mtriang),2)


###################################################################
###################################################deuxieme Semestre
import math as m
import time
#from basicFunctions import *
n=0

#############################################
#Fonctions pour la resolution par Gauss
def recherchepivot(k,A):
	i=k
	while i!=n and A[i][k]==0:
		i+=1
	if i!=n:
		return i
	else:
		return -1


def permutation(i0,i,A,b):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination(k,A,b):
	i=k+1
	while i < n:
		r = round((A[i][k]/A[k][k]),3)
		b[i] -= r*b[k]
		j=k
		while j < n:
			A[i][j]= A[i][j] - r*A[k][j]
			j+=1
		i+=1
	return A,b

def remonte(A,b):
	x = CreerListe(n)        
	x[n-1] = round(b[n-1]/A[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
		x[i]=round(x[i],3)
	return x


def solveSystGauss(A,b):
	global n
	n=len(A)
	k = 0
	arret = 0
	while k!=n and arret!=1:
		i0 = recherchepivot(k,A)
		if i0 == -1:
			arret = 1
		else:
			if i0 == k:
				A,b = elimination(k,A,b)
				k+=1
			else: 
				A,b = permutation(i0,k,A,b)
				A,b = elimination(k,A,b)
				k+=1
	if k==n and A[n-1][n-1]!=0:
		# equation solutions
		x = remonte(A,b)  
		return x
	else:
		# no unique solution
		print("Ce systeme n'admet pas de solution unique")
		return 0


##########################################################
#Fonctions pour la resolution par LU
def eliminationLU(k,A):
	i=k+1
	while i < n:
		r = round((A[i][k]/A[k][k]),3)
		j=k
		while j < n:
			A[i][j] -= r*A[k][j]
			A[i][j]=round(A[i][j],2)
			j+=1
		i+=1
	return A

def descente(A,b):
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= A[i][j]*y[j]
	return y


def factLU(A):
	global n
	n=len(A)
	k=0
	arret=0
	L=CreeMatCar(n)
	while k!=n and arret!=1:
		L[k][k]=1
		if A[k][k] !=0:
			for i in range(k+1,n):
				L[i][k]=round(A[i][k]/A[k][k],2)
			A=eliminationLU(k,A)
			k+=1
		else:
			arret=1
	if arret==0 and A[n-1][n-1]!=0:
		return L,A
	else:
		#print("Les conditions ne sont pas reunies")
		return 0

def solveSystLU(A,b):
	n=len(A)
	L=CreeMatCar(n)
	L=factLU(A)
	if L!=0:
		y=descente(L[0],b)
		x=remonte(L[1],y)
		#print("La solution de votre systeme est \n",x)
		return x
	else:
		#print("Ce systeme ne peut pas etre resolu par la methode LU")
		return 0

####################################################################
#Fonctions Pour la resolution par Cholesky
def factCholesky(A):
	global n
	n=len(A)
	B=CreeMatCar(n)
	try:
		for j in range(n):
			B[j][j]=A[j][j]
			for k in range(j):
				B[j][j] -=B[j][k]*B[j][k]
			B[j][j]= round(m.sqrt(B[j][j]),2)
			for i in range(j+1,n):
				B[i][j]=A[i][j]
				for k in range(j):
					B[i][j]-=B[i][k]*B[j][k]
				B[i][j]=round(B[i][j]/B[j][j],2)
		return B
	except:
		return 0

def descenteChol(L,b):
	global n
	n=len(L)
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
		y[i]/=round((L[i][i]),3)
	return y

def remonteChol(B,b):
	x = CreerListe(n)        
	x[n-1] = round(b[n-1]/B[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= B[j][i]*x[j]
		x[i]/=B[i][i]
		x[i]=round(x[i],3)
	return x

def solveSystCholesky(A,b):
	B=factCholesky(A)
	if B!=0:			
		y=descenteChol(B,b)
		x=remonteChol(B,y)
		return x
	else:
		return 0

#################QR######################
from numpy import *

def solveQR(A,b):
	try:		
		Q,R = linalg.qr(A) # qr decomposition of A
		Qb = dot(Q.T,b) # computing Q^T*b (project b onto the range of A)
		x_qr = linalg.solve(R,Qb)
		return list(x_qr)
	except:
		return 0
#######################################################
##########################Fonction BasicFunction
import time

"""def playError():
		pygame.init()
		son = pygame.mixer.Sound("error.wav")
		son.play()
		time.sleep(1)
		son.stop()"""

#Fonctions de creation de matrices nulles et vecteurs nuls
def CreeMatCar(n):
	return [ [0.0 for j in range(n)] for i in range(n) ]

def CreerListe(n):
	return [0.0 for i in range(n)]

#Fonction qui copie une matrice ds une autre matrice
def CopyMatr(A):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			B[i][j]=A[i][j]
	return B

#Fonction qui copie un vecteur dans un autre vecteur
def CopyVec(b):
	n=len(b)
	v=list()
	for j in range(n):
		v.append(b[j])	
	return v


#Fonction qui teste si un caracter est un nombre 0 1....9"""
def estNombre(carac):
	if carac in ("0","1","2","3","4","5","6","7","8","9"):
		return 1
	else :
		return 0


#Fonction qui teste si dans une chaine il y a autre caractere k un nombre----#ex "az122" return 1 et "1255" return 0
def pasJustqDnbres(chaine):
	for i in range(len(chaine)):
		if i==0:
			if estNombre(chaine[i])==0 and chaine[i] !="-":
				return 1
		else:
			if estNombre(chaine[i])==0:
				return 1
	return 0


print(pasJustqDnbres("-25"))

##################################################################
############################Methode iterative
#from foncNeed import *

"""Resous un systeme avec la methode de gradient"""
def SolveSystIterGrad(A,b,x,err):
	n=len(A)
	r=SomVect(b,ProdVectNbre(-1,ImVect(A,x)))
	d=r
	while NormeVect(r)>err:
		ad=ImVect(A,d)
		t=ProdScal(r,d)/ProdScal(ad,d)
		x=SomVect(x,ProdVectNbre(t,d))
		r=SomVect(r,ProdVectNbre(-t,ad))
		d=r
	for i in range(n):
		x[i]=round(x[i],2)
	return x

"""Resous un systeme avec la methode de gradient conjugue"""
def SolveSystIterGradConj(A,b,x,err):
	r=SomVect(b,ProdVectNbre(-1,ImVect(A,x)))
	d=r
	rp=r
	while NormeVect(r)>err:
		ad=ImVect(A,d)
		t=ProdScal(r,d)/ProdScal(ad,d)
		x=SomVect(x,ProdVectNbre(t,d))
		r=SomVect(r,ProdVectNbre(-t,ad))
		d=SomVect(r,ProdVectNbre((NormeVect(r)/NormeVect(rp)),d))
		rp=r
	return x

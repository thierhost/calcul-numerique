#/usr/bin/env python3
# -*- coding:utf-8 -*-
#Ici on importe la bibliotheque flask ainsi que  l'objet request   
from flask import Flask,request,redirect,url_for,render_template
import fonctions
import myfonctions
from random import randrange
import random
import os
from math import*

app=Flask(__name__)

#definition des routes
@app.route('/')
def index():
	#on redirige vers la  page accueil 
	return render_template("index.html")

@app.route('/inverse',methods=['GET','POST'])
def inverse():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("inverse.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("inverse.html")


@app.route('/gauss',methods=['GET','POST'])
def gauss():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("gauss.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("gauss.html")



@app.route('/resultat_gauss',methods=['GET','POST'])
def resultat_gauss():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		b=[]
		for j in range(dimension):
			ind='b'+str(j)
			b.append(float(request.form[ind]))
		x=fonctions.solveSystGauss(mat,b)
		if(x!=0):
			return render_template("resultat_gauss.html",x=x,dimension=dimension)
		else:
			return render_template("resultat_gauss.html",erreur=0)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("index.html")





@app.route('/resolution_cholesky',methods=['GET','POST'])
def resolution_cholesky():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("resolution_cholesky.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("resolution_cholesky.html")



@app.route('/resultat_cholesky',methods=['GET','POST'])
def resultat_cholesky():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		b=[]
		for j in range(dimension):
			ind='b'+str(j)
			b.append(float(request.form[ind]))
		x=myfonctions.solveSystCholesky(mat,b)
		if(x!=0):
			return render_template("resultat_cholesky.html",x=b,dimension=dimension)
		else:
			return render_template("resultat_cholesky.html",erreur=0)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("index.html")



















@app.route('/resolution_lu',methods=['GET','POST'])
def resolution_lu():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("resolution_lu.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("resolution_lu.html")



@app.route('/resultat_lu',methods=['GET','POST'])
def resultat_lu():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		b=[]
		for j in range(dimension):
			ind='b'+str(j)
			b.append(float(request.form[ind]))
		x=myfonctions.solveSystLU(mat,b)
		if(x!=0):
			return render_template("resultat_lu.html",x=b,dimension=dimension)
		else:
			return render_template("resultat_lu.html",erreur=0)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("index.html")






















@app.route('/cholesky',methods=['GET','POST'])
def cholesky():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("cholesky.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page lu.html 
		return render_template("cholesky.html")
	








@app.route('/result_cholesky',methods=['GET','POST'])
def result_cholesky():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		result=fonctions.factCholesky(mat)	
		if(result!=0):	
			#transposé
			trans=[]
			inter=[]
			for i in range(dimension):
				for j in range(dimension):
					inter.append(result[j][i])
				trans.append(inter)
				inter=[]		
			return render_template("result_cholesky.html",dimension=dimension,matrice=result,transpose=trans)
		else:
			return render_template("result_cholesky.html",erreur=result)		
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("result_cholesky.html")















	
@app.route('/jeu')
def jeu():
	#on redirige vers la  page jeu.html 
	return render_template("jeu.html")

@app.route('/lu',methods=['GET','POST'])
def lu():
	#si on envoi la method POST
	if(request.method=='POST'):
		#on recuperee la taille de la matrice
		taille=int(request.form["taille"])
		return render_template("lu.html",taille=taille)
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page lu.html 
		return render_template("lu.html")
	

@app.route('/result_lu',methods=['GET','POST'])
def result_lu():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(float(request.form[rang]))
			mat.append(inter)
			inter=[]
		result=fonctions.factLU(mat)	
		if(result!=0):
			l=result[0]	
			u=result[1]
			return render_template("result_lu.html",dimension=dimension,matrice=l,u=u)
		else:
			return render_template("result_lu.html",erreur=result)		
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("result_lu.html")



@app.route('/result',methods=['GET','POST'])
def result():
	#si on envoi la method POST
	if(request.method=='POST'):
		#recuperation de la dimension de la matrice
		dimension=int(request.form["dim"])
		#recuperation des elements de la matrice à partir de la taile
		mat=[]
		inter=[]
		for i in range(dimension):
			for j in range(dimension):
				rang='rang'+str(i)+str(j)
				inter.append(eval(request.form[rang]))
			mat.append(inter)
			inter=[]
		inverse=fonctions.inverse(mat,dimension)
		try:
			for i in range(dimension):
				for j in range(dimension):
					inverse[i][j]=round((inverse[i][j]),2)
			return render_template("result.html",dimension=dimension,matrice=inverse)
		except:
			return render_template("result.html",dimension=dimension,erreur=0) 
	#Si c la methode GET	
	if(request.method=='GET'):
		#on redirige vers la  page gauss.html 
		return render_template("result.html")



def crrer(taille):

	b=[]
	inter=[]
	for i in range(taille):
		for j in range(taille):
			inter.append(round(float(random.uniform(-9.0, 9.7)),2))
		b.append(inter)
		inter=[]
	return b		

@app.route('/jouer_matrice',methods=['GET','POST'])
def jouer_matrice():
	if(request.method=='GET'):

		# ici on doit generer 1 matrice puis 4 matrices de la meme taille
		taille=randrange(2,5)
		# On creer ici une matrice A de dimension taille avec des nombres aléatoires
		a=[]
		inter=[]
		for i in range(taille):
			for j in range(taille):
				inter.append(round(float(random.uniform(-9.0, 9.7)),2))
			a.append(inter)
			inter=[]
		#on doi ici calculer linverse de la matrice
		erreur=0
		while(erreur==0):
			inverse=fonctions.inverse(a,taille)
			try:
				for i in range(taille):
					for j in range(taille):
						inverse[i][j]=round((inverse[i][j]),2)
						erreur=1
			except:
				erreur=0 	 	
			# On cree ici 3 matrices ici
		b=crrer(taille)
		c=crrer(taille)
		d=crrer(taille)	
		return render_template("jouer_matrice.html",a=a,inverse=inverse,taille=taille,b=b,c=c,d=d)


app.run(debug= True)
	
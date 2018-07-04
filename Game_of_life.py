#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-


from tkinter import *
from random import *
import time
#global variebel

xmax = 100
ymax = 100
dmax = 5
pilzfeld = [[]]
pilzlebt = [[]]


#as pilzfeld wird ausfallig mit pilzen besetzt

def pilzfeld_initialisieren():
    global pilzfeld
    global pilzlebt

    for i in range(0 , xmax , 1):
        pilzfeld.insert(i , [0])
        pilzlebt.insert(i , [0])
        for j in range( 0 , ymax , 1 ):
            pilzfeld[i].insert(j , 0)
            pilzlebt[i].insert(j , 0 )
    return



def pilzfeld_anpflanzen():
    global pilzfeld
    for i in range(0 , xmax , 1):
        for j in range( 0 , ymax , 1 ):
            k = randint(1 , 5 )
            if k < 4:
                pilzfeld [i] [j] = 1
    return


def pilzfeld_zeichen():
    global pilzfeld

    Feld_mit_Pilzen.delete("pilz") #damit schnelle sein

    #
    for i in range(0 , xmax , 1):
        for j in range( 0 , ymax , 1 ):
            if pilzfeld [i] [j] == 1:
                Feld_mit_Pilzen.create_oval(i * dmax + 2 , j * dmax +2,
                                            i * dmax + dmax + 1 , j * dmax +dmax +1 ,
                                            fill = 'red' , outline='red' ,
                                            tags ="pilz")
            else:
                Feld_mit_Pilzen.create_oval(i * dmax + 2 , j * dmax +2,
                                            i * dmax + dmax + 1 , j * dmax +dmax +1 ,
                                            fill = 'black' , outline='black' ,
                                            tags ="pilz")
    return


#Nachbarn zahlen

def Nachbarzahler(x , y ):
    #zwichen variable
    pilzzahl = 0
    x_min = x - 1
    x_max = x + 1
    y_min = y - 1
    y_max = y + 1

    #Randfrage

    if x == 0:
        x_min = xmax - 1
    elif x == xmax - 1 :
        x_max = 0
    if y == 0:
        y_min = ymax - 1
    elif y == ymax - 1 :
        y_max = 0

    #pilze in der nacharschaft zahlen
    if pilzfeld [x_min] [y_min]:
        pilzzahl += 1
    if pilzfeld [x_min] [y]:
        pilzzahl += 1
    if pilzfeld [x_min] [y_max]:
        pilzzahl += 1
    if pilzfeld [x] [y_min]:
        pilzzahl += 1
    if pilzfeld [x] [y_max]:
        pilzzahl += 1
    if pilzfeld [x] [y_min]:
        pilzzahl += 1
    if pilzfeld [x_max] [y_min]:
        pilzzahl += 1
    if pilzfeld [x_max] [y]:
        pilzzahl += 1
    if pilzfeld [x_max] [y_max]:
        pilzzahl += 1
    return pilzzahl


#lebt die pilze weiter oder entsteht neuer ?

def pilz_leben (x , y):
    global pilzfeld
    lebt = False
    counter = Nachbarzahler(x , y)
    if pilzfeld[x][y]:
        if (counter == 2)|(counter == 3):
            lebt = True
    else:
        if counter == 3:
            lebt = True
    return lebt




#pilzfeld wird auf überleben berechnet und in dem abbild
def pilzfeld_lebt():
    global pilzlebt
    for i in range(0 , xmax , 1):
        for j in range( 0 , ymax , 1 ):
            lebt = pilz_leben(i , j)
            if lebt:
                pilzlebt[i][j] = 1
            else:
                pilzlebt [i][j]=0
    return

#das pilz feld wird aus dem abbild ubertragen

def pilzfeld_setzen():
    global pilzfeld
    for i in range(0 , xmax , 1):
        for j in range( 0 , ymax , 1 ):
            pilzfeld[i][j] = pilzlebt[i][j]

    return




def pilz_spiel(event):
    global xmax
    global ymax
    global dmax

    t1 =time.time()
    print("Anfangzeit : " , t1)

    xmax = anzahl.get()
    ymax = xmax
    dmax = 500 // xmax

    if dmax > 30 :
        dmax = 30

    Feld_mit_Pilzen.config(width = xmax *dmax , height = ymax * dmax )


    pilzfeld_initialisieren()
    pilzfeld_anpflanzen()
    pilzfeld_zeichen()



    schritt_string = zahler.get()
    schritt = int(schritt_string.split("\n")[0])

    i = 0

    while i < (schritt + 1):
        zahler.delete(0,END)
        zahler.insert(END,str(i))
        pilzfeld_lebt()
        pilzfeld_setzen()
        pilzfeld_zeichen()

        Feld_mit_Pilzen.update()
        time.sleep(3/(xmax**2))

        i += 1

    t2 = time.time()
    print("Endezeit :  " , t2 , "und Die Differenz " , t2 - t1 )
    return






#grafik window

root = Tk()
zahler = Entry(root , width=10 )
zahler.bind("<Return>" , pilz_spiel)
zahler.grid(row = 0 , column = 0 , sticky = W+E+S+N )
zahler_label = Label(root, text = "Number Of Units  " )
zahler_label.grid(row=0,column = 1 ,sticky = W+E+S+N)

anzahl = Scale(root , from_=10,to = 100 , length=200 , width = 8 ,
                sliderlength=8,
                resolution = 5 ,
                showvalue = 1,
                orient = HORIZONTAL)
anzahl.grid(row = 0 , column = 2, sticky = W+E )


Feld_mit_Pilzen = Canvas(root , width = xmax * dmax + 2 ,height = ymax * dmax + 2  , bg ='#ffffff')
Feld_mit_Pilzen.grid(row = 1 , columnspan= 3  )










root.mainloop()

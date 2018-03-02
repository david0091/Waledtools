from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk ()
root.title ( "Ticket Reservierung" )
root.configure ( background="#e1d8b2" )
# style
style = ttk.Style ()
style.theme_use ( 'classic' )
style.configure ( 'TLabel', background="#e1d8b2" )
style.configure ( 'TButton', background="#e1d8b2" )
style.configure ( 'TRadiobutton', background="#e1d8b2" )

# Vor Name
ttk.Label ( root, text="Vor Name : " ).grid ( row=0, column=0, padx=3, pady=3 )
VorName = ttk.Entry ( root, width=30, font=('Arial', 10) )
VorName.grid ( row=0, column=1, columnspan=2, pady=10 )
# Nach Name
ttk.Label ( root, text="Nach Name : " ).grid ( row=1, column=0, padx=3, pady=3 )
NachName = ttk.Entry ( root, width=30, font=('Arial', 10) )
NachName.grid ( row=1, column=1, columnspan=2, pady=10 )
# Handy Nummer
ttk.Label ( root, text="Handy Nummer : " ).grid ( row=3, column=0, padx=3, pady=3 )
HandyNummer = ttk.Entry ( root, width=30, font=('Arial', 10) )
HandyNummer.grid ( row=3, column=1, columnspan=2, pady=10 )

# Email Addresse
ttk.Label ( root, text="Email Addresse : " ).grid ( row=4, column=0, padx=3, pady=3 )
Email = ttk.Entry ( root, width=30, font=('Arial', 10) )
Email.grid ( row=4, column=1, columnspan=2, pady=10 )

# Geschliecht
ttk.Label ( root, text="Geschliecht : " ).grid ( row=5, column=0 )
Geschlicht = StringVar ()
ttk.Radiobutton ( root, text="Male", variable=Geschlicht, value="Male" ).grid ( row=5, column=1 )
ttk.Radiobutton ( root, text="Famle", variable=Geschlicht, value="Famle" ).grid ( row=5, column=2 )
# Nachriecht
ttk.Label ( root, text="Nachricht: " ).grid ( row=6, column=0 )
Nachricht = Text ( root, width=20, height=10, font=('Arial', 16) )
Nachricht.grid ( row=6, column=1, columnspan=2 )

# buttons

buSubmit = ttk.Button ( root, text="Submit" )
buSubmit.grid ( row=7, column=2 )
buList = ttk.Button ( root, text="List Res." )
buList.grid ( row=7, column=3 )
#author
ttk.Label ( root, text="All Right is for Evry one Waleed Neukirchen-vluyn,Germany : " ).grid ( row=8, column=0, padx=3, pady=3 )

def BuSaveData():
    print("Vor Name : {}".format(VorName.get()))
    print("Nach Name : {}".format(NachName.get()))
    print("Handy Nummer : {}".format(HandyNummer.get()))
    print("Email : {}".format(Email.get()))
    print("Geschliecht : {}".format(Geschlicht.get()))
    print("Comments : {}".format(Nachricht.get(1.0,'end')))
    VorName.delete ( 0, 'end' )
    NachName.delete ( 0, 'end' )
    HandyNummer.delete ( 0, 'end' )
    Email.delete ( 0, 'end' )
    Nachricht.delete( 1.0, 'end' )


def BuListData():
    # TODO:show  orders
    print ( 'Is Under The Test Created at 01.03.2018 Neukirchen Vluyn' )
    print("I Will Connect Him To Data Basis in The next day Or when I get Ausbildung in köln")


buSubmit.config ( command=BuSaveData () )
buList.config ( command=BuListData () )

root.mainloop ()

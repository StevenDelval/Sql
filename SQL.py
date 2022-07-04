import sqlite3

connexion = sqlite3.connect("Chinook_Sqlite.sqlite")
curseur = connexion.cursor()

curseur.execute("""
                SELECT * from Artist 
""" )

for ligne in  curseur.fetchall() :
    print(ligne,end="\n")
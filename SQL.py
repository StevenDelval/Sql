import sqlite3

connexion = sqlite3.connect("Chinook_Sqlite.sqlite")
curseur = connexion.cursor()

'''
curseur.execute("""
                SELECT Name from Artist ; 
""" )

for ligne in  curseur.fetchall() :
    print(ligne,end="\n")
'''


'''
curseur.execute("""
                SELECT Name,Milliseconds  from Track WHERE Milliseconds >500000;
""" )

for ligne in  curseur.fetchall() :
    print(ligne,end="\n")
'''

""" curseur.execute('''
                SELECT Genre.Name,Track.Name,Milliseconds  from Track JOIN Genre ON Genre.GenreID = Track.GenreID  WHERE Milliseconds >=300000 and Genre.Name ="Rock";
''' )

for ligne in  curseur.fetchall() :
    print(ligne,end="\n") """

curseur.execute("""
                SELECT PlaylistId,COUNT(TrackId) From PlaylistTrack
                GROUP BY  PlaylistId

""" )
count=0
for ligne in  curseur.fetchall() :
    print(ligne,end="\n")
    count +=1
print(count)

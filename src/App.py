import mysql.connector
import csv
import pandas as pd
from csv import DictReader

#create a connection to testing database
cnx = mysql.connector.connect(
    user="root", password="innebandy21", host="127.0.0.1", database="pa2")

mycursor = cnx.cursor(buffered=True)


#Read the species.csv file and every NA object is replaced by 0
#if a row contains 'indefinite then change the value to 0. 

nba2 = pd.read_csv("movies.csv", index_col=False)
nba2.fillna('0', inplace=True)
nba2.replace(to_replace ='indefinite', value ='0', inplace=True)
nba2.head()

nba3 = pd.read_csv("stars.csv", index_col=False)
nba3.fillna('0', inplace=True)
nba3.replace(to_replace ='indefinite', value ='0', inplace=True)
nba3.head()

nba4 = pd.read_csv("producers.csv", index_col=False)
nba4.fillna('0', inplace=True)
nba4.replace(to_replace ='indefinite', value ='0', inplace=True)
nba4.head()
#make action towards the server
#mycursor.execute("create database pa2")
#mycursor.close()
#mycursor.execute("CREATE TABLE producers (name VARCHAR(40), age int, gender VARCHAR(50), primary key(name))") #Creating planets table

#mycursor.execute("CREATE TABLE stars (name VARCHAR(40), age int, gender VARCHAR(50), primary key(name))") #Creating planets table


#for i,row in nba3.iterrows():
      #sql = "INSERT INTO pa2.stars (stars.id, stars.name, stars.age, stars.gender) VALUES (%s, %s, %s, %s)"
      #mycursor.execute(sql, tuple(row))
      #cnx.commit()
#print ('done')

#for i,row in nba3.iterrows():
       #sql = "INSERT INTO pa2.stars VALUES (%s, %s, %s)"
       #mycursor.execute(sql, tuple(row))
       #cnx.commit()
#mycursor.close()
#print ('done')

#for i,row in nba4.iterrows():
       #sql = "INSERT INTO pa2.producers VALUES (%s, %s, %s)"
       #mycursor.execute(sql, tuple(row))
       #cnx.commit()
#mycursor.close()
#print ('done')

#mycursor.execute("CREATE TABLE Species (name VARCHAR(40), classification VARCHAR(50), designation VARCHAR(50), average_height int, skin_colors VARCHAR(50), hair_colors VARCHAR(50), eye_colors VARCHAR (50), average_lifespan int, language VARCHAR(50), homeworld VARCHAR(50), primary key(name))") #Creating species table 

#for i,row in nba2.iterrows():
       #sql = "INSERT INTO testing.species VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
       #mycursor.execute(sql, tuple(row))
       #cnx.commit()
#mycursor.close()
#print ('done')


menu_options = {
    1: 'List all action movies: (1)',
    2: 'Get starname for the movie star wars: (2)',
    3: 'List movies all movies and there category, using join (3)',
    4: 'GROUP BY movies, alfabeth: (4)',
    5: 'Aggregation, count movies: (5)',
    6: 'Create view (6)',
    7: 'Exit'
}

def Querymenu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )


def option1():
  sql = "SELECT movies.title, category.category_name FROM movies JOIN category ON category.id = movies.category_id where movies.category_id = 1"
  mycursor.execute(sql)
  records = mycursor.fetchall()
  
  #present the retrived data 
  for row in records:
        print("Movie = ", row[0], )
        print("Genre = ", row[1], "\n")
  exit = input('Enter any key to go to the main menu: ')
  
def option2():
  sql2 = "SELECT movies.title, stars.name FROM movies JOIN stars on movies.star_id = stars.id WHERE movies.title = 'star wars'"
  mycursor.execute(sql2)
  records = mycursor.fetchall()
  
  #present the retrived data 
  for row in records:
        print("Movie = ", row[0], )
        print("Star = ", row[1], "\n")
  exit = input('Enter any key to go to the main menu: ')
  
  
def option3():
  sql = "SELECT movies.title, category.category_name FROM movies JOIN category on movies.category_id = category.id "
  mycursor.execute(sql)
  records = mycursor.fetchall()
  
  #present the retrived data 
  for row in records:
        print("Name = ", row[0], )
        print("rotation_period = ", row[1], "\n")
  exit = input('Enter any key to go to the main menu: ')


def option4():
  sql2 = ("SELECT movies.title, movies.year, movies.length FROM movies GROUP BY movies.title")
  mycursor.execute(sql2)
  records = mycursor.fetchall()
  
  for row in records:
        print("Title = ", row[0] )
        print("year = ", row[1])
        print("length  = ", row[2], "\n") 
  exit = input('Enter any key to go to the main menu: ')
     

def option5():
  sql3 = ("SELECT COUNT(movies.title) FROM movies")
  mycursor.execute(sql3)
  records = mycursor.fetchall()
  
  for row in records:
        print("there is = ", row[0], " movies in the database", "\n") 
  exit = input('Enter any key to go to the main menu: ')
  
def option6():
  #sql4 = ("CREATE VIEW test_average_moviestar AS SELECT stars.name FROM stars where stars.age > (SELECT AVG(stars.age) FROM stars)")
  sql4 = ("SELECT * FROM test_average_moviestar ")
  mycursor.execute(sql4)
  records = mycursor.fetchall()
  
  for row in records:
        print(row, "\n") 
  exit = input('Enter any key to go to the main menu: ')
  
  
  
#create a menu
if __name__=='__main__':
    while(True):
        Querymenu()
        option = ''
        try:
            option = int(input('Select and press enter: '))
        except:
            print('Wrong input. Try again ...')
        #Check what choice the user selected and visit the function
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
           print('Bye bye')
           exit()
        else:
            print('Please enter a number between 1 and 5.')

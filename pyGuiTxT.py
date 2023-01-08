import mysql.connector
from mysql.connector import Error

def polacz():
    try:
        conn = mysql.connector.connect(user='root_main',password='password_strong_1',host='localhost',database='planner')
        if conn.is_connected():
            print('Nawiązano połączenie !')

    except Error as e:
        print("Wystąpił błąd poadczas łączenia z MySQL", e)


def main():
    decyzja = ''
    
    print(' Witam w programie Planner, zapraszam do interakcji !')
    print(' 1 - sprawdzenie połączenia z bazą danych PLANNER w technologii MySQL')
    print(' 2 - sprawdzenie i wyświetlenie plannera')
    print(' 3 - wprowadzenie danych do plannera')
    
    decyzja = input(' Którą opcję z menu wybierasz ? ')
    while(decyzja != ' '):
        if(decyzja == '1'):
            polacz()
        elif(decyzja == '2'):
            conn = mysql.connector.connect(user='root_main',password='password_strong_1',host='localhost',database='planner')
        
            sql_select_Query = "select * from szczegoly"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            print("Liczba wszystkich pozycji w Planerze: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                print(' Numerek wpisu to ', row[0])
                print("NAGŁE I WAŻNE - ", row[1])
                print("NIE NAGŁE, LECZ WAŻNE - ", row[2])
                print("NAGŁE, LECZ NIE ISTOTNE - ", row[3])
                print("NIE NAGŁE I NIE ISTOTNE - ", row[4], "\n")
         
        elif(decyzja == '3'):
            
            conn = mysql.connector.connect(user='root_main',password='password_strong_1',host='localhost',database='planner')
        
            numerek = input(' Podaj numerek pod którym zostanie zapisany wpis : ')
            txt1 = input(' Podaj to co NAGŁE I WAŻNE : ')
            txt2 = input(' Podaj to co NIE NAGŁE, LECZ WAŻNE : ')
            txt3 = input(' Podaj to co NAGŁE, LECZ NIE ISTOTNE : ')
            txt4 = input(' Podaj to co NIE NAGŁE I NIE ISTOTNE : ')
        
            cursor = conn.cursor()
            sql_select_Query = "INSERT INTO `szczegoly` (`ID`, `URGENT_IMPORTANT`, `NOT_URGENT_IMPORTANT`,`URGENT_UNIMPORTAN`, `NOT_URGENT_UNIMPORTANT`) VALUES (%s, %s, %s, %s, %s);"
            
            val = (numerek,txt1,txt2,txt3,txt4)
            
            cursor.execute(sql_select_Query,val)
            
            conn.commit()
            print(cursor.rowcount, ' Pozycja planera została dodana !')
            
        decyzja = input(' Którą opcję z menu wybierasz ? ')
    
    
if __name__ == "__main__":
    main()
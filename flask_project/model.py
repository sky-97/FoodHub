import sqlite3


def init_db():
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM swiggytable")
        c.execute("SELECT * FROM zomatotable")
        c.execute("SELECT * FROM ubereatstable")
    except:
        c.execute("""create table swiggytable (name TEXT,price REAL)""")
        c.execute("""create table zomatotable (name TEXT,price REAL)""")
        c.execute("""create table ubereatstable (name TEXT,price REAL)""")
    conn.commit()
    conn.close()

def search_location(search):
    search = str(input())
    if search == 'biryani':
        conn=sqlite3.connect('food.db')
        c=conn.cursor()
        swiggy_results=c.execute("SELECT * FROM swiggytable;")
        swiggy_list=[]
        for item in swiggy_results:
            swiggy_list.append([item[0],item[1]])
        zomato_results=c.execute("SELECT * FROM zomatotable;")
        zomato_list=[]
        for item in zomato_results:
            zomato_list.append([item[0],item[1]])
        ubereats_results=c.execute("SELECT * FROM ubereatstable;")
        ubereats_list=[]
        for item in ubereats_results:
            ubereats_list.append([item[0],item[1]])
        return swiggy_list, zomato_list, ubereats_list
    else:
        print("food not avilable")
def show():
    conn=sqlite3.connect('food.db')
    c=conn.cursor()
    swiggy_results=c.execute("SELECT * FROM swiggytable;")
    swiggy_list=[]
    for item in swiggy_results:
        swiggy_list.append([item[0],item[1]])
    zomato_results=c.execute("SELECT * FROM zomatotable;")
    zomato_list=[]
    for item in zomato_results:
        zomato_list.append([item[0],item[1]])
    ubereats_results=c.execute("SELECT * FROM ubereatstable;")
    ubereats_list=[]
    for item in ubereats_results:
        ubereats_list.append([item[0],item[1]])
    return swiggy_list, zomato_list, ubereats_list

def get_details(search):
    conn = sqlite3.connect("food.db")
    c = conn.cursor()
    swiggy_rest = c.execute("SELECT [name],[price] FROM swiggytable Where [name]=(:uname)",{'uname':search}).fetchall()
    list_swiggy = []
    for item in swiggy_rest:
        list_swiggy.append([item[0],item[1]])
    zomato_rest = c.execute("SELECT [name],[price] FROM zomatotable Where [name]=(:uname)",{'uname':search}).fetchall()
    list_zomato = []
    for item in zomato_rest:
        list_zomato.append([item[0],item[1]])
    uber_rest = c.execute("SELECT [name],[price] FROM ubereatstable Where [name]=(:uname)",{'uname':search}).fetchall()
    list_uber = []
    for item in uber_rest:
        list_uber.append([item[0],item[1]])
    return list_swiggy, list_zomato, list_uber
if __name__=='__main__':
    init_db()

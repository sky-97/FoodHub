![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/pinterest_profile_image.png)

# FoodHub


## FoodHub Application

Foodhub is a food search with an extensive price comparison. The prices shown come from various food ordering  websites like Zomato, Swiggy, Ubereats. This means that while users decide on foodhub which food ordering website best suits their needs, the ordering process itself is completed through the booking sites (which are linked to our website).


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites

What things you need to install the software and how to install them

``` pip3 install flask ```

###### You just need to install flask library and for database i am gonna use sqlite3 no need to install sqlite module It is included in the standard library (since Python 2.5)

## File Structure

|FoodHub──

    |flask_project──
    
                ├── app.py
                
                ├── food.db
                
                ├── model.py
                
                |
                └── templates
                
                ├── base.html
                
                ├── food.html
                
                └── home.html 
   

##### app.py is a controller in which all logics are there, model.py is a model file in which all database insert create and querry codes are there, temaplates is a folder inside which there is view files.

## Running the tests

``` python app.py ```

As i am following MVC Model-View-Controller framework MVC Controllers are responsible for controlling the flow of the application execution. When you make a request (means request a page) to MVC application, a controller is responsible for returning the response to that request, Here app.py is my controller thats why i am runing app.py file

* <img src="flask_project/Screenshot from 2019-05-08 11-10-11.png" alt="alt text" width="600">

``` http://127.0.0.1:5000/home ```

*  Add this url to your Browser
    
### This is  home page of our website

   ![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/flask_project/Screenshot%20from%202019-05-09%2019-29-14.png)

### Search for food
    * type "Biryani' in search 
    
  ![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/flask_project/Screenshot%20from%202019-05-09%2019-29-30.png)
    
    
### Compare food

    * there is button where you can select restaurants 
    
![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/flask_project/Screenshot%20from%202019-05-09%2019-29-37.png)

### Select restaurant
    
![alt text](https://github.com/akashcoc/FoodHub/blob/master/flask_project/Screenshot%20from%202019-05-09%2019-29-43.png?raw=true)

### Side by Side comparison 
    
    * Zomato, Swiggy and ubereats price shown, Here in example Paradise restaurant biryani price is different, now users can select which is ever have good deal
    
![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/flask_project/Screenshot%20from%202019-05-09%2019-29-53.png)

### Best deal

* Zomato showing best deal, so click on zomato

![alt text](https://raw.githubusercontent.com/akashcoc/FoodHub/master/flask_project/Screenshot%20from%202019-05-09%2019-30-02.png)

## Built With
 
 [Flask](http://flask.pocoo.org/)
 
 [SQLite](https://www.sqlite.org/index.html)
 
 [MVC](https://flask-diamond.readthedocs.io/en/latest/model-view-controller/)
 
 [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 
 [Bootstrap](https://getbootstrap.com/)




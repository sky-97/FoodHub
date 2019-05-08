![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOSKgCL02z_NzBLQCUxZuHglfbS7dlPgN9lc-fn8yc5qdm9gt8)

# FoodHub


## FoodHub Application

Foodhub is a food search with an extensive price comparison. The prices shown come from various food ordering  websites like ZOMATO, SWIGGY, Ubereats. This means that while users decide on foodhub which food ordering website best suits their needs, the ordering process itself is completed through the booking sites (which are linked to our website).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites

What things you need to install the software and how to install them

``` pip3 install flask ```

###### You just need to install flask library and for database i am gonna use sqlite3 no need to install sqlite module It is included in the standard library (since Python 2.5)

## File Structure

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

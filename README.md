                                                      Electrical Load Management System

A Python-based tool that calculates the total connected electrical load using appliance data stored in an ANSI SQL (SQLite) database. The system computes total wattage, required current, and recommends a suitable MCB rating. Built using basic OOP principles, SQLite, and a clean modular structure.

Features:

Add appliances with wattage and quantity

Stores all data using ANSI SQL (SQLite)

Calculates total connected load (in Watts)

Computes required current (in Amperes)

Suggests the appropriate MCB rating

Simple and beginner-friendly OOP design

Modular and easy-to-understand code structure


Tech Stack:

Python

SQLite (ANSI SQL)

Object-Oriented Programming (OOP)

How to Run:

1. Install Python on your system

2. Place project.py and electrical_load.db in the same folder

3. Run the program
    -- python project.py
4. Follow the on-screen menu to add appliances, view data, and calculate load  

Project Structure:

 Electrical-Load-Management-System/
│── project.py        # Main Python application
│── electrical_load.db  # SQLite database storing appliance data
│── README.md         # Project documentation

About the Project:

This project demonstrates how Python, SQL, and OOP can be integrated to solve a real-world electrical engineering problem: calculating connected load and selecting proper protection devices. It is designed to be simple, practical, and suitable for beginner portfolios.  

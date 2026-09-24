Before running the code, please paste the following on your MySQL Unicode client:


create database blackmamba; use blackmamba; create table credentials(username varchar(15) primary key, password varchar(15), email varchar(60), address varchar(80), phoneno varchar(80), ccno varchar(19), expirydate varchar(6), cvv varchar(4)); create table scores(username varchar(15) primary key,georgeruns int, poppeye int, mambaio int);

IMPORTANT !!!
DON'T FORGET TO CHANGE THE PASSWORD IN THE BLACKMAMBA.py FILE FOR YOUR MYSQL CONNECTOR TO SUCCESSFULLY CONNECT YOUR MYSQL



Credits
The development of Black Mamba Arcade was a collaborative effort by a dedicated team. Arun Jose skillfully handled both the backend and frontend, designing a cohesive user interface that provides an intuitive and enjoyable user experience. Kavin Senthilkumar contributed to the creation of engaging arcade games, enhancing the application's entertainment value. Aditya Menon focused on implementing the game logic and establishing seamless MySQL connectivity, ensuring efficient data management and performance.  Together, their combined efforts brought Black Mamba Arcade to life, creating a valuable tool for stress relief and financial education.

Have fun, enjoy and keep coding :))
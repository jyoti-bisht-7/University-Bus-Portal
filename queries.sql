create database bus;

use bus;

create table student(
  student_id int primary key,
  password varchar(20));

insert into student student_id values (230104702);

insert into student (student_id) values (230121625);

insert into student (student_id) values (230121875);

create table bus_card_details(
  Name varchar(20),
  Student_ID  int,
  Father_name varchar(20),
  Course varchar(10),
  Route varchar(50),
  Phone_no varchar(10),
  Bus_no int,
  Seat_no int));
  



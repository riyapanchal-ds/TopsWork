 /* 1. Retrieve all records from the Students table.
2. Display only the names and ages of students.
3. Show details of students who live in Ahmedabad.
4. List all students with grade 'A'.
5. Find students who scored more than 80 marks.
6. Display students aged between 18 and 21.
7. List students who are from Mumbai and have marks above 70.
8. Find students whose names start with the letter 'A'.
9. Display all students sorted by marks in descending order.
10. List students sorted by age in ascending order.
11. Show students sorted by city and then by marks (highest first).*/


create database students
use students
create table stud(
id int primary key,
name varchar(20),
age int,
city varchar(20),
marks int(5) ,
grade varchar(10)
);

insert into stud(id,name,age,city,marks,grade)
values (1,'riya',22,'ahemedabad',80,'A'),
(2,'mital',25,'amreli',90,'B'),
(3, 'jiya', 21, 'ahemedabad', 92, 'C'),
(4, 'arjun', 18, 'baroda', 67, 'D'),
(5, 'anjali', 22, 'mumbai', 88, 'A'),
(6, 'rahul', 20, 'surat', 75, 'B'),
(7, 'akash', 19, 'mumbai', 82, 'C');

select* from stud;

select name,age from stud;

select* from stud where city = 'ahemedabad';

select* from stud where grade = 'A';

select* from stud where marks > 80;

select* from stud where age between 18 and 21;

select* from stud where city = 'mumbai' and marks > 70;

select* from stud where name like 'a%';

select* from stud order by marks DESC;

select* from stud order by age ASC;

select* from stud order  by city ASC, marks DESC;

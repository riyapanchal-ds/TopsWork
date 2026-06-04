create database department
use department
create table department (
did int primary key,
dname varchar(20)
);
select* from department;
create table employe (
eid int primary key auto_increment,
ename varchar(20),
email varchar(20),
salary int ,
c_no decimal(11),
dept_id int,
foreign key(dept_id) references department(did)
);
insert into department value(101,'sales'),
(102,'software'),
(103,'admin'),
(104,'production');

insert into employe(ename,email,salary,c_no,dept_id)
 values('kashish','kashish@gmail.com',123445,8544888383,101),
 ('tamanna','tamanna@gmail.com',234433,878888332,102),
 ('bhavesh','bhavesh@gmail.com',584844,4949594433,101);
 
 select * from department;
 select * from employe;
 
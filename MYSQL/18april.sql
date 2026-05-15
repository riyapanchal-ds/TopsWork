create database employee
use employee
create table employee(eid int primary key auto_increment,
ename varchar (20),
salary int (10)
);
alter employee city varchar(20);
insert into employee(ename,salary,city) values('riya',20000),
('mital',30000),
('jenish',23000),
('gopi',28000);
update employee set city='ahmedabad' where eid=4;
update employee set city='gandhinagar' where eid=3;
update employee set city='baroda' where eid=2;
update employee set city='surat' where eid=1;
 select* from employee;
 
 select* from employee where salary between 20000 and 25000;
 
 select* from employee order by ename;  -- ascending order
  select* from employee order by ename desc;   -- descending order
 
 
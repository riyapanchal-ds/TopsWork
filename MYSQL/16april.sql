create database student
use student

create table customer1(cid int,
cname varchar(20),
c_no int(10)
);

describe customer1;

alter table customer1 add email varchar(20);



-- drop table customer1;

insert into customer1(cid,cname,c_no,email) 
values(1,'hani',23456,'hani@gmail.com'),
(222,'riya',76543,'riya@gmail.com'),
(123,'kavya',65432,'kavya123@gmail.com');

select* from customer1;

update customer1 set email='hani123@gmail.com' where cid=1;
select* from customer1;

delete from customer1 where cid=222;
select *from customer1;
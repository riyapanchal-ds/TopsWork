create table emplpoyee(
empid integer primary key,
ename text not null,
dept text not null
);
insert into employee values (0001, 'clark', 'sales');
insert into employee values(0002, 'dave' , 'accounting');
insert into employee values(0003 , 'ava' ,'sales');

select * from employee;
select concat(name,'',dept)as 'name-dept' from employee;
 
select name, length(name) as ' total no of letters',upper(name) from employee;

select * from employee;
select subst 
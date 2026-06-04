Create database course
use course
create table course(
c_id int primary key,
course_name varchar(20),
fees decimal(5,2)
);


-- Create Table of Student Details
create table student_details(
std_id int primary key,
student_name varchar(20),
address varchar(20),
std_con_no decimal(10)
);


-- Create Table of Enroll Details
create table enroll_details(
enrol_id int,
course_id int,
student_id int,
enroll_date date,
foreign key (course_id) references course(c_id),
foreign key (student_id) references student_details(std_id)
);


-- create table for department
create table edu_department(
dept_id int primary key,
dept_name varchar(20)
);

-- create table for emplloyees
create table dept_employees(
emp_id int primary key,
emp_name varchar(20),
emp_email varchar(20),
emp_salary decimal(10),
join_date date,
did int,
foreign key (did) references edu_department (dept_id)
);


alter table course modify fees decimal(10,2);

-- Insert Course Details
insert into course (c_id, course_name, fees) values
(101, 'Data Science', 150000),
(102, 'Data Analyitcs', 85000),
(103, 'BackEnd Developer', 65000),
(104, 'FrontEnd Developer', 50000),
(105, 'Graphic Designer', 75000);


select * from course;
insert into student_details (std_id, student_name, address, std_con_no) values
(101, 'Krunal', 'Ahmedabad', 9924983016);

-- insert Student Details
insert into student_details (std_id, student_name, address, std_con_no) values
(102, 'Kavya', 'Mehsana', 9924983035),
(103, 'Netra', 'Ranip', 9924981035),
(104, 'Bhavesh', 'Rajasthan', 9924981012),
(105, 'Riya', 'Idar', 9924981015);

select * from student_details;

alter table enroll_details add primary key (enrol_id);


-- Insert Enrollment Details
insert into enroll_details (enrol_id ,course_id, student_id,enroll_date) values
(1,102, 101, '2026-01-01'),
(2,102, 102, '2026-01-01'),
(3,101, 103, '2026-01-01'),
(4,104, 104, '2026-02-01'),
(5,103, 105, '2026-01-01');
select * from enroll_details;

select enrol_id, student_name, course_name;

-- insert Department Details
insert into edu_department (dept_id , dept_name) values
(1,'Admission'),
(2,'Counsellor'),
(3,'Management'),
(4,'Faculty'),
(5,'Accounts');

select * from enroll_details;

-- Insert Employee Details
insert into dept_employees 
(emp_id, emp_name, emp_email, emp_salary, join_date, did) 
values
(1, 'Krunal', 'krunal@gmail.com', 35000, '2024-01-10', 1),
(2, 'Kavya', 'kavya@gmail.com', 30000, '2024-02-15', 2),
(3, 'Netra', 'netra@gmail.com', 32000, '2024-03-01', 3),
(4, 'Mahek', 'mahek@gmail.com', 28000, '2024-01-20', 4),
(5, 'Masum', 'masum@gmail.com', 27000, '2024-02-10', 5),
(6, 'Bhavesh', 'bhavesh@gmail.com', 40000, '2024-03-12', 1),
(7, 'Shubh', 'shubh@gmail.com', 29000, '2024-01-25', 2),
(8, 'Mahesh', 'mahesh@gmail.com', 31000, '2024-02-28', 3),
(9, 'Jenish', 'jenish@gmail.com', 33000, '2024-03-05', 4),
(10, 'Riya', 'riya@gmail.com', 26000, '2024-01-18', 5),
(11, 'Sneha', 'sneha@gmail.com', 34000, '2024-02-22', 1),
(12, 'Samiskha', 'samiskha@gmail.com', 30000, '2024-03-08', 2),
(13, 'Divya', 'divya@gmail.com', 28000, '2024-01-30', 3),
(14, 'Amit', 'amit@gmail.com', 36000, '2024-02-12', 4),
(15, 'Rahul', 'rahul@gmail.com', 37000, '2024-03-15', 5);

select * from dept_employees;

-- fetch employee details with


-- fetch no of employee in each department
 select count(emp_id)as 'np of emp',dept_name
 from dept_employees.dept_id=
 where ;
 
 -- fetch avg salary of employee in each dept
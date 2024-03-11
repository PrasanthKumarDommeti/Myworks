-- Write your MySQL query statement below
-- Here there is a one solution using joins
select e.name "Employee" from employee e join employee m where  e.managerid = m.id and m.salary < e.salary;
-- Using self join
select e.name "Employee" from employee e , employee m where  e.managerid = m.id and m.salary < e.salary;

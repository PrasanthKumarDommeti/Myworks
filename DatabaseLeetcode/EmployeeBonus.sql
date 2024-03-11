--Simple problem but use only left join the run time will be high and using 
--the left outer join the time will be reduced than the normal left join
select  e.name,b.bonus from employee e left outer join  bonus b on e.empid=b.empid where  b.bonus is null or b.bonus<1000;
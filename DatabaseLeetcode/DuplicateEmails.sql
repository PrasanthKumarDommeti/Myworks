--Simple Group by problem
select email "Email" from person group by email having count(email)>1;
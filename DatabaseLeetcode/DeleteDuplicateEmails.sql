--This is the query about the cross join with the same table
delete e1 from person e1,person e2 where e1.id>e2.id and e1.email = e2.email;
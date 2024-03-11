--MySQL query using the subquery to get result
select c.name "Customers" from customers c where c.id not in (select customerid from orders);
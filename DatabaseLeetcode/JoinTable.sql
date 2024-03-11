select p.firstName ,p.lastName, a.city, a.state from person p left join address a on p.personid =  a.personid;
-- This can be solved by my self
-- Optimised Solution with "using" keyword
SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId)

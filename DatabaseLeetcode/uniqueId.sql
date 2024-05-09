--The unique ids must be identified by matching the elements
select eu.unique_id, e.name from employees e
left join EmployeeUNI eu on eu.id = e.id;
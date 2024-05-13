
select a.machine_id , 
round((select avg(a1.timestamp) from activity a1 where a1.activity_type like 'end' and a1.machine_id = a.machine_id)
-
(select avg(a1.timestamp) from activity a1 where a1.activity_type like 'start' and a1.machine_id = a.machine_id),3) 'processing_time'
 from activity a group by a.machine_id;
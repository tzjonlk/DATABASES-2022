-- Query 3.1 --

SELECT program_name FROM program;

SELECT project_title FROM project;

SELECT researcher.rfirst_name, researcher.rlast_name
FROM project natural join researcher
WHERE project_title = ()
AND starting_date >= ()
AND starting_date <= ()
AND ending_date >= ()
AND ending_date <= ();

SELECT researcher.rfirst_name, researcher.rlast_name, project_title
FROM corporate_member natural join project natural join researcher
WHERE corporate_member.cfirst_name = ()
AND corporate_member.clast_name = ();


-- Query 3.2 -- 

SELECT project_title 
FROM project 
WHERE researcher_id = ();

SELECT DISTINCT project_title 
FROM project 
WHERE org_name = ();


-- Query 3.3 --

SELECT project_title, researcher.rfirst_name, researcher.rlast_name
FROM project natural join researcher
WHERE (YEAR(CURRENT_TIMESTAMP) - YEAR(starting_date) <= 1)
AND field_name = ();

-- Query 3.6 --

SELECT researcher.rfirst_name, researcher.rlast_name, researcher.date_of_birth, (select count(project_title) from project natural join researcher )
FROM project natural join researcher
WHERE (YEAR(CURRENT_TIMESTAMP) - YEAR(date_of_birth) < 40 AND ending_date > curdate());






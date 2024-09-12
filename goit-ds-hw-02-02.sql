--1
SELECT *
FROM tasks
WHERE user_id = '20'
;

--2
SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE status = 'new')
;
 
--3
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE status = 'in progress')
WHERE id = 5
;
 --4

SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks)
; 
--5
INSERT INTO tasks(title, description, status_id, user_id)
VALUES('test_task', 'make test task', 1, particular_user)
WHERE user_id = (SELECT id as particular_user from users WHERE fullname  = 'Timothy Frazier')
;
--6
SELECT *
FROM tasks
WHERE status_id NOT IN (SELECT id FROM status WHERE status = 'completed')
;
 
--7

SELECT *
FROM users
WHERE email LIKE 'robyn19@example.com'
;

UPDATE users
SET fullname = 'Anastasiia Smirnova'
WHERE fullname= "Michael Morgan"
;

SELECT status_id, COUNT(id)
FROM tasks
GROUP BY status_id
;
SELECT *
FROM tasks INNER JOIN users ON tasks.user_id = users.id
WHERE email LIKE '%@example.com'
;

SELECT *
FROM tasks 
WHERE description IS NULL
;

SELECT fullname, title, description
FROM tasks INNER JOIN users ON tasks.user_id = users.id 
WHERE status_id = (SELECT id FROM status WHERE status = 'in progress')
;

SELECT fullname, COUNT(tasks.id)
FROM users LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id
;
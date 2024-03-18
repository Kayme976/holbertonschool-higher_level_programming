-- Lists all cities conatined in the datbase hbtn_0d_usa
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
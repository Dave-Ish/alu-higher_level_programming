-- Lists all cities contained in hbtn_0d_usa with their state names
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

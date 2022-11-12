# Write your MySQL query statement below
SELECT Person.firstName, Person.lastname, Address.city, Address.state
FROM Person LEFT JOIN Address On Person.personId = Address.personId;
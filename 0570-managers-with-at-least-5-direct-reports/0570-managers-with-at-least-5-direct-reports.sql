# Write your MySQL query statement below
Select name
From Employee
Where id in (
    Select  managerId
    From Employee
    Group by managerId
    Having count(managerId) >= 5
);


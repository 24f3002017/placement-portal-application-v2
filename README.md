# placement-portal-application-v2
A role-based web application that streamlines campus recruitment by connecting institutes, companies, and students on a centralized placement portal.

Milestone 0
1) Initial setup

Milestone 1

In this part I made database tables. I created user, student, company, jobposition, application and placements. Also defined relationships between those models. and also pre created ADMIN programmatically.

1) made tables using sqlalchemy
2) defined relationships
3) pre created ADMIN programmatically

Milestone 2

In this part I implemented authentication and role-based access. Students and companies can register, users can log in using JWT authentication, and they are redirected to their respective dashboards based on their roles.

1) implemented JWT authentication
2) student registration
3) company registration
4) role-based login
5) company login restricted until admin approval
6) pre-defined admin login


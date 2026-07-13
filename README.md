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

Milestone 3

In this part I implemented the complete admin management module. Admin can manage students, companies, job postings, applications and placements. I also added account management features like approve, reject, activate, deactivate, blacklist and delete.

1) admin dashboard with statistics
2) student management
3) company management
4) job management
5) application management
6) placement management
7) company approval and rejection
8) student activate, deactivate, blacklist and delete
9) company activate, deactivate, blacklist and delete
10) job approval, rejection and deletion
11) search and filter functionality
12) inactive and blacklisted users cannot log in
13) protected routes verify user account status

Issues Encountered and Fixes

1) Company approve/reject buttons were not working due to missing API integration.
   Fixed by creating backend routes and connecting them with Axios.

2) Delete operation failed because the Authorization header was missing.
   Fixed by sending the JWT token in every protected request.

3) Faced routing and import errors while creating new management pages.
   Fixed by correcting Vue Router configuration and component imports.

4) Some database records caused foreign key dependency issues during deletion.
   Fixed by deleting related records before deleting the parent record.

5) User account management was challenging while implementing activate, deactivate and blacklist features.
   Fixed by updating user status in the backend and validating account status during login and protected API access.

6) Faced issues integrating frontend pages with backend APIs.
   Fixed by testing endpoints individually and ensuring proper request and response handling.

Milestone 4

In this part I implemented the complete company module. Companies can create and manage job postings, view applicants, review resumes and update application status.

1) company dashboard with statistics
2) create new job posting
3) view all company job postings
5) close and reopen jobs
6) company job details page
7) view applicants for each job
8) applicant details page
9) resume upload and resume viewing
10) shortlist and reject applicants
11) application status updates
16) protected company routes using JWT
17) file upload support for student resumes

Issues Encountered and Fixes

1) Resume upload was not working because the file was not being sent in FormData.
   Fixed by using multipart/form-data and appending the selected PDF file before sending the request.

2) Resume was showing as "No Resume" after registration.
   Fixed by saving the uploaded PDF inside the uploads/resumes folder and storing the filename in the database.

3) Company applicants page displayed no records although applications existed.
   Fixed by correcting the application query and matching student IDs with the Student table.

4) Applicant details page failed for some records because Student.query.get() returned None.
   Fixed by recreating the database with valid student records and removing inconsistent seeded data.

5) Resume button opened a 404 page when no resume was available.
   Fixed by displaying "No Resume Uploaded" instead of showing the View Resume button.

6) Company routes were accessible without proper authorization checks.
   Fixed by verifying the logged-in company using JWT before returning job and applicant details.
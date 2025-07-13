A Mini PROJECT to Test 3 Tier Architecture 
A small internal portal for a company where:
•	Employees can browse team members, view their skills, and see who’s available for collaboration or mentorship.

Building (3-Tier App)
1. Web Layer (Apache Public EC2)
•	Shows a polished UI
•	User clicks “Find Available Experts”
•	Triggers fetch from App layer
2. App Layer (Flask Python on Private EC2)
•	API endpoint like /available-skills
•	Fetches available employees from MySQL DB
3. DB Layer (MySQL on Private EC2)
•	Table: employees
o	id, name, skill, location, experience_years


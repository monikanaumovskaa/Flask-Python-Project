# Flask-Based Web Application for User Spending Management
Description
This web application, developed using Flask and SQLite, is designed to manage and track user spending data. The application provides several key functionalities, including retrieving total spending per user, calculating average spending by age group, and saving high-spending users to a database.

Features:
Total Spending per User: Retrieves the total amount spent by a specific user.
Average Spending by Age Group: Calculates the average spending within different age groups.
Save High-Spending Users: Identifies and saves users with high spending to a database for further management.

Application Functionality:
The application interacts with an SQLite database and provides the following API endpoints:

Retrieve Total Spending per User

GET /total_spent/<user_id>
This endpoint retrieves the total spending for a specific user based on their user_id.
Calculate Average Spending by Age Groups

GET /average_spending_by_age
This endpoint calculates and returns the average spending of users, grouped by age range.
Save High-Spending Users

POST /write_high_spending_user-save
This endpoint accepts user data and saves users who meet the criteria of being high spenders into the database.

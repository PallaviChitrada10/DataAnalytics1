# Email Fetch

We need to fetch 1000 random user records from the RandomUser.me API using Python and store them in a structured format (JSON, CSV, or database).  

Task Details:  
Use the requests library to call https://randomuser.me/api/?results=1000.  
Ensure proper error handling for failed requests.  
Store the data in a JSON file (users.json).  
Optional: Convert JSON to CSV for better readability (users.csv).  

Acceptance Criteria:  
A Python script (fetch_random_users.py) that successfully fetches and stores 1000 user records.  
Handles API failures gracefully with retries or error messages.  
Stores data in users.json.  
(Optional) Generates users.csv for structured data representation.  

Reference:  
Random User API Documentation: https://randomuser.me/documentation

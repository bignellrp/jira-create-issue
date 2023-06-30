import requests
import json
import getpass

jira_url = "https://example.com/rest/api/2/search"
jira_username = input("Jira Username: ")
jira_password = getpass.getpass("Jira Password: ")

# jira_url = "https://example.com/rest/api/2/search"
# jira_username = "<JIRA_USERNAME>"
# jira_password = "<JIRA_PASSWORD>"

# JQL query to search for the existing issue
jql_query = "project = <PROJECT_KEY> AND summary ~ '<SUMMARY>'"

# Define the parameters for the request
params = {
    "jql": jql_query,
    "maxResults": 1
}

# Create a session and set the authentication
session = requests.Session()
session.auth = (jira_username, jira_password)

# Send the POST request to search for the issue
response = session.post(jira_url, params=params)

if response.status_code == 200:
    data = response.json()
    total_issues = data.get("total")
    
    if total_issues > 0:
        print("Issue already exists.")
    else:
        print("Issue does not exist. Proceed with creating a new issue.")
else:
    print("Error searching for issue:", response.status_code)
    print(response.text)
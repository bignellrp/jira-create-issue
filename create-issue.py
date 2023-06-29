import base64
import json
import requests

api_url = "https://example.com/rest/api/2/issue"
username = "<JIRA_USERNAME>"
password = "<JIRA_PASSWORD>"

headers = {
    "Authorization": "Basic " + base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8"),
    "Content-Type": "application/json"
}

# Define the variables for each value in the JSON payload
project_key = "PROJECT_KEY"
summary = "Issue Summary"
description = "Issue Description"
issue_type = "Task"
priority = "High"

# Load the createIssue JSON template from the Jira API documentation
template_url = "https://docs.atlassian.com/software/jira/docs/api/REST/8.7.1/_downloads/createIssue.json"
response = requests.get(template_url)
template_json = response.json()

# Populate the variables in the JSON template
template_json["fields"]["project"]["key"] = project_key
template_json["fields"]["summary"] = summary
template_json["fields"]["description"] = description
template_json["fields"]["issuetype"]["name"] = issue_type
template_json["fields"]["priority"]["name"] = priority

# Convert the populated JSON template to a string
json_payload = json.dumps(template_json)

# Make the POST request to create the issue
response = requests.post(api_url, data=json_payload, headers=headers)

if response.status_code == 201:
    print("Issue created successfully!")
else:
    print("Error creating issue:", response.status_code)
    print(response.text)

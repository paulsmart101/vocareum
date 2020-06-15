#-- Import libraries
import requests, json

#-- Identifiers for the user, course, assignment, part, and desired credit limit --
courseId = 6590
userId = 326150
assignmentId = 60327
partId = 60328
credit = 50    #-- new limit --

#-- Read the current spend and credit limit --
url = "https://api.vocareum.com/api/v2/courses/{}/assignments/{}/parts/{}/resources/{}".format(courseId,assignmentId,partId,userId)
headers = {'Authorization': 'Token xxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
payload = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
response_data = response.json()
output = response_data['resources'][0]['cloud'][0]['aws_data']
print("Total Spent:",output['totalspend'])
print("Current Limit:",output['allowedspend'])

#-- Set the new credit limit --
payload = { "state": "active", "budget": credit }
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
response_data = response.json()
output = response_data
print("Update Status:",output['status'])

#-- Read back the new credit limit --
payload = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
response_data = response.json()
output = response_data['resources'][0]['cloud'][0]['aws_data']
print("New Limit:",output['allowedspend'])

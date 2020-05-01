#!/usr/bin/env python
# coding: utf-8

# # Locate student in all classes

# In[30]:


import requests, json
search_for = "paulsmart101@example.com"
headers = {
    'Authorization': 'Token abc'
}
payload = {
    "size":"10", #won't go over 10
    "page":"1"
}

# Request the total number of courses
url = 'https://labs.vocareum.com/api/v2/courses'
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
total_courses = int(parsed['total_records'])
print('Total courses:',total_courses)

# Calculate how many loops are required to iterate through all the courses
size = 10
page = 1 # Starting page
whole_loops = total_courses//size
course_ids = []

# Iterate through the courses 10 at a time
while page <= whole_loops:
    # Retrieve the next page of 10 courses
    url = 'https://labs.vocareum.com/api/v2/courses'
    payload = {'page':page}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    parsed = json.loads(response.text)

    # Loop through the 10 courses
    for course in parsed['courses']:

        # Display progress
        print(".", end=" ")

        # Request list of students in the course
        url = 'https://labs.vocareum.com/api/v2/courses/'+course['id']+'/users?role=student&include_dropped=false'
        payload = {}
        response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
        parsed = json.loads(response.text)

        # Loop through the students
        for user in parsed['users']:
            if user['email'] == search_for:
                print("\nFound user",search_for,"in course",course['name'],"(ID:"+course['id'],")")
                course_ids.append(course['id'])
    page = page+1

print("\nfinished")
print(course_ids)


# # List One Class

# In[1]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/7706'
payload = {}
headers = {'Authorization': 'Token abc'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List all Assignments of One Class

# In[ ]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/4319/assignments'
payload = {}
headers = {'Authorization': 'Token af39bb35c913794279d3f59c784b698b2d3f64df'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List One Assignment of One Class

# In[ ]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/4319/assignments/47296'
payload = {}
headers = {'Authorization': 'Token abc'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List all Parts of One Assignment of One Class

# In[ ]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/4319/assignments/47296/parts'
payload = {}
headers = {'Authorization': 'Token abc'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List One Part, of One Assignment, of One Class

# In[ ]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/4319/assignments/47296/parts/47297'
payload = {}
headers = {'Authorization': 'Token abc'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List all Resources for One Part for One Student

# In[31]:


import requests, json
url = 'https://labs.vocareum.com/api/v2/courses/4319/assignments/47296/parts/47297/resources/290120'
payload = {}
headers = {'Authorization': 'Token abc'}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4, sort_keys=True))


# # List all Students for One Class

# In[32]:


import requests, json
class_id = "7706" #Identifier for the class
headers = {
    'Authorization': 'Token abc'
}
payload = {
    "size":"10", #won't go over 10
    "page":"1"
}

# Get total number of students in the class
url = 'https://labs.vocareum.com/api/v2/courses/'+class_id+'/users?role=student&include_dropped=false'
print(url)
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
parsed = json.loads(response.text)
print(parsed['total_records'])

# Calculate how many loops are required to iterate through all the courses
size = 10
page = 1 # Starting page
whole_loops = parsed['total_records']//size
whole_loops = whole_loops + 1
print(whole_loops)
#whole_loops = 1 #remove when ready

while page <= whole_loops:
    # Retrieve the next page of 10 courses
    payload = {'page':page}
    response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
    parsed = json.loads(response.text)
    for student in parsed['users']:
        if student['dropped']:
            continue
        if not student['organization_terms_agreed_date_utc']:
            student['organization_terms_agreed_date_utc'] = "False"
        print(student['email']+','+student['name']+','+student['organization_terms_agreed_date_utc'])
    page = page+1


#

import json

response = '{"name": "Alex", "age": 17, "skills": ["Python", "Git"]}'

response = json.loads(response)
response['age'] = 18
response['skills'].append("FastAPI")
response = json.dumps(response)
print(response)
print(type(response))
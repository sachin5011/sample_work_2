import requests

# url = r"http://127.0.0.1:8000/api/user/change-password/"
# url = r"http://127.0.0.1:8000/api/user/login/"
# url = r"http://127.0.0.1:8000/api/user/register/"
url = "http://127.0.0.1:8000/api/user/logout/"

payload = {
    "email": "testresponse3@gmail.com",
    "password": "12345"
}

header = {
    # "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0MzQ5MjAzLCJpYXQiOjE2OTQzNDg5MDMsImp0aSI6IjY2NDE3NGYyODk2ZTQ1NzlhMGE4OWQ0YTdkYjViM2JkIiwidXNlcl9pZCI6OX0.VWXTBd0LwMzk2Ei9E7eD1XFqq82E3WvKn_V0BTj40qM"
}
# responese = requests.post(url, data=payload, headers=header)
# responese = requests.post(url, headers=header)
# responese = requests.post(url, data=payload)

# print(responese.status_code)
# print(responese.text)
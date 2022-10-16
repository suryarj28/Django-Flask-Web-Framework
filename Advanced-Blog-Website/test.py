import requests
import datetime


blog_url = "https://api.npoint.io/117c09fda2f9aeeedc5a"
blog_response = requests.get(blog_url).json()

print(blog_response)

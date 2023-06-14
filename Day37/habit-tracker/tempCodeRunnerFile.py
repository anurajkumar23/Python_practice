
response = requests.post(url=pixela_endpoint, json= user_params)
print(response.text)
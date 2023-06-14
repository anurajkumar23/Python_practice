response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
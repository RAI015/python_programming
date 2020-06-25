import requests

# r = requests.post(
#     'http://127.0.0.1:5000/post', data={'username': 'Mike'}
# )
# r = requests.put(
#     'http://127.0.0.1:5000/post', data={'username': 'Mike'}
# )

r = requests.get('http://127.0.0.1:5000/employee/Jun')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'Jun'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'Jun', 'new_name': 'Sakai'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'Jun'})
print(r.text)

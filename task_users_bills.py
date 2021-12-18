
import pandas as pd

users_data = pd.DataFrame(data = {'id': [1, 2, 3], 'name': ['Maria', 'Ivan', 'Asen'], 'number': ['+39587111111', '+39587222222', '+39587333333']})
users_bills_data = pd.DataFrame(data = {'id': [1, 2, 3], 'bill': [25.50, 30.48, 5.98]})

users = pd.merge(users_data, users_bills_data, on = 'id')
max_users = users[users['bill'] == users['bill'].max()]
min_users = users[users['bill'] == users['bill'].min()]

max_bill = max_users['bill'].to_string(index=False)
max_name = max_users['name'].to_string(index=False)

min_bill = min_users['bill'].to_string(index=False)
min_name = min_users['name'].to_string(index=False)

print(f'The user with highest bill - {max_bill} is {max_name}')
print(f'The user with lowest bill - {min_bill} is {min_name}')


users: list = [
    {'name': 'Szymon', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Patrycja', 'posts': 7, 'city': 'Łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},

]
print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'Twój znajomy {user['name']}, z miejscowości {user['city']}, opublikował {user['posts']} postów')
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')

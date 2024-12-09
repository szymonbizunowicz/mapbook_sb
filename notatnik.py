from mapbook.crud import add_user, read_users

users: list = [
    {'name': 'Patryk', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Patryk', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Tomek', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Julia', 'posts': 1, 'city': 'Warszawa'},

]

def remove_user(userlist:list)->None:
    user_to_find:str=input("podaj imię do usunięcia:")
    for user in userlist:
        if user['name'] == user_to_find:
            print(f'usuwam: {user}')
            userlist.remove(user)

# remove_user(users)

def update_user(userlist:list)->None:
    user_to_find: str = input("podaj imię użytkownika do aktualizacji:")
    for user in userlist:
        if user['name'] == user_to_find:
            new_name: str = input("proszę podać nowe imię znajomego ")
            new_posts: int = int(input("podaj nową liczbę postów "))
            new_city: str = input("podaj nowe miasto ")
            user["name"] = new_name
            user["posts"] = new_posts
            user["city"] = new_city


#update_user(users)

while True:
    print("======MENU======")
    print("0. Wyjście z programu")
    print("1. Dodaj znajomego")
    print("2. Wczytaj znajomych")
    print("3. Aktualizuj znajomego")
    print("4. Usuń znajomego")
    print("5. Generuj mapę z lokalizacją znajomego")
    print("6. Generuj mapę z lokalizacją wszystkich znajomych")


    menu_option:str=input("Użytkowniku, wybierz opcję menu: ")
    print(f"Użytkownik wybrał {menu_option}")
    if menu_option == "0":
        break
    if menu_option == "1":
        add_user(users)
    if menu_option == "2":
        read_users(users)
    if menu_option == "3":
        update_user(users)
    if menu_option == "4":
        remove_user(users)
    if menu_option == "5":
        pass
    if menu_option == "6":
        pass
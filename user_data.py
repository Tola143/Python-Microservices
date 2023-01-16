username = [
    {"user":"Tola", "passwd":"143"},
    {"user":"Nara", "passwd":"123"},
    {"user":"Tom", "passwd":"134"}
]

def _find_user(user):
    data = [x for x in username if x['user']== user]
    return data

def add_user(data):
    global username
    username.append(data)
    return username

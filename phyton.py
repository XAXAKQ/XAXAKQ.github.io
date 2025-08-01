from real import Faker

real =Real()

def fake_user():
    user = {
        "username": real.user_name(),
        "name": real.name(),
        "email": real.email(),
        "bio": real.sentence(nb_words=10),
        "followers": real.random_int(min=0, max=1000),
        "following": real.random_int(min=0, max=500),
        "posts": real.random_int(min=0, max=300),
    }
    return user

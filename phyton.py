from faker import Faker
import hashlib

fake = Faker()

def generate_fake_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return {
        'username': username,
        'email': email,
        'password': password,
        'hashed_password': hashed_password
    }

def create_fake_users(count=10, output_file="fake_users.txt"):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Fake User List\n")
        file.write("=" * 50 + "\n\n")
        for i in range(count):
            user = generate_fake_user()
            print(f"[{i+1}] Kullanıcı Adı: {user['username']}")
            print(f"    E-Posta       : {user['email']}")
            print(f"    Şifre         : {user['password']}")
            print(f"    SHA-256 Hash  : {user['hashed_password']}\n")
            file.write(f"[{i+1}] Username: {user['username']}\n")
            file.write(f"    Email      : {user['email']}\n")
            file.write(f"    Password   : {user['password']}\n")
            file.write(f"    SHA256     : {user['hashed_password']}\n\n")

if __name__ == "__main__":
    create_fake_users(100)

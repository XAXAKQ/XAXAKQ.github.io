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

if __name__ == "__main__":
    for _ in range(5):
        user = real_user()
        print(user)
SECRET_PASSWORD = "2007200844"

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        sifre = request.form.get("password")
        if sifre == SECRET_PASSWORD:
            return redirect(url_for("secret"))
        else:
            error = "Şifre yanlış. Tekrar deneyin."
    return render_template("index.html", error=error)

@app.route("/secret")
def secret():
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)

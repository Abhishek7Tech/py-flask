from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def index_is():
    return render_template("index.html")

# @app.route("/holy/<username>")
# def index_again_is(username):
#     return render_template("index.html",name = username)

# @app.route("/holy/<uuid:id>")
# def index_again_is(id=None):
#     return render_template("index.html", ids = id)


@app.route("/about.html")
def about_is():
    return render_template("about.html")


@app.route("/<string:page>")
def page_is(page):
    return render_template(page)


# def set_data(data):
#     with open("../../database.txt", mode="a") as file:
#         first_name = data['firstName']
#         last_name = data['lastName']
#         email = data['email']
#         about = data['about']
#         message = data['message']

#         file.write(
#             f"\n {first_name}, {last_name}, {email}, {about}, {message}")


def set_csv_data(data):
    with open("../../database.csv", "a", newline="") as csvfile:

        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']
        about = data['about']
        message = data['message']

        write = csv.writer(csvfile, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
        write.writerow([first_name, last_name, email, about, message])


@app.route("/contact-me", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # set_data(data)
            set_csv_data(data)
            return redirect("/thanks.html")
        except:
            return "Something went wrong!"
    else:
        return "SOMETHING IS WRONG"

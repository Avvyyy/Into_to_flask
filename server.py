#render_template is used to render a html file
from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

#variable, data is a list of dictionaries 
data = [
    {
        "id":1,
        "todo":"code today",
        "more": "some more code"
    },
    {
        "id":2,
        "todo":"hit the gym",
        "more": "some more gym things"
    },
    {
        "id":3,
        "todo":"go to the market",
        "more": "some more market things"
    }
]

#Putting "@" before variable, app makes it a static method
@app.get("/") # "/" means that server should get from homepage
def home_page():
    return render_template("index.html", todos=data)

@app.get("/details/<int:id>")
def handle_post_details(id):
    todo_data = {}
    for todo in data:
        if todo['id'] == id:
            todo_data = todo
    return render_template("details.html", info=todo_data)

@app.get("/signup")
def sign_up_handler():
    return render_template("signup.html")

#To run a post
@app.post("/signup")
def handle_submit_signup() :
    form_value = request.form
    my_id = random.randint(3, 1000)
    data.append({
        "id":my_id,
        "todo": form_value['todo'],
        "more":form_value['more']
    })
    print(data)
    return redirect("/")

#Code to delete a dictionary from the list

@app.route("/delete_el/<int:id>", methods=["GET", "POST", "DELETE"])
def handle_delete(id):
    for todo in data:
        if todo['id'] == id:
            target_index = data.index(todo)
            data.pop(target_index)
    return redirect ("/")


app.run(port=5050, debug=True)
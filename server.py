from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")  #localhost:5000/
def groot(): 
    return "Hello Captain"

# Create a route in which the data above is declared and then sent to the template engine to be rendered
@app.route('/lists')
def render_lists():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html",users_info = users)









if __name__ == "__main__":
    app.run(debug=True)
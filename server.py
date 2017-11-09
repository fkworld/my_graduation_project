from flask import Flask, render_template, send_file, send_from_directory, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/register')
def register():
    print("node is success register.")
    return "sucecess"

@app.route('/needtask')
def needtask():
    print("node is asking for task.")
    response = make_response(send_file("README.md"))
    response.headers["Content-Disposition"] = "attachment; filename=README.md;"
    return response

if __name__ == '__main__':
    app.run()
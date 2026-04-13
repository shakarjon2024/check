from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def check():
    result = ""

    if request.method == "POST":
        num = int(request.form.get("num"))

        if num % 2 == 0:
            result = "Juft son"
        else:
            result = "Toq son"



if __name__ == '__main__':
    app.run(debug=True)

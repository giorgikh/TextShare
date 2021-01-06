from flask import Flask, render_template, request
from os import path
from MyModule import ManagePath


app = Flask(__name__)

t = ManagePath()
t.createTmpFolder(path.dirname(__file__), "15")
t.createFile(f'{path.dirname(__file__)}/templates/tmp/15/genereated.html')
t.createFile(f'{path.dirname(__file__)}/templates/tmp/15/note')
t.createFile(f'{path.dirname(__file__)}/templates/tmp/15/userInfo')

t.writeTextToFile(
    f'{path.dirname(__file__)}/templates/tmp/15/note', "teqstii \nteqstii22")

t.appendTextToFile(
    f'{path.dirname(__file__)}/templates/tmp/15/note', "\ndaematateqsti")


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        editorData = request.form.get("editordata")
        # return render_template('generate.php', data=editorData)
        return render_template("saveLink.php", link="Link")
    return render_template('index.php')


@app.route("/note", methods=['GET', 'POST'])
def note():
    return render_template("generate.php", data="dataaaa")


@app.route("/saved", methods=['GET', 'POST'])
def createLink():
    return render_template("saveLink.php", data="Link")


if __name__ == "__main__":
    app.run(debug=True)

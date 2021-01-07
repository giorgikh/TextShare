from flask import Flask, render_template, request
from os import path
from MyModule import ManagePath, generate_user_info, note_exist


app = Flask(__name__)
file_manager = ManagePath()


def temp(editor_data):
    user_id, user_link = generate_user_info()

    tmp_folder_path = path.dirname(__file__) + f'/templates/tmp/{user_id}'
    user_data_path = f'{path.dirname(__file__)}/templates/tmp/{user_id}/data'
    user_info_file_path = f'{path.dirname(__file__)}/templates/tmp/{user_id}/userInfo'

    file_manager.create_tmp_folder(tmp_folder_path)
    file_manager.create_file(user_data_path)
    file_manager.create_file(user_info_file_path)

    file_manager.write_text(user_data_path, editor_data)
    # file_manager.append_text(user_data_path, f'{editor_data}')
    return user_id, user_link


@app.route("/", methods=['GET', 'POST'])
def home():
    # ამ ფუნქციაში მოხდება ჩანაწერის შენახვა, ფაილების შექმნა, და ლინკის დაგენერირება
    if request.method == 'POST':
        editor_data = request.form.get("editordata")
        data = editor_data
        print(data)
        print(type(data))
        if data != "":
            user_id, user_link = temp(editor_data)
            # return render_template('generate.php', data=editorData)
            file_url = request.base_url + f'/noteid={user_id}'
            print(file_url)

            return render_template("saveLink.php", data=data, base_url=file_url)
    return render_template('index.php')


@app.route("/note", methods=['GET', 'POST'])
def note():
    return render_template("generate.php", data="dataaaa")


@app.route("/saved", methods=['POST'])
def create_link():
    return render_template("saveLink.php", data="Link")


@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return render_template("error_404.php")


@app.route('/<noteid>')
def word_up(noteid):
    user_note_id = noteid.split("=")[1]
    file_path = path.dirname(__file__) + f'/templates/tmp/{user_note_id}'
    if note_exist(file_path):
        data = file_manager.read_text(file_path + "/data")
        base_url = request.base_url
        print(base_url)
        return render_template("generate.php", data=data, base_url=base_url)
    return "ar arsebobs!"


if __name__ == "__main__":
    app.run(debug=True)

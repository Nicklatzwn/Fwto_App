import os
import secrets
from flask import current_app, send_from_directory


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], picture_fn)

    form_picture.save(picture_path)

    return picture_fn


def delete_picture(form_picture):
    picture_path = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], form_picture)
    os.remove(picture_path)


def download_picture(form_picture):
    relative_directory = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=relative_directory, filename=form_picture, as_attachment=True)
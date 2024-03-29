'''
This file contains the Flask blueprint for the file explorer.
It provides routes for browsing, uploading, and downloading files.
'''
from flask import Blueprint, render_template, request, send_file, current_app
import os
from icecream import ic


file_explorer_bp = Blueprint('flask_file_explorer', __name__, template_folder='templates', static_folder='static')

@file_explorer_bp.route('/')
def index():
    '''
    Renders the index.html template with the base directory.
    '''
    base_directory = get_base_directory()
    return render_template('flask-file-explorer/index.html', base_directory=base_directory)


@file_explorer_bp.route('/browse')
def browse():
    '''
    Renders the index.html template with the files and directories in the given path.
    '''
    base_directory = get_base_directory()
    path = request.args.get('path', '')
    path = remove_leading_slash(path)
    
    
    full_path = os.path.join(base_directory, path)
    ic(base_directory)
    ic(full_path)
    ic(path)
    if not is_in_base_directory(full_path) :
        return 'Illegal path', 400
    
    if os.path.isdir(full_path):
        files = os.listdir(full_path)
        
        if request.args.get('path', '') != '':
            return render_template('flask-file-explorer/listings.html', base_directory=base_directory, path=path, files=files)
        
        return render_template('flask-file-explorer/index.html', base_directory=base_directory, path=path, files=files)
    else:
        return send_file(full_path)
    

@file_explorer_bp.route('/upload', methods=['POST'])
def upload():
    '''
    Handles the file upload request.
    '''
    base_directory = get_base_directory()
    path = request.form.get('path', '')
    path = remove_leading_slash(path)
    
    file = request.files.get('file')
    full_path = os.path.join(base_directory, path, file.filename)
    
    if not is_in_base_directory(full_path) :
        return 'Illegal path', 400
    
    if file:
        file.save(os.path.join(full_path))
    return '', 204


@file_explorer_bp.route('/download')
def download():
    '''
    Handles the file download request.
    '''
    base_directory = get_base_directory()
    path = request.args.get('path', '')
    full_path = os.path.join(base_directory, path)
    
    if not is_in_base_directory(full_path) :
        return 'Illegal path', 400
    
    if os.path.isdir(full_path):
        return send_file(full_path, as_attachment=True)
    else:
        return send_file(full_path)
    
    
def remove_leading_slash(path):
    '''
    Removes the leading slash from a path.
    '''
    if path.startswith('/'):
        return path[1:]
    return path

def is_in_base_directory(path):
    '''
    Checks if a path is in the base directory.
    '''
    base_directory = os.path.abspath(get_base_directory())
    path = os.path.abspath(path)
    return path.startswith(base_directory)

def is_in_subdirectory(path):
    '''
    Checks if a path is in a subdirectory of the base directory.
    '''
    base_directory = os.path.abspath(get_base_directory())
    path = os.path.abspath(path)
    return not path.startswith(base_directory) and base_directory in path


def get_base_directory():
    '''
    Gets the base directory from the configuration.
    '''
    return current_app.config.get('FFE_BASE_DIRECTORY')

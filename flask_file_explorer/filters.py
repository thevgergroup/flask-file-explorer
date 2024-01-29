'''
This file contains custom filters for Jinja2 templates.
'''
import os
from flask import current_app
base_dir = None

def directory(file, path):
    '''
    Checks if a file is a directory.
    '''
    
    full_path = os.path.join(base_dir, path, file)
    return os.path.isdir(full_path)

def inlineable(file):
    '''
    Checks if a file can be shown inline.
    '''
    file_extension = os.path.splitext(file)[1]
    inlineable_extensions = ['.txt', '.md', '.py', '.html', '.css', '.js']
    return file_extension.lower() in inlineable_extensions
def register_filters(app):
    '''
    Registers the custom filters with the Flask app.
    '''
    with app.app_context():
        global base_dir
        base_dir = current_app.config.get('BASE_DIRECTORY')
        
    app.jinja_env.filters['directory'] = directory
    app.jinja_env.filters['inlineable'] = inlineable
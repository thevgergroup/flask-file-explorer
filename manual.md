# File Explorer Flask Blueprint

The File Explorer Flask Blueprint is a web application that allows you to browse, upload, download, and view files in a specified base directory. It provides a user-friendly interface using Bootstrap 5 and Boxicons for directories and folders.

## Installation

To use the File Explorer Flask Blueprint, you need to follow these steps:

1. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

2. Create a new Flask application or add the File Explorer Blueprint to an existing Flask application.

3. Copy the provided code files (`main.py`, `file_explorer.py`, `index.html`, `style.css`, `script.js`, `filters.py`) into your Flask application directory.

4. Update the `main.py` file to register the File Explorer Blueprint and configure the base directory. You can modify the `BASE_DIRECTORY` variable to specify the desired base directory.

5. Run the Flask application by executing the following command:

   ```
   python main.py
   ```

6. Access the File Explorer in your web browser by navigating to `http://localhost:5000/file-explorer`.

## Usage

Once the File Explorer Flask Blueprint is installed and running, you can use it to perform various file operations:

- **Browsing**: The File Explorer displays the files and directories in the specified base directory. You can navigate through the file system by clicking on directories.

- **Uploading**: To upload a file, click on the "Choose File" button, select the file you want to upload, and click the "Upload" button. The file will be saved in the current directory.

- **Downloading**: To download a file or directory, click on the file or directory name. If it's a file, it will be downloaded directly. If it's a directory, a zip file containing the directory contents will be downloaded.

- **Viewing**: Some file types can be viewed inline in the browser. Clicking on a supported file will display its content directly in the File Explorer.

## Customization

You can customize the appearance and behavior of the File Explorer by modifying the provided code files:

- **`index.html`**: This file contains the HTML template for the File Explorer. You can modify the structure and styling of the interface.

- **`style.css`**: This file contains custom CSS styles for the File Explorer. You can modify the styles to match your desired design.

- **`script.js`**: This file contains custom JavaScript code for the File Explorer. You can add additional functionality or modify the existing behavior.

- **`filters.py`**: This file contains custom filters for Jinja2 templates. You can add or modify filters to customize the rendering of file and directory names.

## Conclusion

The File Explorer Flask Blueprint provides a convenient way to browse, upload, download, and view files in a specified base directory. It offers a user-friendly interface and supports common file operations. By following the installation and usage instructions, you can easily integrate the File Explorer into your Flask application and customize it to meet your specific needs.
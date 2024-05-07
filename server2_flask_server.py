from flask import Flask, send_from_directory,render_template,send_file
import os

app = Flask(__name__)

# Specify the directory where your files are located
UPLOAD_FOLDER = 'temp_my_app\\repository\\metadata\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

TARGETS_FOLDER = "temp_my_app\\repository\\targets\\"
app.config['TARGETS_FOLDER'] = TARGETS_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024



@app.route('/metadata/<path:filename>')
def serve_file(filename:str =''):
    print('-----------',filename)
    if filename.endswith('.tar.gz') or filename.endswith('.json'):
        return  send_from_directory(app.config['UPLOAD_FOLDER'], filename,as_attachment=True) 
        # return send_file(path_or_file=app.config['UPLOAD_FOLDER']+ filename,as_attachment=True)
    else:
         return  "<h1> Python Server </h1>"
    
@app.route('/targets/<path:filename>')
def serve_file1(filename:str ):
    if filename.endswith('.tar.gz') or filename.endswith('.json'):
        return  send_from_directory(app.config['TARGETS_FOLDER'], filename,as_attachment=True) 
    else:
         return  "<h1> Python Server </h1>"
    

@app.route('/<path:other>')
@app.route('/')
def home_page(other:str=''):
    return "<h1> Python Server </h1>"

if __name__ == '__main__':
    app.run(debug=False)




# @app.route('/metadata/')
# def serve_file(filename:str):
#     print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
#     if filename.endswith('.tar.gz') or filename.endswith('.json'):
#         print(app.config['UPLOAD_FOLDER'])
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'metadata\\'+filename)
#         print('---------------->',file_path)
#         return send_file(file_path, as_attachment=True)
#     else:
#         return  "<h1> Python Server </h1>"

# @app.route('/targets/')
# def serve_file2(filename:str):
#     if filename.endswith('.tar.gz') or filename.endswith('.json'):
#         print(app.config['UPLOAD_FOLDER'])
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'targets\\'+filename)
#         print('---------------->',file_path)
#         return send_file(file_path, as_attachment=True)
#     else:
#         return  "<h1> Python Server </h1>"


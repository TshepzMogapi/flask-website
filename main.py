from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../UPLOAD_FOLDER'

app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
if __name__ == "__main__":
    app.run(debug=True)
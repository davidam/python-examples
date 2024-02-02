

# Importamos todo lo necesario
import os
from flask import Flask, render_template, request
#from werkzeug import secure_filename

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './upload'

@app.route("/")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('uploadfile.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
#  filename = secure_filename(f.filename)
  filename = f.filename
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  return "<h1>Archivo subido exitosamente</h1>"

if __name__ == '__main__':
 # Iniciamos la aplicación
 app.run(debug=True)

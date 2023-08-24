from flask import request , Flask
import requests
import os
from pdf2image import convert_from_path

app = Flask(__name__)

def image_conversion(pdf_file, output_folder):

    pages = convert_from_path(pdf_file, 500)
    for count, page in enumerate(pages):
        page.save(f'{output_folder}/{output_folder}_{count}.jpg', 'JPEG')

def conversion(app_id , url):
    app_id = app_id.replace('/',"_")
    if not os.path.exists(app_id):
        os.makedirs(app_id)

    pdf = requests.get(url)

    filename = f'./{app_id}/{app_id}.pdf'
    with open(filename, 'wb') as f:
        f.write(pdf.content)

    # Example usage:
    pdf_file = f'./{app_id}/{app_id}.pdf'# Replace with your PDF file name
    output_folder = app_id # Replace with the folder where you want to save the images
    image_conversion(pdf_file, output_folder)

    os.remove(filename)

@app.route('/pdf_to_image',methods=['GET' , 'POST'])
def pdf_to_image():
    data = request.form
    app_id = data['id']
    url = data['url']

    conversion(app_id , url)

    return '200'


if __name__ == "__main__":
    app.run(debug = True , host='0.0.0.0' , port = 5050)
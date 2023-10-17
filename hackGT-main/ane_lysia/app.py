from flask import Flask, render_template, request, redirect, url_for
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time
from dotenv import load_dotenv
import os
from fpdf import FPDF
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    input_image_path = os.path.join('images', 'input_image.jpeg')
    file.save(input_image_path)
    return redirect(url_for('display_pdf'))

@app.route('/display_pdf')
def display_pdf():
    open_dyslexic_convert('input_image.jpeg')
    return render_template('display_pdf.html')

@app.route('/retry', methods=['POST'])
def retry():
    return redirect(url_for('index'))

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    text = main('input_image.jpeg')
    tts = gTTS(text)
    tts.save('static/output.mp3')
    return redirect(url_for('play_audio'))

@app.route('/play_audio')
def play_audio():
    return render_template('play_audio.html')

def open_dyslexic_convert(f_name):
    pdf = FPDF(format='letter', unit='in')
    pdf.add_font('new', '', 'ttf_file.ttf', uni=True)
    pdf.add_page()
    pdf.set_font("new", "", 20)
    pdf.multi_cell(7, 0.4, txt=main(f_name), align='J')
    pdf.output("static/output.pdf") 

def main(path):
    try:
        load_dotenv()
        endpoint = 'use azure endpoint'
        key = 'use azure key'
        computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
        images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        read_image_path = os.path.join(images_folder, path)
        get_text(read_image_path, computervision_client)
        result = get_text(read_image_path, computervision_client)
        return result

    except Exception as ex:
        print(ex)

def get_text(image_file, computervision_client):
    result = ""

    with open(image_file, "rb") as image:
        read_response = computervision_client.read_in_stream(image, raw=True)

    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower() not in ['notstarted', 'running']:
            break
        time.sleep(1)

    if read_result.status == OperationStatusCodes.succeeded:
        for page in read_result.analyze_result.read_results:
            for line in page.lines:
                result += line.text + "\n"

    return result

if __name__ == '__main__':
    app.run(debug=True)

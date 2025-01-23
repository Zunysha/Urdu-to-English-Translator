from flask import Flask, render_template, request
import requests, uuid, json

app = Flask(__name__)

# Add your key and endpoint
key = "74b6be8177c94dfaa41537d39d928754"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "eastasia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'ur',
    'to': ['en']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        body = [{'text': text_to_translate}]
        
        request_trans = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request_trans.json()
        translated_text = response[0]['translations'][0]['text']

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)

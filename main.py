from flask import Flask, request, render_template_string, send_file
import openai
from openai import OpenAI

app = Flask(__name__)

# Replace "your_openai_api_key_here" with your actual OpenAI API key


@app.route('/')
def index():
    # Return the HTML content
    return render_template_string(open("index.html").read())

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['userInput']
    api_key = request.form['apiKey']
    organization_id = request.form['orgID']
    client = OpenAI(
	# This is the default and can be omitted
	api_key = api_key,
	organization = organization_id,
    )

    # Call the OpenAI API with the user's input
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="nova",
        input= user_input
    )
    filename = './output_audio.mp3'
    response.stream_to_file(filename)
    
    # Return the OpenAI API's response
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
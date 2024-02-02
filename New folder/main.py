import pdfrw
from transformers import pipeline
from flask import Flask, render_template, request

pdf = pdfrw.PdfReader('48lawsofpower.pdf')
text = ""

for page in pdf.pages:
    text += page.extract_text()

summarizer = pipeline("summarization")

def generate_answer(question, text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    answer = summary[0]['summary_text']
    return answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        answer = generate_answer(question, text)
        return render_template('index.html', answer=answer)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

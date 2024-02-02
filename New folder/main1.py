import requests

def ask_question(question):
    url = "https://power-of-48-laws.herokuapp.com/"
    data = {"question": question}
    response = requests.post(url, data=data)
    return response.text

question = "Can you give me an example from history where the enemy was crushed totally from the book?"
answer = ask_question(question)
print(answer)
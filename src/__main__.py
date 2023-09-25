import click
import requests
from InquirerPy import prompt

SERVER_URL = 'http://localhost:5000'

def ask_for_options():
    questions = [
    {"type": "input", "message": "Github Repo URL", "name": "url"},
    {"type": "input", "message": "port", "name": "port"},
    {"type": "input", "message": "What is your email?", "name": "email"},
    ]
    return prompt(questions)

def send_request(url, port, email):
    data = {
        "url": url,
        "port": port,
        "email": email
    }
    response = requests.post(SERVER_URL, data=data)
    return response


def main():
    print("Welcome to Sparckles CLI!")
    prompt = ask_for_options()
    url = prompt["url"]
    port = prompt["port"]
    email = prompt["email"]
    print("Sending request...")
    response = send_request(url, port, email)
    print(response.text)



if __name__ == '__main__':
    main()

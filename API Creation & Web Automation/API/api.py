from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

# A small list of some facts about cats 😺
Cat_Facts = [
    "Cats sleep 13-16 hours a day, conserving energy for hunting.",
    "A group of cats is called a clowder.",
    "Cats can rotate their ears 180°, enhancing their hearing.",
    "The oldest pet cat was buried alongside its owner 9,500 years ago.",
    "A cat's nose print is as unique as a human fingerprint.",
    "Cats sleep 70% of their lives.",
    "Cats have five toes on their front paws but only four on their back paws."
]

# A small list of some cat breeds 😺


Cat_Breeds = [
    "American Bobtail",
    "American Wirehair",
    "Abyssinian",
    "American Curl",
    "Birman",
    "Bombay",
    "European Shorthair"
]




# The route of the home (HTML) page

@app.route("/home")
def home():
    # Renders an HTML page displaying a cat fact.

    fact_about_cats = random.choice(Cat_Facts)
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cat Facts</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h1>🐈 Welcome to Cat Facts 🐈</h1>
        <h4 style="font-size: 24px;">Did you know that ?</h4>
        <h6 style="font-size: 30px; color: red; font-style: italic;" id="Cat_Fact">{{ fact }}</h6>
        <p style="color: gray;">Learn more about your feline friends !</p>
    </body>
    </html>
    """
    return render_template_string(html, fact=fact_about_cats)

@app.route("/breeds")
def breeds():
    # Renders an HTML page displaying a cat breed.

    cat_breed = random.choice(Cat_Breeds)
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cat Breeds</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h1>😺 Welcome to Cat Breeds 😺</h1>
        <h4 style="font-size: 24px;">This is a cat breed 👇</h4>
        <h6 style="font-size: 30px; font-style: italic;" id="Cat_Breed">{{ fact }}</h6>
        <p style="color: gray;">Learn more about your feline friends !</p>
    </body>
    </html>
    """
    return render_template_string(html, fact=cat_breed)

# The route of the fact page

@app.route("/fact")
def fact():
    # API endpoint that returns a cat fact in JSON format.

    return jsonify({"fact_about_cats": random.choice(Cat_Facts), "cat_breed": random.choice(Cat_Breeds)})


if __name__ == "__main__":
    app.run(debug=True)

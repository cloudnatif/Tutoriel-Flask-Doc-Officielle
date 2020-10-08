from flask import Flask
app = Flask("__name__")
@app.route('/')
def hello(): 
    return """Bonjour Mon frère \
        C'est vraiment cool. Je vais devenir un expert en architecture Cloud Natives"""
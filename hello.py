from flask import Flask
app = Flask("__name__")
@app.route('/')
def hello(): 
    return """Bonjour Mon frère \
        C'est vraiment cool. Je vais devenir un expert en architecture Cloud Natives
        Dans un premier temps je commence par Flask
        Ensuite ja vais vers les architecture cloud native avec une appli flask/aws ou flask/azure
        Le debugger c'est cool
        il faudra se donner du temps
        Créer une ESN pour aider les entreprises à migrer vers des architectures Cloud Natives"""
from main import app

@app.route('/')
def top_page():
    return 'Hello, World!'

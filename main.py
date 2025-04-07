from app import FrameWorkApp

app=FrameWorkApp()

@app.route("/home")
def home(request, response):
    response.text="Home pagedan salom"

@app.route("/about")
def about(request, response):
    response.text="About pagedan salom"
@app.route("/contacts")
def home(request, response):
    response.text="Telegram - @storm_asliddin"
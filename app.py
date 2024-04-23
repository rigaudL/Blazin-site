from flask import Flask, render_template
import pandas as pd

# df = pd.read_csv("Dataforwebsite.csv")
# for index, row in df.iterrows():
#     pass

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("/Home.html")


@app.route("/Products")
def Products():
    return render_template("/Products.html")


@app.route("/About")
def About():
    return render_template("/About.html")

@app.route("/Book")
def Book():
    return render_template("/Book.html")



if __name__ == "__main__":
    app.run(debug=True)
    

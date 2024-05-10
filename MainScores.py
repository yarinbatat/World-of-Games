from flask import Flask

app = Flask("yarin")

@app.route('/')
def score_server():
    with open('scores.txt', 'r') as file:
        score = file.read().strip()
        if score.isdigit():
            html_content = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1>The score is <div id="score">{score}</div></h1>
            </body>
            </html>
            """
        else:
            html_content = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{score}</div></h1>
            </body>
            </html>
            """
    return html_content

app.run(host="0.0.0.0", port=5001, debug=True)

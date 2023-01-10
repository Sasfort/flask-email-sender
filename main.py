from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message
import os

load_dotenv()
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv("SENDER_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("SENDER_PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', sender=os.getenv("SENDER_EMAIL"),
                  recipients=['sasfort14@gmail.com'])
    msg.body = "Flask message sent to Syabib."

    mail.send(msg)
    return "Mail sent successfully"


if __name__ == '__main__':
    app.run(debug=True)

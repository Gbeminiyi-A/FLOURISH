from flask import Flask, render_template, request, flash, redirect, url_for
import datetime
import ssl, smtplib, pandas
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

year = datetime.datetime.today().year

app = Flask(__name__)

app.config['SECRET_KEY'] = "Your secret key"
# app.config['SECRET_KEY'] = os.environ.get('secret_key')

email = "hello@yourflourishlife.com"
password = "FloRich1!"
# password = os.environ.get("flourishemailpassword")
context = ssl.create_default_context()

msg = MIMEMultipart()
msg['Subject'] = "Welcome to the Flourish Rapidly Community."
body = """
Hello,
Thanks for subscribing to your flourish life newsletter. As a welcome gift, check out this free document.
"""

msg.attach(MIMEText(body, "plain"))

filename = "Social Media guidelines burgeon careers.pdf"
attachment = open("Social Media guidelines burgeon careers.pdf", "rb")

part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)

part.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(part)
host = "mail.privateemail.com"

text = msg.as_string()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email_to_subscribe = request.form.get('email')
        if len(email_to_subscribe) > 0:
            df = pandas.read_csv("C:/Users/OLUWAGBEMINIYI/Documents/Geebee/subscribed_emails.csv")
            emails = df.to_dict(orient="list")['emails']
            if email_to_subscribe in emails:
                flash("You've already subscribed!")
                return redirect(url_for('home'))
            else:
                with open("subscribed_emails.csv", "a+") as file:
                    file.write(f"{email_to_subscribe}\n")
                with smtplib.SMTP_SSL(host, 465, context=context) as connection:
                    connection.ehlo()
                    connection.login(email, password)
                    connection.sendmail(
                        from_addr=email,
                        to_addrs="gagbedejobi@gmail.com",
                        msg=text,
                    )
    return render_template("index.html", year=year)


@app.route("/about-me", methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        email_to_subscribe = request.form.get('email')
        if len(email_to_subscribe) > 0:
            df = pandas.read_csv("C:/Users/OLUWAGBEMINIYI/Documents/Geebee/subscribed_emails.csv")
            emails = df.to_dict(orient="list")['emails']
            if email_to_subscribe in emails:
                flash("You've already subscribed!")
                return redirect(url_for('about'))
            else:
                with open("subscribed_emails.csv", "a+") as file:
                    file.write(f"{email_to_subscribe}\n")
                with smtplib.SMTP_SSL(host, 465, context=context) as connection:
                    connection.ehlo()
                    connection.login(email, password)
                    connection.sendmail(
                        from_addr=email,
                        to_addrs="gagbedejobi@gmail.com",
                        msg=text,
                    )
    return render_template('about.html', year=year)


@app.route("/courses", methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        email_to_subscribe = request.form.get('email')
        if len(email_to_subscribe) > 0:
            df = pandas.read_csv("C:/Users/OLUWAGBEMINIYI/Documents/Geebee/subscribed_emails.csv")
            emails = df.to_dict(orient="list")['emails']
            if email_to_subscribe in emails:
                flash("You've already subscribed!")
                return redirect(url_for('courses'))
            else:
                with open("subscribed_emails.csv", "a+") as file:
                    file.write(f"{email_to_subscribe}\n")
                with smtplib.SMTP_SSL(host, 465, context=context) as connection:
                    connection.ehlo()
                    connection.login(email, password)
                    connection.sendmail(
                        from_addr=email,
                        to_addrs="gagbedejobi@gmail.com",
                        msg=text,
                    )
    return render_template('courses.html', year=year)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contact_email = request.form.get("contact-email")
        if contact_email is not None:
            with smtplib.SMTP_SSL(host="mail.privateemail.com", port=465, context=context) as connection:
                connection.ehlo()
                connection.login(user=email, password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=email,
                    msg=f"Subject:Email from {request.form.get('name')}\n\n{request.form.get('name')}, {request.form.get('contact-email')}, sent you this message:"
                        f" {request.form.get('message')}"
                )
    if request.method == 'POST':
        email_to_subscribe = request.form.get('email')
        if email_to_subscribe is not None:
            df = pandas.read_csv("C:/Users/OLUWAGBEMINIYI/Documents/Geebee/subscribed_emails.csv")
            emails = df.to_dict(orient="list")['emails']
            if email_to_subscribe in emails:
                flash("You've already subscribed!")
                return redirect(url_for('contact'))
            else:
                with open("subscribed_emails.csv", "a+") as file:
                    file.write(f"{email_to_subscribe}\n")
                with smtplib.SMTP_SSL(host, 465, context=context) as connection:
                    connection.ehlo()
                    connection.login(email, password)
                    connection.sendmail(
                        from_addr=email,
                        to_addrs=f"{email_to_subscribe}",
                        msg=text,
                    )
    return render_template("contact.html", year=year)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

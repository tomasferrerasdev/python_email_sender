""" This module is used to send email to the user when the user is registered successfully. """

import smtplib, ssl


def send_email(message):
    """This function is used to send email to the user when the user is registered successfully."""
    host = "smtp.gmail.com"
    port = 465

    username = "hellotomasdev@gmail.com"
    password = "bbeoqgefnhhakuxa"

    receiver_email = "hellotomasdev@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
        server.quit()

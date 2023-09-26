from flask import Flask, send_file, request
import datetime
import urllib.request
import urllib.error

app = Flask(__name__)


@app.route('/')
def my_function():
    spy_meme = "/home/ubuntu/git/spy-pixel/app/pixels/root_email.png"
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S")
    get_ip = request.remote_addr
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ get_ip) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")

    log_entry =f"Root Email Opened:\nTimestamp: {timestamp}\nUser Agent: {user_agent}\nIP: {get_ip}\nData: {data}\n"

    log_file_path = "/home/ubuntu/git/spy-pixel/spy_logs.txt"
    with open(log_file_path, 'a') as f:
        f.write(log_entry)

    return send_file(spy_meme, mimetype="image/png")


@app.route('/first')
def first_email():
    spy_meme = "/home/ubuntu/git/spy-pixel/app/pixels/first_email.png"
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S")
    get_ip = request.remote_addr
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ get_ip) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")

    log_entry =f"First Email Opened:\nTimestamp: {timestamp}\nUser Agent: {user_agent}\nIP: {get_ip}\nData: {data}\n"

    log_file_path = "/home/ubuntu/git/spy-pixel/spy_logs.txt"
    with open(log_file_path, 'a') as f:
        f.write(log_entry)

    return send_file(spy_meme, mimetype="image/png")



if __name__ == '__main__':
    app.run()

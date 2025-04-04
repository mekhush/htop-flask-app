from flask import Flask
import getpass
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Kushal B"  # Replace with your full name if different
    username = getpass.getuser()

    # Get current IST time
    time_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    ist_time = time_now.strftime('%Y-%m-%d %H:%M:%S')

    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    return f"""
    <h1>/htop Endpoint</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

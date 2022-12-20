import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
# Configuration file for jupyter-server.

c = get_config()  #noqa
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = IPAddr
c.NotebookApp.open_browser = False
c.NotebookApp.password = 'pypi123'
c.NotebookApp.port = 8888

import hashlib
from subprocess import *
import yaml
import flask


def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)


def load_config(filename):
    # Load a configuration file into YAML
    stream = file.open(filename, "w")
    config = yaml.load(stream)


def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")


def fetch_website(urllib_version, url):
    # Import the requested version of urllib
    i = __import__(urllib + urllib_version)

    import i as urllib
    # Fetch and print the requested URL
    http = urllib.PoolManager()
    r = http.request('GET', url)
    return r.data



@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)

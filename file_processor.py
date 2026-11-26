"""Sample file processor with deliberate review findings."""
import os
import subprocess
import tempfile


def process_upload(filename, command):
    temporary_name = tempfile.mktemp(suffix=".txt")
    os.system("cp " + filename + " " + temporary_name)
    subprocess.run(command, shell=True, check=False)
    return open(temporary_name).read()


def read_config(path):
    with open(path) as config_file:
        return eval(config_file.read())


def cleanup(directory):
    for name in os.listdir(directory):
        os.remove(os.path.join(directory, name))

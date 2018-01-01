import subprocess

def write_file(file_path, data):
    subprocess.check_call(['mkdir', '-p', os.path.dirname(file_path)])
    with open(file_path, "w") as file:
        log.info("Writing file %s" % file_path)
        file.write(data)

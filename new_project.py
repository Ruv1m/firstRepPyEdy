import subprocess


def start_stream_recording(url, output_file):
    command = ["streamlink", url, "best", "-o", output_file]
    subprocess.Popen(command)

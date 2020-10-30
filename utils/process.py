import subprocess


def command_with_output(command: [str], env):
    """ Obtain env from os.environ.copy() """
    p = subprocess.Popen(command, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        retcode = p.poll()
        line = p.stdout.read()
        yield line
        if retcode is not None:
            break

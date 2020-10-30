import os
import re

from utils.process import command_with_output


def run_docker(command, docker_image='test',
               docker_host=None,
               network=None,
               docker_params=[]):
    my_env = os.environ.copy()
    if docker_host is not None:
        my_env["DOCKER_HOST"] = docker_host
    name = get_docker_name(my_env)
    print(name)
    for line in docker(command, my_env,
                       docker_params=docker_params,
                       docker_image=docker_image,
                       network=network):
        yield line


def get_docker_name(env):
    for line in command_with_output(['docker', 'system', 'info'], env):
        x = re.search("Name: (.*)", line.decode("UTF-8"))
        if x is not None:
            group = str(x.group(1))
            return group
    return None


def docker(command, env, docker_image='test', network=None, docker_params: [str] = None):
    docker_command = ['docker', 'run', '-i', '--name', 'backup']
    if docker_params is not None:
        docker_command.extend(docker_params)
    if network is not None:
        docker_command.extend(['--network', network])
    docker_command.append(docker_image)
    docker_command.extend(command)
    print(str(" ".join(docker_command)))
    for line in command_with_output(docker_command, env=env):
        yield line

import os

from utils.docker import run_docker


def backup_docker_mongo():
    """
    conf:
    - host, port, user, pass, database
    output:
    - database_TIMESTAMP.sql
    """
    env = os.environ.copy()
    lines = []
    f = open("output2.tar.gz", "wb")
    for line in run_docker(['/bin/bash', '-c',
                            'mongodump --gzip --archive --uri="mongodb://dev_mongodb_1:27017/companyms"'],
                           docker_params=['-w', "/tmp"],
                           docker_image='mongo:4.0.20-xenial',
                           network='dev_default'):
        f.write(line)
        lines.append(line)
    f.close()
    pass


def restore_docker_mongo():
    print('restore')
    pass

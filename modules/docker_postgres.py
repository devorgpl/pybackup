import os

from utils.docker import run_docker


def backup_docker_postgres():
    """
    conf:
    - host, port, user, pass, database
    output:
    - database_TIMESTAMP.sql
    """
    env = os.environ.copy()
    env['PGPASSWORD'] = 'password'
    lines = []
    f = open("output.sql", "wb")
    for line in run_docker(['pg_dump', '-h', 'dev_keycloak_pg_1', '-U', 'keycloak', 'keycloak'],
                           docker_params=['-e', 'PGPASSWORD=password'],
                           docker_image='postgres:9.6-alpine',
                           network='dev_default'):
        f.write(line)
        lines.append(line)
    f.close()
    pass


def restore_docker_postgres():
    print('restore')
    pass

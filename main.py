from modules.docker_mongo import backup_docker_mongo
from modules.docker_postgres import backup_docker_postgres

if __name__ == '__main__':
    print('PyCharm')
    backup_docker_postgres()
    backup_docker_mongo()

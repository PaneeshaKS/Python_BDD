import configparser
import mysql.connector


# To read configurations from a properties.ini file
# and to provide a URL and header for API requests.
def get_configurations():
    """
    Reads configurations from properties.ini file.
    Returns:
        dict: A dictionary containing the configurations.
    """
    config = configparser.ConfigParser()
    path = r"C:\Users\paneek\Desktop\WorkSpace_BDD\python-bdd-project\utilities\properties.ini"
    config.read(path)
    
    # configurations = {}
    # for section in config.sections():
    #     configurations[section] = dict(config.items(section))
    
    return config

# To establish a connection to a MySQL database.
def get_my_sql_connections():
    config = get_configurations()
    db_config = {
        "host": config.get(['SQL']['host']),
        "database" : config.get(['SQL']['database']),
        "user": config.get(['SQL']['user']),
        "password": config.get(['SQL']['password'])
        }

def get_ssh_connection():
    config = get_configurations()
    ssh_config = {
        "host": config.get(['SERVER']['host']),
        "port": config.get(['SERVER']['port']),
        "username": config.get(['SERVER']['username']),
        "password": config.get(['SERVER']['password'])
    }
    return ssh_config

def get_url():
    url = "https://www.python.org/"
    return url

def get_header():
    header = {
        "x-api-key": "reqres-free-v1"
    }
    return header


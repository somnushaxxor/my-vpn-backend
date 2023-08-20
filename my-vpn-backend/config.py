from dotenv import load_dotenv
from os import environ, path

load_dotenv()

CREATE_OVPN_PROFILE_SCRIPT_PATH = environ["CREATE_OVPN_PROFILE_SCRIPT_PATH"]
OVPN_PASSPHRASE = environ["OVPN_PASSPHRASE"]
OVPN_PROFILES_DIRECTORY = environ["OVPN_PROFILES_DIRECTORY"]

ROOT = path.dirname(path.abspath(__file__))

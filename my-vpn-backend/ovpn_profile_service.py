from uuid import uuid4
from os import system, path
from config import (
    OVPN_PASSPHRASE,
    CREATE_OVPN_PROFILE_SCRIPT_PATH,
    OVPN_PROFILES_DIRECTORY,
)


class ProfileUuidAlreadyExistsError(RuntimeError):
    pass


class OvpnProfileService:
    PROFILE_FILE_SUFFIX = ".ovpn"

    @staticmethod
    def create_profile() -> str:
        profile_uuid = uuid4()
        new_profile_path = (
            OVPN_PROFILES_DIRECTORY
            + str(profile_uuid)
            + OvpnProfileService.PROFILE_FILE_SUFFIX
        )
        if path.isfile(new_profile_path):
            raise ProfileUuidAlreadyExistsError()
        system(
            f"{CREATE_OVPN_PROFILE_SCRIPT_PATH} {str(profile_uuid)} {OVPN_PROFILES_DIRECTORY} {OVPN_PASSPHRASE}"
        )
        return new_profile_path

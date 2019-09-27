import logging
from typing import List

import requests
import yaml

import restconf_helpers

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('restconf.provision')


def load_devices() -> List[dict]:
    with open('configuration.yaml', 'r') as config_file:
        devices = yaml.load(config_file.read(), Loader=yaml.FullLoader)['devices']
        return devices


def init_logger():
    _logger = logging.getLogger('restconf')
    _logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    _logger.addHandler(ch)


#def get_interfaces(host: dict) -> str:
#    response = restconf_helpers.RestconfRequestHelper().get(
#        url=f'https://{host["connection_address"]}/restconf/data/Cisco-IOS-XE-native:native/interface/',
#        username=host['username'],
#        password=host['password'])
#    return response


#def print_interfaces(host: dict) -> None:
#    print(get_interfaces(host=host))


def main():
    logger.info(f"Loading device configurations...")
    devices = load_devices()
    for device in devices:
        logger.info(f"Found configuration for device {device['devicename']} on address {device['ip_address']}")
    input("Proceed with provisioning these devices?")
#        print_interfaces(host=device)


if __name__ == '__main__':
    init_logger()
    main()

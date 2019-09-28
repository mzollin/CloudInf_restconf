import logging
from typing import List

import requests
import yaml
from jinja2 import Environment, FileSystemLoader

import restconf_helpers

requests.packages.urllib3.disable_warnings()

logger = logging.getLogger('restconf.provision')


def load_config() -> List[dict]:
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


def main():
    logger.info(f"Loading device configurations...")
    devices = load_config()
    for device in devices:
        logger.info(f"Found configuration for device {device['devicename']} on address {device['ip_address']}")
    input("Proceed with provisioning these devices?")


    for device in devices:
        for section in device['configuration']:
            print(section['section'])
            device_url = f"https://{device['ip_address']}/restconf/data/Cisco-IOS-XE-native:{section['endpoint_url']}"
            env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
            template = env.get_template(f"templates/{section['section']}.j2")
            response = requests.put(url=device_url,
                                    data=template.render(),
                                    auth=(device['username'], device['password']),
                                    verify=False    # those pesky self-signed certs
                                   )
            if not response:
                logger.error(f"Provisioning section {section['section']} on device {device['devicename']} "
                             f"failed with HTTP error {response.status_code}")


if __name__ == '__main__':
    init_logger()
    main()

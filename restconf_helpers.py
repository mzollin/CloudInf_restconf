import logging
from enum import Enum
from typing import Any, Dict

import requests
from requests import Response

logger = logging.getLogger('restconf.restconf_helpers')


class RestconfFormat(Enum):
    XML = 1
    JSON = 2


class RestconfRequestHelper:
    headers_json = {'Content-Type': 'application/yang-data+json',
                    'Accept': 'application/yang-data+json'}

    headers_xml = {'Content-Type': 'application/yang-data+xml',
                   'Accept': 'application/yang-data+xml'}

    def get(self, url: str, username: str, password: str, restconf_format: RestconfFormat = RestconfFormat.XML,
            headers: Dict[str, str] = None,
            **kwargs: Dict[Any, Any]) -> Response:
        logger.debug(f'GET request to {url}')
        request_headers = self.get_headers(restconf_format, headers)
        response = requests.request(method='GET', auth=(username, password),
                                    headers=request_headers,
                                    url=url,
                                    verify=False,
                                    **kwargs)
        logger.debug(f'Got response from {url} with code {response.status_code} and content \n {response.text}')
        response.raise_for_status()
        return response

    def get_headers(self, format: RestconfFormat, headers: Dict[str, str]) -> Dict[str, str]:
        restconf_headers = self.headers_json if format == RestconfFormat.JSON else self.headers_xml
        if headers and isinstance(headers, dict):
            headers.update(restconf_headers)
            return headers
        return restconf_headers

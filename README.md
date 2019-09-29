# CloudInf RESTCONF Automation
## Introduction
Configuring all your network devices one by one over the command line interface can be tedious. Spare your fingers and enable automation by using this model based approach which allows you to automatically provision all your devices using the RESTCONF protocol with a Python script and configuration files.

## Setup
- Install Python > 3.6 and pip
- Install the required libraries by running the command `pip install -r requirements.txt`

## Configuration
RFC 8040 (RESTCONF) states:
>Configuration data and state data are exposed as resources that can
>be retrieved with the GET method.  Resources representing
>configuration data can be modified with the DELETE, PATCH, POST, and
>PUT methods.  Data is encoded with either XML [W3C.REC-xml-20081126]
>or JSON [RFC7159]

## Usage
Prepare the configuration and template files as stated above and start the script:
`python restconf_provision.py`

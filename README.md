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

You will need to provide these resources by building XML templates for the capabilities you want to use and then writing a YAML configuration with the specific values for every device. With the templates and the configuration file this script will put together the necessary REST calls to provision your devices and send them out.

To build a template you could look for the exact YANG data model you need and create an XML template from it. The easier way is to configure one of the devices by hand over the CLI and read the XML back by reading the appropriate RESTCONF URI. Sadly, to quote Cisco Learning Labs:
>One aspect true of all REST APIs is the importance of the URI in identifying the data being requested or configured, and RESTCONF is no >exception. A unique aspect of RESTCONF is that it lacks any true "API Documentation" that a developer would use to learn how to use it. >Rather, the YANG Models themselves ARE the API documentation.

Once you got the XML you can replace the values that you want as variables with Jinja2 placeholders and add the name and value to the configuration specific to the devices.

## Usage
Prepare the configuration and template files as stated above and start the script:  
`python restconf_provision.py`

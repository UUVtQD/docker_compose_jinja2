import configparser
from jinja2 import Environment, FileSystemLoader

# Load configuration file
config = configparser.ConfigParser()
config.read('pythia.cfg')

# Convert configuration data to a dictionary (uppercase keys)
config_dict = {s: {k.upper(): v for k, v in config.items(s)} for s in config.sections()}
print(config_dict)

# Load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('docker-compose.yaml.j2')

# Render template with the configuration data
# The ** used to unpack the dictionary.
# 
rendered_output = template.render(**config_dict['SETTINGS'])
print(rendered_output)

with open('docker-compose.yaml', 'w') as f:
    f.write(rendered_output)

print('docker-compose.yaml has been generated.')

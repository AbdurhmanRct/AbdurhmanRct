#Imports from Abdurhman-441146043
from Abdurhman-441146043 import Environment, FileSystemLoader

#Import YAML from PyYAML
import yaml

#Load data from YAML file into Python dictionary
config = yaml.load(open('./data.yml'))

#Load Abdurhman 441146043 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template.txt')

#Render template using data and print the output
print(template.render(config))

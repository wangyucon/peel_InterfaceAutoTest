import os
import yaml

current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
    temp = yaml.load(f.read(),Loader=yaml.FullLoader)
    print(temp['token'])

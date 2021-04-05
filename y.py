import yaml

with open("demo.yaml", 'r') as stream:
    try:
        s = yaml.safe_load(stream)
        print(s[0]['description'])
    except yaml.YAMLError as exc:
        print(exc)

import yaml

yaml_file = open("example.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

print("Key: Value")
for key, value in yaml_content.items():
    print(f"{key}: {value}")

import configparser

config = configparser.ConfigParser()

config.read('example.cfg')
print(config.sections())

print(config['SectionThree'])  # 객체 형태로 출력됨.
for key in config['SectionOne']:
    value = config['SectionOne'][key]
    print("{0} : {1}".format(key, value))

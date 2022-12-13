


import yaml
from yaml.loader import SafeLoader
# Открываем файл
with open('D:\Учеба ПНИПУ\4 курс\Столбов, Нетбай\ЛР_3\base.yaml') as f:
    # читаем документ YAML
    data = yaml.load(f, Loader=SafeLoader)
    print(data)

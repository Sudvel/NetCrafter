import yaml
from netmiko import ConnectHandler


def connection_info_parser(show_version_command: str):
    '''
    Устанавливет соединение с коммутатор для получения 
    вывода команды просмотра информации об устройстве.

    Args:
        show_version_command: Команда просмотра версии.

    Returns: void (пока)
    '''
    with open("string_router.yaml", "r") as file:
        data = yaml.safe_load(file)  # Считываем файл с описанием.
        # Команда просмотра версии - список коммутаторов, которые соответствуют этой команде.

    device_group = data[show_version_command]  # Список возможных коммутаторов.
    one_connection_device_type = device_group[0]  # Можно взять первый коммутатор, т.к команда просмотра версии одинаковая.

    router = {
        'device_type': one_connection_device_type,
        'host': 'clab-switch_3_clab-ceos',
        'username': 'admin',
        'password': 'admin',
        'port': 22,  # По дефолту порт 22.
    }

    net_connect = ConnectHandler(**router)  # Уствновка соединения.

    output = net_connect.send_command(show_version_command)  # Отправка команды просмотра версии.

    print(output)  # Пока что вывод в консоль.

    net_connect.disconnect()  # Разрыв соединения.


connection_info_parser('show version')

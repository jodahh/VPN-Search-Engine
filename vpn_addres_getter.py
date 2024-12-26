import requests
from bs4 import BeautifulSoup

i = 0

litSSTP = ["Protocol: SSTP\nLogin: vpn\nPassword: vpn\n"]

litL2TP = ["Protocol: L2TP\nShared key: vpn\nLogin: vpn\nPassword: vpn\n"]

litOpenVPN = ['Protocol: OpenVPN\n']

# URL веб-страницы
def sstp_protocol_vpn():
    url = 'https://ipspeed.info/freevpn_sstp.php?language=ru'
    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все элементы с классом 'list' и стилем 'width: 373px;'
        host_elements = soup.find_all('div', class_='list', style=lambda s: s and 'width: 373px;' in s)
        host_countrys = soup.find_all('div', class_='list', style=lambda f: f and 'width: 263px;' in f)
        host_ping = soup.find_all('div', class_='list', style=lambda f: f and 'width: 120px;' in f)
        host_uptime = soup.find_all('div', class_='list', style=lambda f: f and 'width: 180px;' in f)
        
        # Проходим по всем найденным элементам
        for i in range(len(host_elements)):
            host_name = host_elements[i].get_text(strip=True)
            host_countr = host_countrys[i].get_text(strip=True)
            ping = host_ping[i].get_text(strip=True)
            uptime = host_uptime[i].get_text(strip=True)
            # print(host_name)
        # Пропускаем заголовок "ИМЯ ХОСТА"
            if "ИМЯ ХОСТА" not in host_name and "ПИНГ" not in ping and "РАСПОЛОЖЕНИЕ" not in host_countr and "ВРЕМЯ РАБОТЫ" not in uptime:

                litSSTP.append(f"\nHost Name: {host_name}\nCountry: {host_countr}\nPing: {ping}\nUptime: {uptime}\n")
        return litSSTP

    else:
        print(f"Ошибка запроса: {response.status_code}")

def l2tp_protocol_vpn():
    url = 'https://ipspeed.info/freevpn_l2tpipsec.php?language=ru'
    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все элементы с классом 'list' и стилем 'width: 373px;'
        host_elements = soup.find_all('div', class_='list', style=lambda s: s and 'width: 373px;' in s)
        host_countrys = soup.find_all('div', class_='list', style=lambda f: f and 'width: 263px;' in f)
        host_ping = soup.find_all('div', class_='list', style=lambda f: f and 'width: 120px;' in f)
        host_uptime = soup.find_all('div', class_='list', style=lambda f: f and 'width: 180px;' in f)
        
        # Проходим по всем найденным элементам
        for i in range(len(host_elements)):
            host_name = host_elements[i].get_text(strip=True)
            host_countr = host_countrys[i].get_text(strip=True)
            ping = host_ping[i].get_text(strip=True)
            uptime = host_uptime[i].get_text(strip=True)
            # print(host_name)
        # Пропускаем заголовок "ИМЯ ХОСТА"
            if "ИМЯ ХОСТА" not in host_name and "ПИНГ" not in ping and "РАСПОЛОЖЕНИЕ" not in host_countr and "ВРЕМЯ РАБОТЫ" not in uptime:

                litL2TP.append(f"\nHost NAme: {host_name}\nCountry: {host_countr}\nPing: {ping}\nUptime: {uptime}\n")
        return litL2TP

    else:
        print(f"Ошибка запроса: {response.status_code}")

def open_vpn_protocol_vpn():
    url = 'https://ipspeed.info/freevpn_openvpn.php?language=ru'
    # Выполняем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все элементы с классом 'list' и стилем 'width: 373px;'
        host_elements = soup.find_all('div', class_='list', style=lambda s: s and 'width: 373px;' in s)
        host_countrys = soup.find_all('div', class_='list', style=lambda f: f and 'width: 263px;' in f)
        host_ping = soup.find_all('div', class_='list', style=lambda f: f and 'width: 120px;' in f)
        host_uptime = soup.find_all('div', class_='list', style=lambda f: f and 'width: 180px;' in f)
        
        # Проходим по всем найденным элементам
        for i in range(len(host_elements)):
            # host_name = host_elements[i].get_text(strip=True)[: len(host_elements[i].get_text(strip=True)) // 2]
            host_name = host_elements[i].get_text(strip=True)

            if host_name.count('ovpn') == 2 and "ИМЯ ХОСТА" not in host_name and "ПИНГ" not in ping and "РАСПОЛОЖЕНИЕ" not in host_countr and "ВРЕМЯ РАБОТЫ" not in uptime:
                list_host = host_name.split('.ovpn')
                host_name_one = list_host[0] + '.ovpn'
                host_name_two = list_host[1] + '.ovpn'
                # print(host_name_one,"\n",host_name_two)
                litOpenVPN.append(f"\nHost Name 1: {host_name_one}\nHost Name 2: {host_name_two}\nCountry: {host_countr}\nPing: {ping}\nUptime: {uptime}\n")

            host_countr = host_countrys[i].get_text(strip=True)
            ping = host_ping[i].get_text(strip=True)
            uptime = host_uptime[i].get_text(strip=True)
            # print(host_name)
        # Пропускаем заголовок "ИМЯ ХОСТА"
            if "ИМЯ ХОСТА" not in host_name and "ПИНГ" not in ping and "РАСПОЛОЖЕНИЕ" not in host_countr and "ВРЕМЯ РАБОТЫ" not in uptime:
                litL2TP.append(f"\nHost NAme: {host_name}\nCountry: {host_countr}\nPing: {ping}\nUptime: {uptime}\n")
        return litOpenVPN

    else:
        print(f"Ошибка запроса: {response.status_code}")

# open_vpn_protocol_vpn()
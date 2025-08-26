# 配置来源

## shodan

https://account.shodan.io/

## fofa

https://fofa.info/userInfo

## hunter

https://hunter.qianxin.com/home/myInfo

## quake

https://quake.360.net/quake/#/personal

## chinaz

https://user.chinaz.net/servicesPurchased/myApi

## aiwen

通过账号密码登录即可

# 脚本配置运行

安装 query_sdk

`python3 setup.py install`

## 配置文件

通过json内容配置各个服务阈值

- shodan，fofa，hunter，quake 支持多API检查

```text

config_str = '''
{
  "shodan": {
    "apikey": ["x"],
    "credit": 50
  },
  "fofa": {
    "apikey": ["x"],
    "credit": 8000
  },
  "hunter": {
    "apikey": ["x","x","x"],
    "credit": 400000
  },
  "quake": {
    "apikey": ["x"],
    "credit": 50000
  },
  "aiwen": {
    "username": "13888888888",
    "password": "123456",
    "credit": {
      "IPv4行业-API": 50000,
      "IPv4应用场景-API": -1,
      "IP宿主信息-API": -1,
      "IPv4归属地-API（区县级）": 30000,
      "IPv4归属地-API（高精准-商业版）": 30000
    }
  },
  "chinaz": {
    "apikey": "x",
    "config": {
      "ICP域名备案实时查询": 100,
      "企业备案实时查询": 100
    }
  }
}
'''
```

## SDK使用方法

```text
import json
from query_sdk import get_results

if __name__ == '__main__':
    # 使用 eval 解析配置文件
    config = json.loads(config_str)

    # 获取结果
    results = get_results(config)

    # 打印结果
    print(json.dumps(results, indent=4, ensure_ascii=False))
```

返回值如下所示

- 空间测绘类型，对应APIKEY的值为TRUE的情况下则代表已经超过了阈值，可进行短信通知提醒
- aiwen及chinaz类型，对应各个服务的值为TRUE的情况下则代表已经超过了阈值，可进行短信通知提醒

```text

{
    "shodan": {
        "x": true
    },
    "fofa": {
        "x": true
    },
    "hunter": {
        "x": false,
        "x": true,
        "x": false
    },
    "quake": {
        "x": true
    },
    "aiwen": {
        "IPv4行业-API": false,
        "IPv4应用场景-API": false,
        "IP宿主信息-API": false,
        "IPv4归属地-API（区县级）": true,
        "IPv4归属地-API（高精准-商业版）": true
    },
    "chinaz": {
        "ICP域名备案实时查询": true,
        "企业备案实时查询": false
    }
}
```
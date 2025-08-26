import json

from query_sdk import get_results

# 配置文件内容
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
    "apikey": ["x-x-x-x-x"],
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


if __name__ == '__main__':
    # 使用 eval 解析配置文件
    config = json.loads(config_str)

    # 获取结果
    results = get_results(config)

    # 打印结果
    print(json.dumps(results, indent=4, ensure_ascii=False))

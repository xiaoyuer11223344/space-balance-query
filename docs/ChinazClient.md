
# ChinazClient 文档

## 概述

`ChinazClient` 是一个客户端类，用于与 Chinaz API 交互，获取用户的各种 API 的剩余使用量。

## 初始化
- **参数**：
  - `api_key` (List[str]): 用户的 API 密钥列表。
  - `base_url` (str): 默认为 `"https://userapi.chinaz.net/api/api"`。

## 方法：`get_remain_count`

### 功能

获取 Chinaz 用户的各种 API 的剩余使用量。

### 返回值

返回一个字典，主键为服务名称，值为剩余使用量。

```text
{'ICP域名备案实时查询': 10, '企业备案实时查询': 2099}
```
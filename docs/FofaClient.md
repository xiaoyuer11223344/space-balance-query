# FofaClient 文档

## 概述

`FofaClient` 是一个客户端类，用于与 FOFA API 交互，获取用户的剩余积分信息。

## 初始化
- **参数**：
  - `api_key` (List[str]): 用户的 API 密钥列表。
  - `base_url` (str): 默认为 `"https://fofa.info/api/v1"`。

## 方法：`get_remain_count`

### 功能

获取 FOFA 用户的剩余积分（`fofa_point`）。

### 返回值

返回一个字典，主键为API_KEY，值为剩余使用量

```text
{
    'e106b567-7f7d-4894-a340-f53122dc3d13': 47763
}
```
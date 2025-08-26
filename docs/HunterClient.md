
# HunterClient 文档

## 概述
`HunterClient` 是一个客户端类，用于与 Hunter API 交互，获取用户的剩余点数信息。

## 初始化
- **参数**：
  - `api_key` (List[str]): 用户的 API 密钥列表。
  - `base_url` (str): 默认为 `"https://hunter.qianxin.com/openApi"`。

## 方法：`get_remain_count`

### 功能

获取 Hunter 用户的剩余点数（`rest_equity_point`）。

### 返回值

返回一个字典，主键为API_KEY，值为剩余使用量

{
    '2bcf13b782f4319bb4537944d386a11f06256c77b8daade4a6fb9c9f3be73f06': 1686537
}
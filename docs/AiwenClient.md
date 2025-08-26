
# AiwenClient 文档

## 概述

`AiwenClient` 是一个客户端类，用于与 Aiwen API 交互，获取用户的各种服务的剩余使用量。

## 初始化

- **参数**：
  - `username` (str): 用户名。
  - `password` (str): 密码。
  - `base_url` (str): 默认为 `"https://account.ipplus360.com"`。

## 方法：`get_remain_count`

### 功能

获取 Aiwen 用户的各种服务的剩余使用量。

### 返回值

返回一个字典，主键为服务名称，值为剩余使用量。

```text
{
    'IPv4行业-API': 82487,
    'IPv4应用场景-API': 0,
    'IP宿主信息-API': 0,
    'IPv4归属地-API（区县级）': 12093,
    'IPv4归属地-API（高精准-商业版）': 29956
}
```

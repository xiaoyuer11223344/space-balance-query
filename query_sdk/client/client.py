# coding=utf-8

from typing import Type, List

from pydantic import BaseModel, ValidationError
import requests

from query_sdk.model.aiwen import LoginResponse, BalanceResponse
from query_sdk.model.chinaz import ChinazResponse
from query_sdk.model.fofa import FofaInfoResponse
from query_sdk.model.hunter import HunterResponse, HunterPersonalData, HunterEnterpriseData
from query_sdk.model.quake import QuakeResponse
from query_sdk.model.shodan import ShodanResponse


class QueryClient:
    def __init__(self, api_key: List, base_url: str):
        self.base_url = base_url
        self.api_key = api_key

    def _request(self, method: str, endpoint: str, **kwargs):
        """
        内部方法，用于发送 HTTP 请求并返回 JSON 数据
        :param method: HTTP 方法（如 GET、POST）
        :param endpoint: API 端点路径
        :param kwargs: 额外的请求参数（如 headers、params、data 等）
        :return: 响应数据（JSON 格式）
        """
        # 默认的 headers
        default_headers = {
            "Content-Type": "application/json"
        }

        # 如果用户通过 kwargs 提供了自定义 headers，则合并到默认 headers 中
        headers = {**default_headers, **kwargs.pop("headers", {})}

        # 构造完整的 URL
        url = f"{self.base_url}/{endpoint}"

        # 发送请求
        response = requests.request(method, url, headers=headers, **kwargs)

        # 检查响应状态码
        if response.status_code >= 400:
            raise Exception(f"Error {response.status_code}: {response.text}")

        return response.json()

    def _parse_response(self, data: dict, base_model: Type[BaseModel]):
        """
        内部方法，用于解析和验证响应数据
        :param data: 原始 JSON 数据
        :param model: Pydantic 模型类
        :return: 验证后的模型实例
        """
        if not isinstance(base_model, type) or not issubclass(base_model, BaseModel):
            raise TypeError("base_model must be a subclass of BaseModel")

        try:
            return base_model(**data)  # 使用 Pydantic 模型解析数据
        except ValidationError as e:
            raise ValueError(f"Response validation failed: {e}")

    def login(self):
        """获取登录信息"""
        return self._request("GET", "/")

    def get_remain_count(self):
        """获取用户信息"""
        return self._request("GET", "/")


class FofaClient(QueryClient):
    """
    curl -X GET "https://fofa.info/api/v1/info/my?key={api-key}""
    """

    BASE_URL = "https://fofa.info/api/v1"

    def __init__(self, api_key: List):
        super().__init__(api_key, self.BASE_URL)

    def get_remain_count(self):
        """获取 FOFA 用户信息

        返回值：{'d8f6b3363a6460601299d144196c1597': 6076}

        抽象化：{_api_key: 剩余量}
        """
        response_data = {}
        for _api_key in self.api_key:
            raw_data = self._request("GET", "info/my", params={"key": _api_key}, verify=False)
            response = self._parse_response(raw_data, FofaInfoResponse)
            response_data[_api_key] = response.fofa_point
        return response_data


class HunterClient(QueryClient):
    """
    curl -X GET -k "https://hunter.qianxin.com/openApi/userInfo?api-key={api-key}"
    """

    BASE_URL = "https://hunter.qianxin.com/openApi"

    def __init__(self, api_key: List):
        super().__init__(api_key, self.BASE_URL)

    def get_remain_count(self):
        """获取 Hunter 用户信息

        返回值：{'{api-key}"': 1686537}

        抽象化：{_api_key: 剩余量}
        """
        response_data = {}
        for _api_key in self.api_key:
            params = {"api-key": _api_key}
            raw_data = self._request("GET", "userInfo", params=params, verify=False)
            # print(raw_data)  # 打印原始数据便于调试
            response = self._parse_response(raw_data, HunterResponse)
            # 根据账号类型提取剩余量
            if isinstance(response.data, HunterPersonalData):
                response_data[_api_key] = response.data.rest_equity_point
            elif isinstance(response.data, HunterEnterpriseData):
                response_data[_api_key] = response.data.rest_equity_point
        return response_data


class QuakeClient(QueryClient):
    """
    curl -X GET "https://quake.360.net/api/v3/user/info" -H "X-QuakeToken: {api-key}""
    """

    BASE_URL = "https://quake.360.net/api/v3"

    def __init__(self, api_key: List):
        super().__init__(api_key, self.BASE_URL)

    def get_remain_count(self):
        """获取 Quake 用户信息

        返回值：{'{api-key}"': 47763}

        抽象化：{_api_key: 剩余量}
        """
        response_data = {}
        for _api_key in self.api_key:
            headers = {"X-QuakeToken": _api_key}
            raw_data = self._request("GET", "user/info", headers=headers, verify=False)
            response = self._parse_response(raw_data, QuakeResponse)
            response_data[_api_key] = response.data.credit
        return response_data


class ShodanClient(QueryClient):
    """
    curl -X GET "https://api.shodan.io/api-info?key={api-key}""
    """

    BASE_URL = "https://api.shodan.io"

    def __init__(self, api_key: List):
        super().__init__(api_key, self.BASE_URL)

    def get_remain_count(self):
        """获取 Shodan 账户信息


        返回值：{'{api-key}"': 39}

        抽象化：{_api_key: 剩余量}
        """
        response_data = {}
        for _api_key in self.api_key:
            params = {"key": self.api_key}
            raw_data = self._request("GET", "api-info", params=params)
            response = self._parse_response(raw_data, ShodanResponse)
            response_data[_api_key] = response.query_credits
        return response_data


class AiwenClient(QueryClient):
    BASE_URL = "https://account.ipplus360.com"
    BASE_MAIL_URL = "https://mall.ipplus360.com"

    LOGIN_URL = "api/blade-auth/oauth/token"
    QUERY_URL = "infos/ordersInfo"

    def __init__(self, username: str, password: str):
        super().__init__(api_key=[], base_url=self.BASE_URL)
        self.username = username
        self.password = password

    def login(self):
        """
        登录获取 access_token
        """
        headers = {
            "Authorization": "Basic c3dvcmQ6c3dvcmRfc2VjcmV0",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        payload = {
            "username": self.username,
            "password": self.password,
            "valicode": "",
            "grant_type": "captcha",
        }

        # 发送登录请求
        raw_data = self._request("POST", self.LOGIN_URL, headers=headers, data=payload)
        # 解析并验证登录响应
        login_response = self._parse_response(raw_data, LoginResponse)
        self.api_key = login_response.access_token

    def get_remain_count(self):

        # 第一步：登录获取 access_token
        self.login()

        """
        获取余量信息
        
        返回值：{'IPv4行业-API': 82487, 'IPv4应用场景-API': 0, 'IP宿主信息-API': 0, 'IPv4归属地-API（区县级）': 12093, 'IPv4归属地-API（高精准-商业版）': 29956}
        
        抽象化：{'服务API名称': 剩余量}
                
        """
        if not self.api_key:
            raise ValueError("请先调用 login 方法获取 access_token")

        self.base_url = self.BASE_MAIL_URL
        headers = {
            "Blade-Auth": f"{self.api_key}",
            "Content-Type": "application/json;charset=UTF-8",
        }

        data = {"currPage": 1, "pageSize": 100}

        # 发送余额查询请求
        raw_data = self._request("POST", self.QUERY_URL, headers=headers, json=data)

        # print(raw_data)
        # 解析并验证余额响应
        balance_response = self._parse_response(raw_data, BalanceResponse)

        result = {}
        for item in balance_response.dict().get("data", {}).get("list", []):
            order_info_vo = item.get("orderInfoVo")
            if order_info_vo:  # 检查 orderInfoVo 是否存在
                name = order_info_vo.get("productName", "Unknown")
                tokens = item.get("tokens", [])

                for token in tokens:
                    if name == "IPv4应用场景-API":
                        # 使用 sceneCounts 字段
                        count = token.get("sceneCounts", 0)
                    else:
                        # 使用 counts 字段
                        count = token.get("counts", 0)

                    # 累加到结果字典
                    if name in result:
                        result[name] += count
                    else:
                        result[name] = count

        return result


class ChinazClient(QueryClient):
    """
    curl -X GET "https://userapi.chinaz.net/api/api/getApiList?expireType=&pageSize=10&pageIndex=1 -H 'Cookie: xxxx'"
    """

    BASE_URL = "https://userapi.chinaz.net/api/api"

    def __init__(self, api_key: List):
        super().__init__(api_key, self.BASE_URL)

    def get_remain_count(self):
        """获取 Chinaz 账户信息

        返回内容：

        {_api_key: {'ICP域名备案实时查询': 10, '企业备案实时查询': 2099}}

        """
        response_data = {}

        for _api_key in self.api_key:

            params = {"expireType": "", "pageSize": 100, "pageIndex": 1}

            # 设置请求头
            headers = {
                "Auth-Token": _api_key,
                "Content-Type": "application/json;charset=UTF-8",
            }

            raw_data = self._request("GET", "getApiList", params=params, headers=headers)

            # 解析响应数据
            response = self._parse_response(raw_data, ChinazResponse)

            # 遍历 data 字段并构建字典
            for item in response.data:
                response_data[item.apiName] = item.totalUsableCount - item.usedCount

        return response_data

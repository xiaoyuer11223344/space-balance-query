# coding=utf-8
from typing import Union

from pydantic import BaseModel, Field


# 定义个人用户信息模型
class PersonalInfo(BaseModel):
    user_name: str = Field(..., description="用户名")
    phone: str = Field(..., description="手机号")
    is_charge: bool = Field(..., description="是否为充值用户")


# 定义企业用户信息模型
class EnterpriseInfo(BaseModel):
    account: str = Field(..., description="企业账号")
    start_time: str = Field(..., description="账号开始时间")
    end_time: str = Field(..., description="账号结束时间")


# 定义公共字段的数据模型
class HunterDataCommon(BaseModel):
    type: str = Field(..., description="账号类型")
    rest_equity_point: int = Field(..., description="剩余权益点数")
    rest_export_quota: int = Field(..., description="剩余导出配额")
    day_export_quota: int = Field(..., description="每日导出配额")
    once_export_quota: int = Field(..., description="单次导出配额")


# 定义个人用户的数据模型
class HunterPersonalData(HunterDataCommon):
    personal_info: PersonalInfo = Field(..., description="个人用户信息")
    rest_free_point: int = Field(..., description="剩余免费点数")
    day_free_point: int = Field(..., description="每日免费点数")


# 定义企业用户的数据模型
class HunterEnterpriseData(HunterDataCommon):
    enterprise_info: EnterpriseInfo = Field(..., description="企业用户信息")


# 定义顶层响应模型
class HunterResponse(BaseModel):
    code: int = Field(..., description="状态码")
    data: Union[HunterPersonalData, HunterEnterpriseData] = Field(..., description="数据内容")
    message: str = Field(..., description="消息")

    class Config:
        extra = 'allow'  # 允许额外字段

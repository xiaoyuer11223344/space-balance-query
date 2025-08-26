# coding=utf-8

from pydantic import BaseModel, Field
from typing import List, Optional


class Role(BaseModel):
    fullname: str = Field(..., description="角色名称")
    priority: int = Field(..., description="优先级")
    credit: int = Field(..., description="信用额度")


class PrivacyLog(BaseModel):
    status: bool = Field(..., description="隐私日志状态")
    time: Optional[str] = Field(None, description="时间")


class EnterpriseInformation(BaseModel):
    name: Optional[str] = Field(None, description="企业名称")
    email: Optional[str] = Field(None, description="企业邮箱")
    status: str = Field(..., description="认证状态")


class User(BaseModel):
    id: str = Field(..., description="用户ID")
    username: str = Field(..., description="用户名")
    fullname: str = Field(..., description="全名")
    email: str = Field(..., description="邮箱")


class QuakeData(BaseModel):
    id: str = Field(..., description="用户唯一标识")
    user: User = Field(..., description="用户信息")
    baned: bool = Field(..., description="是否被封禁")
    ban_status: str = Field(..., description="封禁状态")
    credit: int = Field(..., description="信用额度")
    persistent_credit: int = Field(..., description="持久信用额度")
    token: str = Field(..., description="Token")
    mobile_phone: Optional[str] = Field(None, description="手机号码")
    source: str = Field(..., description="来源")
    privacy_log: PrivacyLog = Field(..., description="隐私日志")
    enterprise_information: EnterpriseInformation = Field(..., description="企业信息")
    personal_information_status: bool = Field(..., description="个人信息状态")
    role: List[Role] = Field(..., description="角色列表")


class QuakeResponse(BaseModel):
    code: int = Field(..., description="状态码")
    message: str = Field(..., description="消息")
    data: QuakeData = Field(..., description="数据内容")
    meta: dict = Field({}, description="元数据")

    class Config:
        extra = 'allow'  # 允许额外字段# coding=utf-8

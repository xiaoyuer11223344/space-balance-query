# coding=utf-8

from pydantic import BaseModel, Field


# 定义 Pydantic 模型
class FofaInfoResponse(BaseModel):
    error: bool = Field(..., description="是否出现错误")
    email: str = Field(..., description="邮箱地址")
    username: str = Field(..., description="用户名")
    category: str = Field(..., description="用户种类")
    fcoin: int = Field(..., description="F币")
    fofa_point: int = Field(..., description="F点")
    remain_free_point: int = Field(..., description="剩余免费F点")
    remain_api_query: int = Field(..., description="API月度剩余查询次数")
    remain_api_data: int = Field(..., description="API月度剩余返回数量")
    isvip: bool = Field(..., description="是否是会员")
    vip_level: int = Field(..., description="会员等级")
    is_verified: bool = Field(..., description="是否已验证")
    avatar: str = Field(..., description="头像链接")
    message: str = Field("", description="消息")
    fofacli_ver: str = Field(..., description="FOFA CLI 版本")
    fofa_server: bool = Field(..., description="是否为 FOFA 服务器")

    class Config:
        extra = 'allow'  # 允许额外字段
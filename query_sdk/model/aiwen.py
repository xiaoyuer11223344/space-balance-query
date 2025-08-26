from typing import List, Optional
from pydantic import BaseModel


# 定义登录响应模型
class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str
    user_name: str
    reg_form: str
    mobile: str
    description: str
    avatar: str
    uuid: str
    client_id: str
    organizationId: str
    thirdSource: str
    user_id: str
    grant_type: str
    nickname: str
    key: str
    email: str
    jti: str


# Token 模型
class Token(BaseModel):
    index: str
    token: str
    createdDate: int
    expireDate: Optional[int] = None  # 将 expireDate 设置为可选
    productId: int
    available: bool
    notified: bool
    testCount: int
    counts: int
    dailyLimit: int
    canWebLocate: bool
    countsToYear: Optional[str] = None  # 将 countsToYear 设置为可选
    test: bool


# OrderInfoVo 模型
class OrderInfoVo(BaseModel):
    uuid: str
    id: int
    orderSerial: str
    price: float
    status: int
    dateCreated: int
    dateUpdated: int
    isInvoice: int
    paymentMethod: int
    productId: int
    productName: str
    amountStr: str
    productType: int
    itemNum: int


# ListItem 模型
class ListItem(BaseModel):
    orderInfoVo: OrderInfoVo
    tokens: List[Token]
    fileOrders: Optional[List[dict]] = None
    isShew: Optional[bool] = None
    sort: Optional[str] = None


# BalanceData 模型
class BalanceData(BaseModel):
    currPage: int
    totalPage: int
    pageSize: int
    list: List[ListItem]
    allCount: int
    hasNextPage: bool


# BalanceResponse 模型
class BalanceResponse(BaseModel):
    success: bool
    code: int
    data: BalanceData
    msg: str

    class Config:
        extra = 'allow'  # 允许额外字段

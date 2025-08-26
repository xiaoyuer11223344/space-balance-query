# coding=utf-8
from pydantic import BaseModel, Field
from typing import List, Optional


class ApiItem(BaseModel):
    createTime: str
    updateTime: str
    status: int
    id: str
    userId: int
    goodsId: str
    goodsApiId: Optional[str] = None
    interfaceId: str
    apiName: str
    apiKey: str
    queryIp: Optional[str] = None
    isOpen: int
    packageType: int
    remark: Optional[str] = None
    totalUsableCount: int
    usedCount: int
    endDate: str
    onlyDate: Optional[str] = None
    categoryName: str
    expireStatus: int
    exhaustStatus: int
    goodsType: int
    docUrl: str
    goodsName: str
    supplierApiId: Optional[str] = None
    goodsRandomId: str
    minEndDate: Optional[str] = None


class ChinazResponse(BaseModel):
    code: int
    msg: str
    success: bool
    data: Optional[List[ApiItem]] = None  # 允许 data 为 None
    timeStamp: int

    class Config:
        extra = 'allow'  # 允许额外字段

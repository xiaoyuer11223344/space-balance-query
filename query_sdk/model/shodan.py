# coding=utf-8

from pydantic import BaseModel, Field


class UsageLimits(BaseModel):
    scan_credits: int = Field(default=-1, description="Scan credits limit")
    query_credits: int = Field(default=-1, description="Query credits limit")
    monitored_ips: int = Field(default=-1, description="Monitored IPs limit")


class ShodanResponse(BaseModel):
    scan_credits: int = Field(default=0, description="Available scan credits")
    usage_limits: UsageLimits = Field(default_factory=UsageLimits, description="Usage limits details")
    plan: str = Field(default="default", description="Plan name")
    https: bool = Field(default=False, description="HTTPS enabled flag")
    unlocked: bool = Field(default=False, description="Unlocked status")
    query_credits: int = Field(default=0, description="Available query credits")
    monitored_ips: int = Field(default=0, description="Number of monitored IPs")
    unlocked_left: int = Field(default=0, description="Remaining unlocked credits")
    telnet: bool = Field(default=False, description="Telnet enabled flag")

    class Config:
        extra = 'allow'  # 允许额外字段

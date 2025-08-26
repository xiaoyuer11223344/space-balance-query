# coding=utf-8

class RemainSdkError(Exception):
    """Base exception for MySDK"""
    pass


class AuthenticationError(RemainSdkError):
    """Raised when authentication fails"""
    pass


class APIError(RemainSdkError):
    """Raised when an API request fails"""
    pass

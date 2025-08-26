# setup.py

from setuptools import setup, find_packages

setup(
    # 包的基本信息
    name="query_sdk",  # 包名，用户通过 pip install query-sdk 安装时使用
    version="0.1.0",  # 版本号，遵循语义化版本控制（major.minor.patch）
    author="Your Name",  # 作者名
    author_email="your.email@example.com",  # 作者邮箱
    description="A Python SDK for querying APIs with a simple interface.",  # 简短描述
    long_description=open("../README.md").read(),  # 长描述，通常从 README 文件读取
    long_description_content_type="text/markdown",  # 长描述的内容类型（Markdown 格式）

    # 自动发现包及其子模块
    packages=find_packages(),  # 自动查找所有包和子包

    # 依赖项
    install_requires=[
        "requests>=2.32.3",  # 示例：需要 requests 库
        "pydantic>=2.11.1",  # 示例：需要 pydantic 库
    ],

    # 分类信息
    classifiers=[
        "Programming Language :: Python :: 3",  # 支持的 Python 版本
        "License :: OSI Approved :: MIT License",  # 许可证类型
        "Operating System :: OS Independent",  # 操作系统兼容性
    ],

    # 最低 Python 版本要求
    python_requires=">=3.7",

    # 可选：包含非 Python 文件（如配置文件、文档等）
    include_package_data=True,
)
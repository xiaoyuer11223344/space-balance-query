from query_sdk.client.client import QuakeClient, AiwenClient, ChinazClient, ShodanClient, FofaClient, HunterClient
from query_sdk.utils.utils import check_remain_count

__all__ = ["get_results"]  # 明确指定只暴露 get_results 方法


def get_results(config):
    """
    根据查询参数获取结果。

    :param query: 查询字符串
    :param config_path: 配置文件路径，默认为 "config.json"
    :return: 查询结果
    """

    results = {}

    # ShodanClient 测试
    if "shodan" in config:
        shodan_api_keys = config["shodan"]["apikey"]
        shodan_client = ShodanClient(shodan_api_keys)
        try:
            shodan_remain_count = shodan_client.get_remain_count()
            results["shodan"] = check_remain_count("shodan", shodan_remain_count, int(config["shodan"]["credit"]))
        except Exception as e:
            results["shodan"] = f"Error: {str(e)}"

    # FofaClient 测试
    if "fofa" in config:
        fofa_api_keys = config["fofa"]["apikey"]
        fofa_client = FofaClient(fofa_api_keys)
        try:
            fofa_remain_count = fofa_client.get_remain_count()
            results["fofa"] = check_remain_count("fofa", fofa_remain_count, int(config["fofa"]["credit"]))
        except Exception as e:
            results["fofa"] = f"Error: {str(e)}"

    # HunterClient 测试
    if "hunter" in config:
        hunter_api_keys = config["hunter"]["apikey"]
        hunter_client = HunterClient(hunter_api_keys)
        try:
            hunter_remain_count = hunter_client.get_remain_count()
            results["hunter"] = check_remain_count("hunter", hunter_remain_count, int(config["hunter"]["credit"]))
        except Exception as e:
            results["hunter"] = f"Error: {str(e)}"

    # QuakeClient 测试
    if "quake" in config:
        quake_api_keys = config["quake"]["apikey"]
        quake_client = QuakeClient(quake_api_keys)
        try:
            quake_remain_count = quake_client.get_remain_count()
            results["quake"] = check_remain_count("quake", quake_remain_count, int(config["quake"]["credit"]))
        except Exception as e:
            results["quake"] = f"Error: {str(e)}"

    # AiwenClient 测试
    if "aiwen" in config:
        aiwen_username = config["aiwen"]["username"]
        aiwen_password = config["aiwen"]["password"]
        aiwen_client = AiwenClient(aiwen_username, aiwen_password)
        try:
            aiwen_remain_count = aiwen_client.get_remain_count()
            results["aiwen"] = check_remain_count('aiwen', aiwen_remain_count, config['aiwen']['credit'])
        except Exception as e:
            results["aiwen"] = f"Error: {str(e)}"

    # ChinazClient 测试
    if "chinaz" in config:
        chinaz_api_keys = [config["chinaz"]["apikey"]]
        chinaz_client = ChinazClient(chinaz_api_keys)
        try:
            chinaz_remain_count = chinaz_client.get_remain_count()
            results["chinaz"] = check_remain_count("chinaz", chinaz_remain_count, config['chinaz']['config'])
        except Exception as e:
            results["chinaz"] = f"Error: {str(e)}"

    return results

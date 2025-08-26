# coding=utf-8

def check_remain_count(service_name, remain_count, expected_credit):
    """检查实际剩余量是否小于预期值"""
    if isinstance(remain_count, dict) and isinstance(expected_credit, dict):
        # 如果两者都是字典，则递归检查每个键值对
        results = {}
        for key in expected_credit:
            if key in remain_count:
                if isinstance(remain_count[key], int) and isinstance(expected_credit[key], int):
                    if remain_count[key] < expected_credit[key]:
                        # print(f"[{service_name}] {key}: 实际剩余量 ({remain_count[key]}) < 配置值 ({expected_credit[key]})")
                        results[key] = True
                    else:
                        results[key] = False
                else:
                    # print(f"[{service_name}] {key}: 数据类型不匹配 (实际: {type(remain_count[key])}, 预期: {type(expected_credit[key])})")
                    results[key] = False
            else:
                # print(f"[{service_name}] {key}: 实际剩余量中缺少该字段")
                results[key] = False
        return results

    elif isinstance(remain_count, dict) and isinstance(expected_credit, int):
        # 如果 remain_count 是字典，而 expected_credit 是整数
        results = {}
        for key, actual_value in remain_count.items():
            if isinstance(actual_value, int):
                if actual_value < expected_credit:
                    # print(f"[{service_name}] {key}: 实际剩余量 ({actual_value}) < 配置值 ({expected_credit})")
                    results[key] = True
                else:
                    results[key] = False
            else:
                # print(f"[{service_name}] {key}: 数据类型不匹配 (实际: {type(actual_value)}, 预期: {type(expected_credit)})")
                results[key] = False
        return results

    elif isinstance(remain_count, int) and isinstance(expected_credit, int):
        # 如果两者都是整数，则直接比较
        if remain_count < expected_credit:
            # print(f"[{service_name}] 实际剩余量 ({remain_count}) < 配置值 ({expected_credit})")
            return True
        return False

    else:
        # 数据类型不匹配，返回 False
        # print(f"[{service_name}] 数据类型不匹配 (实际: {type(remain_count)}, 预期: {type(expected_credit)})")
        return False
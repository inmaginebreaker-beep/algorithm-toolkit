class AlgorithmToolkitError(Exception):
    """Algorithm Toolkit 的基础异常。"""


class InvalidInputError(AlgorithmToolkitError):
    """输入数据不符合要求时抛出。"""


class AlgorithmNotFoundError(AlgorithmToolkitError):
    """指定算法不存在时抛出。"""

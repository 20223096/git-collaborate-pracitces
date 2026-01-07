"""
통계 함수 모듈

담당: 팀원 :isak
브랜치: feature/statistics
"""

from typing import List


def mean(numbers: List[float]) -> float:
    """숫자 리스트의 평균을 반환합니다.

    Args:
        numbers: 숫자 리스트

    Returns:
        평균값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20])
        15.0
    """
    # TODO: 구현하세요
    # 힌트: 빈 리스트 체크 필요
    if not numbers:
        raise ValueError("ValueError: 빈 리스트입니다.")
    return sum(numbers) / len(numbers)  


def median(numbers: List[float]) -> float:
    """숫자 리스트의 중앙값을 반환합니다.

    중앙값: 정렬했을 때 가운데 위치한 값
    - 홀수 개: 가운데 값
    - 짝수 개: 가운데 두 값의 평균

    Args:
        numbers: 숫자 리스트

    Returns:
        중앙값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> median([1, 3, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
    """
    # TODO: 구현하세요
    # 힌트: sorted()로 정렬 후 가운데 값 찾기
    if not numbers: 
        raise ValueError("ValueError: 빈 리스트입니다.")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2                  


def mode(numbers: List[float]) -> float:
    """숫자 리스트의 최빈값을 반환합니다.

    최빈값: 가장 자주 나타나는 값
    동일한 빈도의 값이 여러 개면 가장 먼저 나온 값을 반환

    Args:
        numbers: 숫자 리스트

    Returns:
        최빈값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> mode([1, 2, 2, 3, 3, 3])
        3
        >>> mode([1, 1, 2, 2])
        1
    """
    # TODO: 구현하세요
    # 힌트: 딕셔너리로 빈도수 카운트
    if not numbers:
        raise ValueError("ValueError: 빈 리스트입니다.")
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_frequency = max(frequency.values())
    for num, freq in frequency.items():
        if freq == max_frequency:
            return num


def variance(numbers: List[float]) -> float:
    """숫자 리스트의 분산을 반환합니다.

    분산: 각 값과 평균의 차이의 제곱의 평균

    Args:
        numbers: 숫자 리스트

    Returns:
        분산값

    Raises:
        ValueError: 빈 리스트일 경우

    Examples:
        >>> variance([1, 2, 3, 4, 5])
        2.0
    """
    # TODO: 구현하세요
    # 힌트: 먼저 평균을 구한 후, 각 값과 평균의 차이의 제곱을 구하고 평균
    if not numbers:
        raise ValueError("ValueError: 빈 리스트입니다.")
    avg = mean(numbers)
    squared_diffs = [(x - avg) ** 2 for x in numbers]
    return mean(squared_diffs)  



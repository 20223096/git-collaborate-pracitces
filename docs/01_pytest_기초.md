# pytest 기초 가이드

## 1. pytest란?

**pytest**는 Python에서 가장 널리 사용되는 테스트 프레임워크입니다.

### 왜 테스트가 필요한가?

```python
# 이런 함수를 작성했다고 가정해봅시다
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 잘 동작하는 것 같지만...
print(calculate_average([1, 2, 3]))  # 2.0 ✓

# 빈 리스트를 넣으면?
print(calculate_average([]))  # ZeroDivisionError! 💥
```

테스트를 작성하면 이런 버그를 **코드를 배포하기 전에** 발견할 수 있습니다.

### print 테스트 vs pytest

❌ **print로 테스트하는 경우 (비추천)**
```python
def add(a, b):
    return a + b

# 직접 눈으로 확인해야 함
print(add(1, 2))  # 3이 나오면 성공...인가?
print(add(-1, 1)) # 0이 나와야 하는데...
```

문제점:
- 매번 눈으로 결과를 확인해야 함
- 테스트가 많아지면 관리 불가능
- 자동화 불가능

✅ **pytest로 테스트하는 경우 (추천)**
```python
def add(a, b):
    return a + b

def test_add_positive():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, 1) == 0
```

장점:
- 자동으로 성공/실패 판정
- 한 번에 모든 테스트 실행
- CI/CD 파이프라인과 연동 가능

---

## 2. pytest 설치 및 실행

### 설치

```bash
# pip으로 설치
pip install pytest

# 또는 requirements.txt 사용
pip install -r requirements.txt
```

### 실행 방법

```bash
# 모든 테스트 실행
pytest

# 특정 파일만 실행
pytest tests/test_calculator.py

# 특정 테스트 함수만 실행
pytest tests/test_calculator.py::test_add_positive

# 상세 출력 (-v: verbose)
pytest -v

# 특정 이름 패턴의 테스트만 실행 (-k: keyword)
pytest -k "add"
```

### 실행 결과 예시

```
==================== test session starts ====================
collected 3 items

tests/test_calculator.py::test_add_positive PASSED     [ 33%]
tests/test_calculator.py::test_add_negative PASSED     [ 66%]
tests/test_calculator.py::test_add_zero PASSED         [100%]

==================== 3 passed in 0.02s ====================
```

- `PASSED`: 테스트 성공 ✅
- `FAILED`: 테스트 실패 ❌
- `ERROR`: 테스트 실행 중 에러 발생

---

## 3. 테스트 파일 작성 규칙

### 파일명 규칙

pytest가 자동으로 찾는 파일:
- `test_*.py` (추천) - 예: `test_calculator.py`
- `*_test.py` - 예: `calculator_test.py`

### 함수명 규칙

pytest가 테스트로 인식하는 함수:
- `test_`로 시작하는 함수

```python
# ✅ pytest가 인식함
def test_addition():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"

# ❌ pytest가 인식하지 못함
def addition_test():  # test_로 시작하지 않음
    assert 1 + 1 == 2

def check_addition():  # test_가 없음
    assert 1 + 1 == 2
```

### 클래스 사용 (선택)

관련 테스트를 그룹화할 때 유용:

```python
class TestCalculator:
    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(5, 3) == 2
```

---

## 4. assert 문 사용법

### 기본 사용법

```python
# 값이 같은지 확인
assert result == expected

# 에러 메시지 추가 (실패 시 출력됨)
assert result == expected, f"Expected {expected}, but got {result}"
```

### 다양한 비교

```python
# 같음
assert add(1, 2) == 3

# 같지 않음
assert add(1, 2) != 0

# 크기 비교
assert find_max([1, 5, 3]) > 0
assert len(result) >= 1

# 포함 여부
assert "hello" in "hello world"
assert 5 in [1, 3, 5, 7]

# 타입 확인
assert isinstance(result, list)
assert isinstance(result, (int, float))

# True/False
assert is_valid == True
assert not is_empty

# None 확인
assert result is None
assert result is not None
```

### 예외 테스트

특정 예외가 발생하는지 확인:

```python
import pytest

def test_divide_by_zero():
    # divide(10, 0)이 ZeroDivisionError를 발생시키는지 확인
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_invalid_input():
    # "hello" + 1이 TypeError를 발생시키는지 확인
    with pytest.raises(TypeError):
        result = "hello" + 1
```

---

## 5. 실습 예제

### 프로젝트 구조

```
Day02_Git-Team-Collaboration/
├── src/
│   └── calculator.py    # 테스트할 코드
├── tests/
│   └── test_calculator.py  # 테스트 코드
└── pytest.ini
```

### src/calculator.py

```python
def add(a: float, b: float) -> float:
    """두 수의 합을 반환합니다."""
    return a + b

def divide(a: float, b: float) -> float:
    """두 수의 나눗셈 결과를 반환합니다."""
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다")
    return a / b
```

### tests/test_calculator.py

```python
import pytest
from src.calculator import add, divide

def test_add_positive_numbers():
    """양수 덧셈 테스트"""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """음수 덧셈 테스트"""
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    """양수와 음수 덧셈 테스트"""
    assert add(-1, 1) == 0

def test_divide_normal():
    """정상적인 나눗셈 테스트"""
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    """0으로 나누기 예외 테스트"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

### 테스트 실행

```bash
# 프로젝트 루트에서 실행
pytest -v

# 결과
tests/test_calculator.py::test_add_positive_numbers PASSED
tests/test_calculator.py::test_add_negative_numbers PASSED
tests/test_calculator.py::test_add_mixed_numbers PASSED
tests/test_calculator.py::test_divide_normal PASSED
tests/test_calculator.py::test_divide_by_zero PASSED
```

---

## 6. 자주 발생하는 문제

### ModuleNotFoundError

```
ModuleNotFoundError: No module named 'src'
```

**해결 방법**: 프로젝트 루트 디렉토리에서 pytest 실행

```bash
# 잘못된 방법
cd tests
pytest test_calculator.py

# 올바른 방법
cd Day02_Git-Team-Collaboration
pytest tests/test_calculator.py
```

### 테스트 함수가 인식되지 않음

```python
# ❌ test_가 없어서 인식 안됨
def calculate_test():
    assert 1 + 1 == 2

# ✅ 올바른 명명
def test_calculate():
    assert 1 + 1 == 2
```

---

## 7. 다음 단계

pytest 기초를 익혔다면, 이제 팀 협업 실습을 시작합니다!

👉 [02_팀_워크플로우.md](02_팀_워크플로우.md)로 이동하세요.

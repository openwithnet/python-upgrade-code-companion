# Part IV. 패러다임의 조합과 소프트웨어 설계

# Chapter 9. 계약, 타입과 프로그램 검증

> **문서 상태:** 상세 재구성 검토본. 기존 채팅의 원고 전체와 문장별 축자 대조가 수행되지 않았으므로 출판 원고가 아니며 NOT FROZEN.
> **실행 상태:** 첨부 기준 코드에서 42개 pytest 테스트 재통과. 일부 본문 코드는 교육용 부분 예제.

## Part IV Introduction

앞의 Part에서는 함수, 객체, 상속과 합성, 인터페이스를 학습하였다. Part IV에서는 이러한 구성 요소를 연결하면서 과학 프로그램이 어떤 조건에서 신뢰할 수 있는 결과를 제공하는지 다룬다.

소프트웨어가 올바르게 작동하는 것과 과학적 모델이 실제 문제에 적절한 것은 별개의 검증 대상이다. 코드 구조의 정합성, 수치 오차, 입력 데이터의 의미를 함께 고려해야 한다.

## Chapter 9 Introduction — 실행 가능한 프로그램에서 신뢰할 수 있는 프로그램으로

실행 성공은 프로그램 검증의 출발점일 뿐이다. 선형 보정식 s=ac+b의 역산식은 c=(s-b)/a이다. 이 식을 올바르게 구현했더라도 a=0, 비유한 입력, 단위 불일치, 부적합한 보정 모델은 별도로 고려해야 한다.

이번 장은 계약, 타입과 데이터 검증, pytest, 수치 정확도, 측정 단위 및 과학적 타당성을 연결한다. 예제는 Chapter 8의 C3 Calibration Program을 재사용한다.

**핵심 관계식:** c = (s − b) / a

## 9.1 프로그램의 정확성과 계약

프로그램의 구문적 정확성, 실행 가능성, 수학적 정확성, 계약 준수, 수치적 정확성과 과학적 타당성은 구분해야 한다. 요구사항을 올바르게 구현했는지 확인하는 Verification과 실제 목적에 맞는지 평가하는 Validation도 구별한다.

입력과 출력의 기대 조건을 명확하게 기술하면 프로그램의 실패를 분석하기 쉽다.

## 9.1.1 프로그램이 올바르다는 것의 의미

반지름 r에 대한 원의 넓이는 πr²이다. 코드가 2πr을 반환하더라도 Python 문법과 타입에는 문제가 없을 수 있다. 이 사례는 실행 가능한 코드와 수학적으로 정확한 코드를 구별한다.

음의 반지름을 어떻게 처리할지 명확하게 정하지 않았다면 올바른 계산식도 잘못된 입력에 사용할 수 있다.

Verification은 구현의 정확성을, Validation은 사용 목적에 대한 모델의 적합성을 평가한다. 두 활동 모두 필요하다.

**핵심 관계식:** A = πr²

```python
import math

def area_of_circle(radius: float) -> float:
    if radius < 0:
        raise ValueError("radius must be nonnegative")
    return math.pi * radius**2
```

## 9.1.2 Design by Contract

계약 기반 설계는 함수의 호출자가 충족해야 할 조건과 함수가 정상 완료 시 제공해야 할 결과를 명시한다. Python의 타입 주석은 계약 일부를 전달하지만 실행 시 자동 검증하지는 않는다.

C3에서는 유한한 실수, 양의 계수, 모델별 신호 유효 영역을 검사한다. TypeError는 잘못된 자료형, ValueError는 허용되지 않은 수치 조건에 사용한다.

문서 문자열에는 수학식과 단위 및 사용 가능 범위를 기술한다. 계약을 모든 하위 함수에서 무차별적으로 반복 검증하는 대신 검증 책임을 명확히 배치한다.

## 9.1.3 사전조건·사후조건·불변조건

사전조건은 함수 호출 전에 필요한 조건, 사후조건은 정상적인 결과의 보장, 불변조건은 객체의 유효한 상태에서 계속 유지되어야 하는 조건이다.

C3의 사전조건은 유한한 신호와 모델의 유효 영역이다. 사후조건은 유한한 비음수 농도와 모델 수학식의 만족이다. 불변조건은 유한한 보정 계수와 양의 기울기 또는 제곱 응답 계수이다.

외부 입력 검증에는 assert 대신 명시적인 if와 예외를 사용한다. assert는 -O 옵션에 의해 제거될 수 있으므로 필수 런타임 검증에 적합하지 않다.

**핵심 관계식:** a > 0; k > 0; s ≥ b; c ≥ 0

## 9.2 타입과 데이터 검증

과학 데이터의 유효성은 자료형, 값의 범위, 단위 및 과학적 의미에 의해 결정된다. float은 온도와 농도를 구분하지 않는다.

## 9.2.1 Type Hints의 역할

Type Hints는 매개변수, 반환값, 변수 및 객체 속성의 기대 자료형을 표현한다. list[float]은 숫자 목록, float | None은 실수 또는 결측 상태를 나타낼 수 있다.

@dataclass(frozen=True)는 일반적인 속성 변경을 제한하지만 생성 시 전달된 값의 타입을 자동 검증하지 않는다. Literal["V", "mV"]도 실행 시 문자열의 값을 강제하지 않는다.

따라서 타입 주석은 문서화와 정적 분석의 기반이지만 실제 측정 데이터 검증을 대신할 수 없다.

```python
from typing import Protocol

class CalibrationModel(Protocol):
    def predict_concentration(self, signal: float) -> float:
        ...
```

## 9.2.2 정적 타입 검사와 실행 시 검증

mypy와 Pyright 같은 정적 검사기는 실행 전에 타입 호환성 문제를 찾을 수 있다. 그러나 계산식이 올바른지, 신호가 유한한지, 단위가 적절한지는 일반적으로 판단하지 못한다.

실행 시 검증은 실제 값에 대해 isinstance(), math.isfinite(), 범위 조건을 적용한다. bool은 int의 하위 타입이므로 이번 C3에서는 별도로 거부한다.

거대한 정수를 float으로 변환할 때 OverflowError가 발생할 수 있으므로 유한성 검증에서 이러한 예외도 고려한다.

```python
import math

def finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result
```

## 9.2.3 유효하지 않은 데이터와 예외 처리

결측값(None이나 빈 문자열로 명시한 상태)과 잘못된 측정값은 구분해야 한다. 문자를 수치로 변환하지 못한 경우 임의의 0.0으로 대체하면 실제 영농도와 혼동된다.

예외를 호출자에게 전달할지, 특정 관측값을 제외하고 상태를 기록할지는 분석 정책에 따라 결정한다. 광범위한 except Exception: return 0.0 같은 패턴은 원인을 은폐한다.

V와 mV처럼 서로 다른 단위를 혼용한 상태에서 숫자만 비교하면 과학적 오류가 생길 수 있다. 단위는 별도로 검증하거나 단위가 포함된 객체로 표현한다.

```python
def parse_measurement(text: str) -> float | None:
    if not isinstance(text, str):
        raise TypeError("measurement must be a string")
    value = text.strip()
    if not value:
        return None
    try:
        return finite_real(float(value), "measurement")
    except ValueError as exc:
        raise ValueError("invalid measurement") from exc
```

## 9.3 테스트 가능한 프로그램

자동 테스트는 선택된 입력에서 약속된 계산과 예외가 발생하는지 확인한다. 테스트의 통과는 모든 가능한 입력에서 결함이 없다는 증명은 아니다.

## 9.3.1 단위 테스트

테스트는 Arrange(준비), Act(실행), Assert(검증)의 순서로 작성할 수 있다. 기대 결과는 가급적 테스트 대상 함수와 독립적으로 구한다.

반복해 같은 함수를 두 번 호출한 결과를 비교하는 테스트는 동일한 버그를 발견하지 못할 수 있다. 경계값, 이상값, 입력 유형을 함께 검사한다.

회귀 테스트는 프로그램 수정 이후 기존의 검증된 행동이 유지되는지 확인하는 데 사용한다.

```python
import math
from c3_calibration import LinearCalibration

model = LinearCalibration(slope=2.0, intercept=1.0)
assert math.isclose(model.predict_concentration(9.0), 4.0)
```

## 9.3.2 pytest 기본

pytest에서는 test_로 시작하는 함수와 테스트 파일을 수집한다. pytest.mark.parametrize를 사용하면 여러 테스트 사례를 중복 없이 실행할 수 있다. pytest.raises는 예상된 예외를 확인하고 pytest.approx는 수치의 근사 비교에 활용한다.

프로그램과 테스트 코드를 별도 파일로 관리하면 기준 구현과 검증 책임을 구분할 수 있다. 테스트의 기대값 역시 잘못될 수 있으므로 실패 원인을 점검해야 한다.

```python
import pytest
from c3_calibration import LinearCalibration

@pytest.mark.parametrize("signal, expected", [(1.0, 0.0), (3.0, 1.0), (9.0, 4.0)])
def test_linear_known_values(signal, expected):
    model = LinearCalibration(2.0, 1.0)
    assert model.predict_concentration(signal) == pytest.approx(expected)
```

## 9.3.3 경계조건·오류 사례 테스트

C3에서 s=b이면 농도 0으로 해석한다. s<b는 교육용 계약의 유효 영역 밖이므로 ValueError를 발생시킨다. 양의 계수 조건을 위반한 0 또는 음의 기울기 역시 모델 생성 시 거부한다.

str, bool, None에 대해 TypeError, nan과 inf에 대해 ValueError가 발생하는지 테스트한다. frozen dataclass의 일반적인 속성 대입에서 FrozenInstanceError가 발생하는지도 검증한다.

테스트 케이스는 단순한 개수보다 공통 계약과 경계 및 실패 조건을 얼마나 충실히 표현하는지가 중요하다.

```python
import pytest
from c3_calibration import LinearCalibration

def test_lower_bound():
    model = LinearCalibration(2.0, 1.0)
    assert model.predict_concentration(1.0) == 0.0
    with pytest.raises(ValueError):
        model.predict_concentration(0.0)
```

## 9.4 과학계산의 검증

수치적 정확성은 자료형과 계산식의 정확성만으로 설명되지 않는다. 유한 정밀도의 부동소수점 계산은 반올림 및 근사 오차를 가진다.

## 9.4.1 부동소수점·수치 오차

대부분의 Python 환경에서 float은 IEEE 754 binary64 형식이다. 0.1은 이진 부동소수점으로 정확히 표현되지 않으며 0.1+0.2==0.3이 False일 수 있다.

반올림 오차는 유한 정밀도에 의한 것이고 절단 오차는 무한하거나 연속적인 수학 과정을 유한한 근사로 바꾸면서 발생한다.

전진차분 (f(x+h)-f(x))/h에서 h를 무조건 작게 하면 정확도가 계속 개선되는 것은 아니다. 지나치게 작은 h에서 상쇄로 유효숫자를 잃을 수 있다.

조건수는 문제 자체가 입력 오차에 얼마나 민감한지 표현한다. 선형 보정 c=(s-b)/a에서 신호가 Δs만큼 변할 때 Δc=Δs/a이며 작은 a는 큰 농도 변화로 이어질 수 있다.

**핵심 관계식:** Δc = Δs / a

```python
def forward_difference(f, x: float, h: float) -> float:
    if h == 0:
        raise ValueError("h must not be zero")
    return (f(x + h) - f(x)) / h
```

## 9.4.2 허용오차·근사 비교

절대오차는 |x̂−x|, 상대오차는 |x̂−x|/|x|이며 기준값이 0이면 상대오차를 그대로 사용할 수 없다.

math.isclose(a,b)는 |a−b| ≤ max(rel_tol×max(|a|,|b|), abs_tol)을 사용한다. pytest.approx(expected)는 기대값을 기준으로 상대 허용오차를 평가한다.

허용오차가 지나치게 크면 오류가 가려지고, 지나치게 작으면 무해한 반올림 차이에도 실패한다. 수치 알고리즘과 계산 규모, 실험 요구사항에 따라 기준을 정한다.

**핵심 관계식:** |a−b| ≤ max(rel_tol × max(|a|,|b|), abs_tol)

```python
import math
assert math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-12, abs_tol=1e-12)
```

## 9.4.3 프로그램 검증과 과학적 타당성의 차이

Verification은 계산이 정의된 요구사항과 수학식을 올바르게 구현했는지, Validation은 실제 사용 목적에서 모델이 적절한지 평가한다.

실제 신호가 s=2c²+1일 때 c=3의 신호는 19이다. 이를 선형식 s=2c+1로 역산하면 c=9가 된다. 선형 계산은 정확하지만 모델 선택은 부적합하다.

부동소수점 오차와 측정 불확실성은 다르다. 신호의 불확실성이 0.2, 기울기가 2라면 계수를 정확한 상수로 보는 단순화 아래 농도 변화 크기는 약 0.1이다. 실제 분석에서는 계수 불확실성 및 상관관계도 고려한다.

**핵심 관계식:** s = 2c² + 1; c=3 ⇒ s=19; 선형 역산 ⇒ c=9

## 9.5 실습: Calibration Program 검증

기존 C3 모델은 변경하지 않고 외부 입력의 자료형과 단위 검증을 수행하는 계층을 추가한다. 원래 모델은 mV 단위의 신호를 입력받는다고 계약을 정한다.

## 9.5.1 측정값과 단위의 유효성

0.009 V와 9.0 mV는 같은 전압이다. SignalMeasurement는 value와 unit을 함께 저장하고, V/mV만 허용하며, 값의 유한성을 확인한다.

as_millivolts()는 V를 mV로 변환한다. 유한한 입력도 1000을 곱하는 과정에서 무한대가 될 수 있으므로 변환 결과를 다시 검사해야 한다.

보정 계수는 mV 신호에 대응하는 계수여야 한다. 단위 변환을 수행한다고 해서 서로 다른 단위로 추정된 계수가 자동으로 호환되지는 않는다.

**핵심 관계식:** 0.009 V = 9.0 mV

```python
from c3_validation import SignalMeasurement
measurement = SignalMeasurement(0.009, "V")
assert measurement.as_millivolts() == 9.0
```

## 9.5.2 계산 함수와 객체의 계약

analyze_measurements()는 각 측정값을 mV로 정규화한 다음 기존 analyze_many()에 전달한다. 모델은 내부에서 선형식 또는 제곱 응답식의 역산을 수행한다.

입력 계층과 모델 계산 계층이 분리되어 있어 단위 변환만 독립 테스트할 수 있고 모델을 교체해도 분석 함수의 호출 구조는 유지된다.

입력 [0.001 V, 3 mV, 0.009 V]는 [1,3,9] mV이다. 선형 모델의 출력은 [0,1,4], 제곱 응답 모델의 출력은 [0,1,2]가 된다.

```python
from c3_calibration import LinearCalibration, QuadraticCalibration
from c3_validation import SignalMeasurement, analyze_measurements

inputs = [SignalMeasurement(0.001, "V"), SignalMeasurement(3.0, "mV"), SignalMeasurement(0.009, "V")]
print(analyze_measurements(inputs, LinearCalibration(2.0, 1.0)))
print(analyze_measurements(inputs, QuadraticCalibration(2.0, 1.0)))
```

## 9.5.3 회귀 결과 및 예외 사례 검증

단위 표현만 다른 두 신호 0.009 V와 9 mV는 같은 농도를 생성해야 한다. 기존 C3 테스트 16개와 측정·단위 검증 16개를 합쳐 앞서 32개가 통과했다.

추가 회귀 테스트에서는 모델별 절편, 빈 입력, 입력 순서 보존, 잘못된 계수, 경계 아래 입력 등 기존 테스트가 놓치기 쉬운 사례를 점검하였다. 이후 총 42개 테스트가 통과한 기록을 확보하였다.

이러한 테스트가 실험 기반의 보정 계수 추정, 불확실성 전파, 장비 검출한계를 검증한 것은 아니다.

```python
import pytest
from c3_calibration import LinearCalibration
from c3_validation import SignalMeasurement, analyze_measurements

model = LinearCalibration(2.0, 1.0)
measurements = [SignalMeasurement(0.009, "V"), SignalMeasurement(9.0, "mV")]
assert analyze_measurements(measurements, model) == pytest.approx([4.0, 4.0])
```

## 9.6 신뢰할 수 있는 프로그램 설계

검증 가능성을 고려하여 프로그램을 구성하면 오류를 발견하는 데 드는 비용이 줄어들고, 모델의 변경에도 기존 계약을 유지하기 쉬워진다.

## 9.6.1 검증 가능성과 테스트 용이성

하나의 함수에 파일 읽기, 단위 변환, 수학적 계산, 시각화와 저장까지 집중시키면 테스트 범위와 책임이 불명확해진다.

SignalMeasurement는 단위와 입력 상태, analyze_measurements는 연결, CalibrationModel은 수학적 계산을 담당한다. 각 부분을 독립 테스트할 수 있다.

외부에서 모델 객체를 인수로 전달하는 의존성 주입 방식은 테스트용 대체 객체로 호출 여부를 확인할 수 있게 한다. 하지만 작은 계산마다 과도한 클래스를 생성할 필요는 없다.

## 9.6.2 계약과 인터페이스의 관계

Protocol은 메서드의 형태를 표현하지만 유한한 농도와 비음수 결과 등의 과학적 계약을 자동으로 보장하지 않는다.

predict_concentration()가 항상 -999.0을 반환하는 구현도 메서드 구조만으로는 호환되어 보일 수 있다. 공통 계약 테스트는 이러한 의미적 오류를 발견하는 데 도움을 준다.

모델별 수학식이 다르다는 이유만으로 계약 위반은 아니다. 공통 입력 영역, 단위, 반환값의 의미와 오류 정책을 일치시키면서 개별 수학적 결과는 허용한다.

## 9.6.3 과학적 가정과 한계의 명시

이번 C3 모델은 양의 계수, 비음수 농도, 신호 s≥b를 가정한다. 이 제약을 모든 종류의 보정 문제에 적용되는 보편적 법칙으로 이해해서는 안 된다.

결과 재현을 위해 사용한 모델, 계수, 원본 신호와 단위, 데이터 출처, 적용 범위, 코드 버전, 불확실성 등의 메타데이터를 관리할 수 있다.

테스트를 통과한 범위와 실제 과학적 검증이 이뤄지지 않은 영역을 명시한다. 현재 예제는 실제 장비의 보정 범위, 계수 추정, 검출한계 및 불확실성 전파를 다루지 않는 교육용 프로그램이다.

## 9.7 Chapter Summary — 과학 프로그램의 신뢰성과 검증

Chapter 9에서는 프로그램이 실행되는 것에서 출발하여 계약의 정의, Type Hints와 실행 검증, 단위 테스트, 수치 오차와 Validation까지 학습하였다.

Type Hints는 기대 자료형을 표현하지만 자동 런타임 검증이 아니다. pytest는 선택된 사례에 대한 동작과 오류 정책을 확인한다. math.isclose는 수치 비교의 허용오차를 정의하지만 측정 불확실성을 보정하지 않는다.

Chapter 8은 교체 가능한 인터페이스를 설계했고 Chapter 9는 교체된 구현이 계약을 지키며 수학적 결과를 올바르게 제공하는지 검증했다.

신뢰할 수 있는 과학 프로그램은 올바른 입력·출력 조건을 기술하고, 그 조건을 테스트하며, 모델의 적용 범위와 검증되지 않은 한계를 함께 밝히는 프로그램이다.

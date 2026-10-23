# Chapter 8. 추상화, 인터페이스와 교체 가능한 객체

> **INTEGRATED REVIEW — NOT FROZEN**  | 원본 화면 원고의 축자 전사본이 아닌 **재구성 검토본**. 누락 없는 출판 원고로 간주하지 말 것.

## Introduction — 구현보다 계약에 의존하는 프로그램

Chapter 6에서는 상태와 책임, Chapter 7에서는 상속·합성·다형성을 학습하였다. Chapter 8에서는 여러 구현이 공유하는 인터페이스를 설계하고, 과학적 동작 계약이 유지되는 범위에서 모델을 교체하는 방법을 살펴본다.

C3 사례는 측정 신호 s로부터 농도 c를 추정하는 보정 모델이다. 선형식 s = ac + b와 제곱 응답식 s = kc² + b는 서로 다른 과학적 가정을 사용하지만 공통 메서드 predict_concentration(signal)를 제공할 수 있다. 이때 같은 메서드 이름은 계산 결과의 동등성을 뜻하지 않는다.

이 장의 목적은 추상화를 과도하게 늘리는 것이 아니라 구현과 계약, 소프트웨어 검증과 과학적 검증의 차이를 이해하는 것이다.

## 8.1 추상화와 인터페이스

추상화는 특정 목적에 필요한 성질을 선택한다. 과학적 추상화는 모델링할 변수와 관계를 선택하고, 소프트웨어 추상화는 외부 사용자가 의존할 인터페이스를 정한다. 하나의 보정 모델만 있는 간단한 경우에는 독립 함수로 충분하다. 여러 모델을 바꿔 사용해야 할 때 추상화가 이점을 제공한다.

### 8.1.1 추상화의 역할

과학적 모델은 현실의 모든 복잡성을 다루지 않는다. 예를 들어 운동 방정식 dx/dt = v와 dv/dt = a는 위치와 속도를 중심으로 현상을 표현한다. 같은 방식으로 보정 모델도 신호와 농도 사이의 관계를 특정 수학식으로 추상화한다.

소프트웨어는 이 모델을 실행하기 위한 공개 계약을 추상화한다. predict_concentration(signal)는 농도 추정을 요청한다는 의미를 담지만 실제 역산식은 구현에 맡긴다. 추상화의 질은 감춘 코드의 양보다 공개 계약의 명확성에 좌우된다.

### 8.1.2 구현과 인터페이스의 분리

구체적인 함수 analyze_signal(signal, slope, intercept)가 선형식을 내부에 고정하면 비선형 보정 모델로 교체하기 어렵다. 대신 analyze_signal(signal, model)처럼 모델 객체를 전달받게 만들면 선택된 모델에 계산을 위임할 수 있다.

선형 모델의 농도는 (s-b)/a, 제곱 응답 모델의 농도는 sqrt((s-b)/k)로 계산된다. 분석 함수는 두 계산식의 차이를 몰라도 된다. 그렇다고 두 모델의 결과나 적용 범위가 동일해지는 것은 아니다.

### 8.1.3 인터페이스를 통한 결합도 감소

분석 함수가 특정 구현을 직접 생성하거나 계수에 접근하지 않으면 해당 구현의 변경이 분석 절차에 미치는 영향을 줄일 수 있다. 모델을 함수 인수로 외부에서 주입하는 것만으로도 간단한 의존성 주입을 구현할 수 있다.

인터페이스는 모든 의존성을 제거하지 않는다. 호출자는 여전히 어떤 모델을 생성하여 전달할지 결정해야 한다. 또한 추상화 자체의 추가 코드와 테스트 비용도 고려해야 한다.

## 8.2 Python의 인터페이스 표현

Python은 명목적 상속 기반 ABC, 구조적 타이핑 기반 Protocol, 동적 호출을 활용하는 Duck Typing을 제공한다. 세 접근은 서로 경쟁하지 않으며 시스템의 목적에 따라 함께 사용될 수 있다.

### 8.2.1 Abstract Base Class (ABC)

abc.ABC와 @abstractmethod로 필수 메서드를 명시한다. 미구현 추상 메서드가 남은 클래스는 인스턴스화할 수 없다. ABC는 관리되는 상속 계층이나 공통 구현이 필요한 라이브러리에 적합할 수 있다. 그러나 추상 메서드의 존재는 수학적 올바름을 검증하지 않으며 반환값 형식을 자동으로 강제하지도 않는다.

### 8.2.2 Protocol

typing.Protocol은 모델이 제공해야 할 메서드의 구조를 나타낸다. 구현 클래스가 Protocol을 직접 상속할 필요는 없다. 정적 타입 검사 도구는 해당 구조에 부합하는지 확인할 수 있으나 실제 함수 호출에서 자동으로 과학적 계약을 검증하지 않는다. @runtime_checkable도 제한적인 구조 확인에 그친다.

외부 라이브러리의 독립적인 모델 객체를 동일 분석 함수에 연결할 때 Protocol이 유용하다. 다만 입력 단위나 결과 의미가 다르면 구조적으로 호환되어도 직접 교체할 수 없다.

### 8.2.3 Duck Typing

Duck Typing은 구체적인 클래스보다 객체가 제공하는 실제 동작에 주목한다. model.predict_concentration(signal)을 직접 호출할 수 있다면 별도의 인터페이스 선언은 필수가 아니다. 작은 Python 프로그램에서는 매우 자연스러운 방식이다.

다만 잘못된 객체는 런타임에 AttributeError 등을 발생시킬 수 있다. hasattr 검사 역시 메서드의 인수와 과학적 의미까지 보장하지 못한다. 계약 문서화와 테스트가 중요하다.

## 8.3 다형성과 교체 가능성

다형성은 동일한 호출 형식으로 다른 구현을 이용할 수 있게 한다. 안전한 교체 가능성은 구조적 호환성을 넘어 의미적 동작 계약을 요구한다.

### 8.3.1 공통 인터페이스의 의미

predict_concentration(signal: float) -> float이라는 명세만으로 입력 신호 단위, 반환 농도 단위, 유효 범위, 계수 추정 조건, 모델 불확실성을 알 수 없다. 과학적 계약은 구조적 계약보다 넓다.

동일한 신호 9를 입력했을 때 선형 모델은 4, 제곱 응답 모델은 2를 반환한다. 이는 서로 다른 모델식에 따른 결과이며 다형성 위반이 아니다.

### 8.3.2 구현 교체와 호환성

대체 가능성을 판단하려면 사전조건과 사후조건을 검토해야 한다. 공통 인터페이스가 허용하는 입력에 대해 구현이 더 강한 추가 조건을 요구한다면 안전한 교체가 어려울 수 있다. 반환값의 물리 단위가 달라져도 문제가 생긴다.

이번 예제는 두 모델에 c ≥ 0, 양의 보정계수, s ≥ b라는 제한을 의도적으로 둔다. 절편은 모델별 매개변수이므로 각 구현의 유효 영역이 다를 수 있다. 일반적인 선형 모델에서 기울기가 반드시 양수여야 하는 것은 아니다.

### 8.3.3 인터페이스와 동작 계약

동작 계약은 유효한 입력, 계산 결과, 오류 처리, 객체의 상태 불변조건을 규정한다. 잘못된 자료형은 TypeError, 비유한 값이나 정의역 위반은 ValueError로 취급한다.

공통 계약 테스트는 유한한 비음수 결과를 확인할 수 있지만 수학식이 올바른지는 별도 모델별 테스트가 필요하다. 실제 실험 자료에서 모델의 적합성이 좋은지 확인하는 과학적 검증은 다시 별개의 문제이다.

## 8.4 실습: 교체 가능한 Calibration Model

C3 통합 구현은 불변 dataclass로 두 종류의 모델을 표현하고 공통 Protocol에 따라 계산한다. 실행 가능한 전체 기준 코드는 별도 c3_calibration.py 파일로 제공한다. 여기의 발췌는 해당 기준 구현에서 가져온 것이다.

### 8.4.1 모델의 공통 연산 정의

공통 연산 predict_concentration(signal)은 유한한 기본 수치형 신호를 받아 유한한 비음수 농도를 반환한다. 각 모델의 매개변수는 유한하며 slope > 0 또는 coefficient > 0이다. 신호는 모델의 절편 미만일 수 없다.

자료형 명세 float는 런타임 검증을 대신하지 않는다. finite_real()은 bool, 문자열, nan, inf를 거부하고 큰 정수의 float 변환 오버플로도 검사한다.

### 8.4.2 서로 다른 모델 구현

LinearCalibration은 c = (s-b)/a, QuadraticCalibration은 c = sqrt((s-b)/k)를 계산한다. 두 구현은 frozen dataclass로 매개변수를 보관하고 __post_init__에서 유효성을 검증한다.

선형 모델에 a=2, b=1, s=9를 주면 c=4이고, 제곱 응답 모델에 k=2, b=1, s=9를 주면 c=2이다. 이 모델들은 교육용 무차원 계산이며 실제 보정 데이터를 적합한 결과는 아니다.

### 8.4.3 인터페이스 기반 계산

analyze_signal()은 선택된 모델에 계산을 위임한다. analyze_many()는 신호 목록에 동일 모델을 적용한다. s=[1,3,9]일 때 선형 모델의 결과는 [0,1,4], 제곱 모델의 결과는 [0,1,2]이다.

비정상 입력이 목록 중간에 등장하면 현재 구현은 예외를 발생시키고 결과 목록을 반환하지 않는다. 행 단위 오류 기록은 향후 확장 가능하지만 현 단계에서는 도입하지 않는다. 16개 자동화 테스트로 대표 계산, 오류 경계, 불변성, 구조적 교체 가능성을 확인하였다.

## 8.5 인터페이스 설계의 기준

구현을 바꿀 이유가 실제로 존재하는지 확인한 뒤 가장 작은 의미 있는 인터페이스를 선택한다. 인터페이스 구조는 최소화하되 단위와 유효 범위에 대한 과학적 계약을 줄여서는 안 된다.

### 8.5.1 최소 인터페이스

현재 분석 함수에 필요한 동작은 predict_concentration() 하나이다. fit, plot, save, uncertainty를 모두 요구하면 일부 모델이 의미 없는 메서드를 구현하도록 강제할 수 있다. 이는 인터페이스 분리 원칙과 연결된다.

계수 추정은 농도 예측과 별도 책임이다. 특히 현재 frozen 모델에 상태를 수정하는 fit 메서드를 추가하는 것은 설계와 충돌할 수 있다. 별도 함수가 새로운 모델을 반환하는 방식이 대안이다.

### 8.5.2 과도한 추상화

하나의 선형 보정식만 필요하면 단일 함수로 충분할 수 있다. 공통 계약이나 변경 이유를 제공하지 않는 여러 추상 계층은 유지보수 비용을 높인다. Factory나 Adapter 같은 패턴도 실제 사용 요구가 없다면 도입하지 않는다.

모든 과학 모델을 predict(x) 한 가지로 통일하면 농도, 확률, 상태 배열의 의미가 숨겨질 수 있다. 호출명과 계약은 해당 과학적 계산의 의미를 전달해야 한다.

### 8.5.3 ABC와 Protocol의 선택

ABC는 명시적인 클래스 계층과 공통 구현이 필요할 때 유용하다. Protocol은 독립적인 모델 클래스나 외부 라이브러리의 구현을 같은 호출 계약으로 연결할 때 유용하다. Duck Typing은 간단한 호출을 위해 충분할 수 있다.

C3에서는 공통 구현 상속이 필요하지 않으며 두 계산 모델을 교체하는 것이 핵심이므로 Protocol을 선택한다. ABC나 과도한 클래스 계층을 추가하지 않는다.

## 8.6 Chapter Summary — 추상화와 인터페이스의 설계 원칙

Chapter 6은 개별 객체의 상태와 책임(P1), Chapter 7은 객체 사이의 관계(B1), Chapter 8은 구현과 계약의 분리(C3)를 다루었다. 세 단계는 서로 연결되지만 모든 문제에 세 단계의 복잡도를 모두 적용할 필요는 없다.

ABC는 명시적 클래스 관계, Protocol은 구조적 계약, Duck Typing은 동작 중심 사용을 돕는다. 다형성이 보장하는 것은 동일한 호출 경로이며 동일한 수치 결과가 아니다.

과학 소프트웨어에서는 구조적 검증, 동작 계약 검증, 수학적 계산 검증, 수치적 안정성 검사, 실제 데이터에 대한 과학적 타당성 평가를 구분해야 한다. 좋은 추상화는 실제로 교체해야 하는 구현과 안정적으로 유지해야 하는 계약의 경계를 명확하게 한다.

## 정규 실행 코드 발췌

```python
"""C3: interchangeable calibration models (educational, dimensionless)."""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Protocol


def finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f'{name} must be a real number')
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f'{name} must be finite') from exc
    if not isfinite(result):
        raise ValueError(f'{name} must be finite')
    return result


class CalibrationModel(Protocol):
    def predict_concentration(self, signal: float) -> float: ...


@dataclass(frozen=True)
class LinearCalibration:
    slope: float
    intercept: float

    def __post_init__(self) -> None:
        slope = finite_real(self.slope, 'slope')
        intercept = finite_real(self.intercept, 'intercept')
        if slope <= 0:
            raise ValueError('slope must be positive')
        object.__setattr__(self, 'slope', slope)
        object.__setattr__(self, 'intercept', intercept)

    def predict_concentration(self, signal: float) -> float:
        signal = finite_real(signal, 'signal')
        if signal < self.intercept:
            raise ValueError('signal is below the zero-concentration response')
        result = (signal - self.intercept) / self.slope
        return finite_real(result, 'concentration')


@dataclass(frozen=True)
class QuadraticCalibration:
    coefficient: float
    intercept: float

    def __post_init__(self) -> None:
        coefficient = finite_real(self.coefficient, 'coefficient')
        intercept = finite_real(self.intercept, 'intercept')
        if coefficient <= 0:
            raise ValueError('coefficient must be positive')
        object.__setattr__(self, 'coefficient', coefficient)
        object.__setattr__(self, 'intercept', intercept)

    def predict_concentration(self, signal: float) -> float:
        signal = finite_real(signal, 'signal')
        if signal < self.intercept:
            raise ValueError('signal is below the zero-concentration response')
        adjusted = (signal - self.intercept) / self.coefficient
        return finite_real(sqrt(adjusted), 'concentration')


def analyze_signal(signal: float, model: CalibrationModel) -> float:
    return model.predict_concentration(signal)


def analyze_many(signals: list[float], model: CalibrationModel) -> list[float]:
    return [analyze_signal(signal, model) for signal in signals]


if __name__ == '__main__':
    for model in (LinearCalibration(2, 1), QuadraticCalibration(2, 1)):
        print(type(model).__name__, analyze_many([1.0, 3.0, 9.0], model))

```

## 검증 상태

- C3 단일 실행 코드: 16개 unittest 통과
- 목표 Python 3.14.x 별도 검증: 미실시
- 화면 상세 원고와의 축자 대조: 미실시
- Word 문서: 재구성 편집 검토본

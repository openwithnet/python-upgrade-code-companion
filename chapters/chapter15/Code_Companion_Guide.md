# Chapter 15 Code Companion — v53 후보

- **15.1–15.4**: 개념·부분 코드 위주. 이 패키지는 해당 절 전체 코드를 재현하지 않는다.
- **15.5.1**: `numpy_concentration`, `analytical_jacobian`; 시간 `[0,1,2,3,5]`, 매개변수 `[1.0,0.2]`.
- **15.5.2**: `torch_jacobian`, CPU float64, `torch.func.jacrev`.
- **15.5.3**: `jax_jacobian`, x64 설정, `jax.jacrev`, 선택적 `jax.jit`.
- **15.6–15.7**: 비교·요약; 별도 독립 코드 전수 추출 미완료.

모델은 `C(t)=C0 exp(-kt)`, Jacobian 열 순서는 `[∂C/∂C0, ∂C/∂k]`, 크기는 (5,2). 결과는 농도/매개변수 단위에 의존한다. 이 예제는 원고에 등장하는 식·매개변수를 바탕으로 **재구성**했다. 원고의 모든 코드 블록이 검증되었다는 뜻이 아니다.

```bash
python -m pytest tests -q
```

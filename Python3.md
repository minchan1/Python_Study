# 입력과 출력



## 함수

- 입력값으로 어떤 일을 수행한 후 결과물을 출력하는 것

- 반복되는 일을 처리하기 좋고 프로그램의 흐름을 파악할 수 있음

- 기본 형태

- ```python
  def func() :
      if문, while문, for문 등등...
      ...
      
  ```



### 함수의 형태

- 일반적인 형태

- ```python
  # 입력값과 결과값이 존재
  
  def func(a, b):
      asdf
      ...
      return c
  
  # a,b를 입력, 결과값 c가 출력
  ```

- 입력값이 없는 함수

- ```python
  def func():
      return 'c'
  a = func()
  print(a)
  c
  
  # 입력값은 없지만 a에 결과값 c 를 돌려줌
  ```

- 결과값이 없는 함수

- ```python
  def func():
      print('ccc')
  print(func())
  None
  
  # 함수를 실행하면 print가 수행되어 ccc가 출력되지만,
  # return값이 없기 때문에 print(func())는 None이 된다
  ```



### 매개변수 지정

- ```python
  >>> def add(a, b):
  ...     return a+b
  ... 
  
  >>> result = add(a=3, b=7)  # a에 3, b에 7을 전달
  >>> print(result)
  10
  
  >>> result = add(b=5, a=3)  # b에 5, a에 3을 전달
  >>> print(result)
  8
  
  # 순서에 상관없이 사용가능!
  ```



### 입력값의 수를 모를때

- ```python
  def 함수이름(*매개변수): 
      <수행할 문장>
      ...
  ```

- ```python
  >>> def add_many(*args): 
  ...     result = 0 
  ...     for i in args: 
  ...         result = result + i 
  ...     return result 
  
  # 입력값이 몇개가 되더라도 문제 x
  # 앞에 *를 붙이면 입력값을 전부 모아서 튜플로 바꿔준다
  ```



### 키워드 파라미터 

- ```python
  >>> def print_kwargs(**kwargs):
  ...     print(kwargs)
  ...
  
  # 매개변수 앞에 **를 붙임
  ```

- ```python
  >>> print_kwargs(a=1)
  {'a': 1}
  >>> print_kwargs(name='foo', age=3)
  {'age': 3, 'name': 'foo'}
  
  # 딕셔너리로 만들어져서 출력된다
  ```



### lambda 함수

- 함수를 생성할때 사용함, def와 동일한 역할

- 한줄로 간결하게 만들때 사용

- ```python
  >>> add = lambda a, b: a+b
  >>> result = add(3, 4)
  >>> print(result)
  7
  ```





## 입력과 출력



### 사용자 입력

- input의 사용

- ```python
  >>> a = input()
  Life is too short, you need python
  >>> a
  'Life is too short, you need python'
  >>>
  
  # 문자열로 취급되어 입력된다는 것 주의
  ```

- 




































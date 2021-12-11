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

- 프롬프트 띄워서 입력받기

- ```python
  >>> number = input("숫자를 입력하세요: ")
  숫자를 입력하세요: 3
  >>> print(number)
  3
  
  # input("질문 내용")의 형태로 띄워주기
  ```

- 



### print에 대해

- 큰따옴표로 둘러싸인 문자열은 + 연산과 동일

- ```python
  >>> print("life" "is" "too short") 
  lifeistoo short
  >>> print("life"+"is"+"too short") 
  lifeistoo short
  ```

- 콤마를 사용하면 문자열 띄어쓰기

- ```python
  >>> print("life", "is", "too short")
  life is too short
  ```

- 한 줄에 결과값 출력하기

- ```python
  >>> for i in range(10):
  ...     print(i, end=' ')
  0 1 2 3 4 5 6 7 8 9
  
  # 매개변수 end 사용
  ```





## 파일 읽고 쓰기



### 파일생성

- 파이썬 내장함수 open을 사용

- 파일 이름과 파일 열기 모드를 입력값으로 받고 결과값으로 파일 객체를 돌려줌

- r : 읽기모드, w : 쓰기모드, a : 추가모드

- ```python
  f = open("C:/Users/alfls/Python_Study/newfile.txt", 'w')
  f.close()  # 파일객체 닫는역할, 생략가능
  ```



### 쓰기모드

- ```python
  f = open("C:/Users/alfls/Python_Study/newfile.txt", 'w')
  for i in range(1, 11):
      data = "%d번째 줄입니다.\n" % i
      f.write(data)
  f.close()
  ```



### 내용 추가하기

- 쓰기모드로 열면 내용이 모두 사라짐

- 원래의 내용을 유지하면서 새로운 값만 추가할때 

- ```python
  f = open("C:/Users/alfls/Python_Study/newfile.txt",'a')
  for i in range(11, 20):
      data = "%d번째 줄입니다.\n" % i
      f.write(data)
  f.close()
  ```

- with문을 통해 파일을 열고 닫는것을 자동으로 처리가능

- ```python
  with open("newfile.txt", "w") as f:
      f.write("Life is too short, you need python")
  ```

- 








































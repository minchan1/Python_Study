# 제어문



## if문

- 조건을 판단하여 해당 조건에 맞는 상황을 수행

- ```python
  # 기본 구조는 다음과 같다
  if 조건문 :
      수행할 문장1
      수행할 문장2
      ...
  else :
      수행할 문장A
      ...
      
  # 조건문이 참이면 if블록들을 수행
  # 조건문이 거짓이면 else블록들을 수행
  ```

- 들여쓰기, 콜론(:) 사용에 주의할 것 !!



### 비교연산자

- (`<`, `>`, `==`, `!=`, `>=`, `<=`) 

- ```python
  n = int(input())
  if n >= 70 :
      print('조건이 맞으면 수행')
  else :
      print('조건문이 거짓이면 수행')
  ```



### and, or, not

- x and y : x,y 모두 참이어야 참

- x or y : x,y 둘중에 하나만 참이면 참

- not x : x가 거짓이면 참

- ```python
  x,y = input().split()
  if x = True and y = True :
      print('둘다 참이면 수행')
  ```



### in, not in

- x in 리스트 / 튜플 / 문자열

- 리스트 / 튜플 / 문자열 안에 x가 포함되면 참

- ```python
  >>> 1 in [1, 2, 3]
  True
  >>> 1 not in [1, 2, 3]
  False
  ```

- 조건문에서 아무 일도 하지 않게 설정하는 경우

- ```python
  >>> n = [1, 2, 3]
  >>> if 1 in n:
  ...     pass 
  ... else:
  ...     print('조건문이 참이 아니면 실행')
  # 1이 n에 포함되므로 if블록이 실행,
  # pass가 수행되고 아무 결과도 표시되지 않음
  ```



### elif ?

- if와 else만으로 표현하기 어렵거나 코드가 복잡해지면

- 다중 조건을 판단하기 위한 기능

- 이전 조건문이 거짓이면 elif문이 수행된다

- ```python
  If <조건문>:
      <수행할 문장1> 
      <수행할 문장2>
  elif <조건문>:
      <수행할 문장1>
      <수행할 문장2>
  else:
     <수행할 문장1>
  	...
  ```





## while문



### 반복문

- 반복해서 문장을 수행해야 할때! (반복문)

- ```python
  # 기본 구조
  while <조건문>:
      <수행할 문장1>
      <수행할 문장2>
      <수행할 문장3>
      ...
  # 조건문이 참이면 계속 반복하여 수행
  ```



### 강제로 종료하기

- 강제로 종료하려면?

- ```python
  while <조건문>:
      <수행할 문장1>
      <수행할 문장2>
      if <조건문2>:
          break
          # break문을 사용하여 탈출!
  ```



### 처음으로 돌아가기

- 맨 처음으로 돌아가려면?

- ```python
  >>> a = 0
  >>> while a < 10:
  ...     a = a + 1
  ...     if a % 2 == 0: continue
  ...     print(a)
  # a가 짝수이면 continue문에 의해 처음으로 돌아감!
  # 따라서 a가 짝수일때는 print(a)가 실행되지 않는다.
  ```



## for문



### 구조와 예시

- fora문의 기본 구조

- ```python
  for 변수 in 리스트(또는 튜플, 문자열):
      수행할 문장
      ...
  # 리스트,튜플,문자열 등의 첫번째 요소부터
  # 마지막 요소까지 변수에 대입되어 수행된다
  ```

- for문의 활용예시

- ```python
  n = [60, 70, 45, 88, 54]
  for i in n :
      if i >= 70 :
          print('pass')
      else :
          print('fail')
  ```



### continue 활용

- continue의 사용?

- ```python
  n = [60, 70, 45, 88, 54]
  for i in n :
      if i >= 70 :
          continue
      print('pass')
  ```



### range 함수

- 숫자 리스트를 자동으로 만들어 주는 range 함수

- ```python
  n = 0
  for i in range(10) :
      n = n+i
  print(n)
  45
  # 10미만의 숫자까지 대입
  ```

- 리스트 내포 사용

- ```python
  >>> a = [1,2,3,4]
  >>> result = []
  >>> for num in a:
  ...     result.append(num*3)
  ...
  >>> print(result)
  [3, 6, 9, 12]
  # a 리스트에 3을 곱한 result 리스트 생성
  ```

- 








































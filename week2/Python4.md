# 파이썬 응용



## 클래스

- 사용자가 정의하는 새로운 타입, 함수와도 같음

- 파이썬에서는 int, str, list, tuple ... 등등 미리 정의해둔 클래스들이 있다

- ```python
  # 기본 형태
  class 클래스명 :
      클래스 블록
      ...
  
  # 클래스를 정의할 때 이름은 대문자로 시작하길 권장
  ```

- 무언가를 계속해서 만들어 낼 수 있는 설계도면과도 같다.



### 객체

- object, instance 라고도 한다
- 비유하자면 클래스로 만든 피조물과도 같다
- 객체마다 고유한 성격을 가지며, 객체들끼리는 서로 영향을 주지않는다
- 임의로 삭제하기 전까지 메모리에 남아있음



### 생성자

- 객체가 생성될 때 자동으로 호출되는 메소드
- 모든 객체가 동일한 속성을 갖게 해줌
- \__init__(self, 변수): 의 형태



### 상속

- 기존 클래스를 변경하지 않고 기능을 추가하거나 변경
- 상속한 클래스에 있는 메서드를 다시 만드는것을 오버라이딩 이라고 함
- 부모클래스 대신 오버라이딩 한 메서드가 호출됨
- 반드시 상속을 거쳐야함!!



### 클래스변수

- 객체변수는 다른 객체들에 영향받지 않고 독립적임

- 클래스변수는 클래스 안에 변수를 선언하여 생성

- ```python
  >>> class Family:
  ...     lastname = "김"
  ...
  
  >>> print(Family.lastname)
  김
  # 클래스이름.클래스변수 로 사용한다
  ```

- 클래스로 만든 모든 객체에 공유된다







## 모듈

- 함수나 변수 또는 클래스를 모아놓은 파일

- 확장자가 py인 파이썬 소스파일

- import를 통해 불러오자

- ```python
  # import 모듈이름 import 모듈함수 의 형태
  from mod1 import add
  add(3,4)
  7
  
  # 모듈내의 함수 전부 가져오기?
  from mod1 import *
  ```

- _\_name__ == "_\_main__" ?

- ```python
  # 파이썬 소스 파일을 직접 실행할 때
  __name__ 변수의 값이 __main__ 이 됨
  
  # 모듈로 import되어 실행될 때
  __name__ 변수의 값이 모듈이름이 됨
  
  if __name__ == "__main__" :
      print('asd')
      # if __name__ == "__main__" 을 사용하여
      # 파일을 실행할때는 if문이 참이되어 print가 실행
      # 모듈을 불러서 사용할 때는 print가 실행되지 않음
  ```



- 모듈 불러오기

- ```python
  import sys
  sys.path
  # 를 사용하여 경로들에서 파일을 찾음
  # 새로운 경로를 path에 추가함
  sys.path.append('경로')
  ```





## 패키지

- 여러개의 모듈을 하나로 묶은 것

- 폴더내에 \__init__.py가 있으면 패키지로 인식

- 패키지 생성

- ```python
  C:/doit/game/__init__.py
  C:/doit/game/sound/__init__.py
  C:/doit/game/sound/echo.py
  C:/doit/game/graphic/__init__.py
  C:/doit/game/graphic/render.py
      
  # __init__.py는 생성만 하고 내용은 없어도 됨
  
  # echo.py
  def echo_test():
      print("echo")
      
  
  ```

- 함수 실행

- ```python
  # echo 모듈을 import하여 실행
  >>> import game.sound.echo
  >>> game.sound.echo.echo_test()
  echo
  
  # echo 모듈이있는 디렉터리까지 from import 하여 실행
  >>> from game.sound import echo
  >>> echo.echo_test()
  echo
  
  # echo 모듈의 echo_test함수를 import하여 실행
  >>> from game.sound.echo import echo_test
  >>> echo_test()
  echo
  ```





## 예외처리

- try, except 문

- ```python
  try:
      ...
  except [발생 오류[as 오류 메시지 변수]]:
      ...
      
  # try 블록 수행 중 오류가 발생하면 except 블록 수행
  # 발생하지 않으면, except 블록도 수행 X
  
  # 사용한 리소스를 close 해야 할때
  f = open('foo.txt', 'w')
  try:
      ...
  finally:     # finally절은 예외와 상관없이 항상 수행
      f.close()  
  ```

- 여러개의 오류 처리

- ```python
  # 여러개의 오류 처리할때
  try:
      ...
  except 발생 오류1:
     ... 
  except 발생 오류2:
     ...
  
  # 오류 메시지가 여러개
  try:
      a = [1,2]
      print(a[3])
      4/0
  except (ZeroDivisionError, IndexError) as e:
      print(e)   # 괄호로 함께 묶어 처리
  ```

- else절 사용하기

- ```python
  try:
      ...
  except [발생 오류[as 오류 메시지 변수]]:
      ...
  else:  # 오류가 없을 경우에만 수행된다.
      ...
      
  ```



## 주요 내장함수

1. abs : abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.
2. all : all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
3. any : any(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
4. chr : chr(i)는 유니코드(Unicode) 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
5. dir : dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여 주는 예이다. 우리가 02장에서 살펴본 자료형 관련 함수를 만나 볼 수 있다.
6. divmod : divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.


















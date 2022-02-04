---
title: Practice Coding - Lv1 UP&DOWN game
author:
  name: jinozpersona
  link: 
date: 2022-02-04 9:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

업앤다운 UP&Down 숫자맞추기 게임
--------------------------

***

컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
사용자는 이 숫자를 맞추어야 합니다.
입력한 숫자보다 정답이 크면 → "UP" 출력,
입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.

출처 : [codingdojang](<https://codingdojang.com/scode/711?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. 랜텀 숫자 추출
>    > 2. try except 정수 확인
>    > 3. 양의 정수 판별
>    > 4. while 반복문 안에서 if 조건에 맞는 내용 출력


## My Answer
<details><summary>Click Here</summary>

<pre>
<code>
import random

target_num = random.randrange(1,101)
# test try
# target_num = 10

try_cnt = 1
while try_cnt > 0:
  input_num = input("Please input number: ")

  try:
    int(input_num)
    it_is = True
    input_num = int(input_num)

  except ValueError:
    it_is = False

  # print(it_is)

  if it_is == True and input_num >= 1:
    if input_num == target_num:
      print("정답 : Target Num = {}, Your Answer = {}\n시도 횟수 : {}\n".format(target_num,input_num, try_cnt))
      break
    elif input_num < target_num:
      print("UP : {} --- Target Num, try_cnt = {}\n".format(input_num, try_cnt))
      try_cnt = try_cnt + 1
    elif input_num > target_num:
      print("DOWN : Target Num --- {}, try_cnt = {}\n".format(input_num, try_cnt))
      try_cnt = try_cnt + 1
  else:
    print("Your input_num is wrong, please input positive integer number.")
</code>
</pre>

</details>
<!-- 



# 2. github.io 블로그 생성
## github.io 일명 github page 생성하기



# 3. github.io jekyll bundler 설치 및 git push 적용
## github jekyll theme 사용을 위한 ruby 설치와 localhost server 실행



# 4. github.io chirpy-theme 적용 및 git push
## jekyll theme 적용 과정


 -->
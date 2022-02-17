---
title: Practice Coding - Lv1 password encryption
author:
  name: jinozpersona
  link: 
date: 2022-02-07 9:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1, password, encryption]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

수 암호화 프로그램
-------------

***

0~25만의 수 1개를 입력으로 받으면 그 수를 암호화하여 출력하는 프로그램을 작성하세요. 방법은 다음과 같습니다. 
1. 입력받은 수의 제곱근에 1000을 곱한다. 
(예시: 2 => 1.414213... * 1000 => 1414.213...) 
2. 1의 결과에서 소수점 이하를 버림한다. (예시: 1414.213... => 1414) 
3. 2의 결과에서 입력받은 수를 뺀다.(예시: 1414 => 1414 - 2 => 1412) 이렇게 하면 2를 입력받았을 때 1412를 출력합니다. 

다음 결과로 테스트하세요.

password(2)

1412

출처 : [codingdojang](<https://codingdojang.com/scode/704?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. input number
>    > 2. try except 정수 확인, 양의 정수 판별
>    > 3. encryption number function
>    > 4. output


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
input_num = input("password: ")

try:
  int(input_num)
  it_is = True
  input_num = int(input_num)

except ValueError:
  it_is = False


if it_is == True and input_num >= 1 and input_num <= 2.5*10**5:
  do_secret = int((input_num**(1/2))*10**3) - input_num
  print("encryption number : {}\n".format(do_secret))

else:
  print("Your input_num is wrong, please input positive integer number.")

</code>
</pre>

</details>

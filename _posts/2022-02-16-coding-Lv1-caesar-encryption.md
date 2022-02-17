---
title: Practice Coding - Lv1 caesar encryption
author:
  name: jinozpersona
  link: 
date: 2022-02-16 21:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1, caesar, encryption]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

시저 암호 풀기
-----------

***

시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데, 
예를 들어 알파벳 A를 입력했을 때, 
그 알파벳의 n개 뒤에 오는(여기서는 예를 들 때 3으로 지정하였다)알파벳이 출력되는 것이다. 
예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.

어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.

출처 : [codingdojang](<https://codingdojang.com/scode/555?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. alphabet list
>    > 2. try except string
>    > 3. encrytion function for n
>    > 4. output


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
from string import ascii_lowercase
 
 
alph_list = list(ascii_lowercase)

while True:
  try:
    input_strs = input("input alphabet only lowercase:")
    if input_strs.isalpha() != True:
      print("Please input alphabet")
      continue
    elif input_strs.islower() != True:
      print("Please input lowercase")
      continue
    else:
      pass

  except Exception as e:
    print("Exception msg: {}".format(e))

  else:
    while True:
      try:
        input_n = int(input("input shift number(plus integer):"))
        if input_n >= 0:
          break
        
        else:
          print("Please input plus integer number")
          continue
          # input_n = int(input("input shift number(plus integer):"))

      except ValueError as v:
        print(v)
    
    print("Confirm your input {}, {}".format(input_strs, input_n))
    break
    
input_conv_list = []

for input_str in input_strs:
  shift_n = alph_list.index(input_str) + int(input_n)
  if shift_n > len(alph_list):
    shift_n = shift_n - len(alph_list)
  input_conv_list.append(alph_list[shift_n])

print("Done caesar_enctyption : {}".format(''.join(input_conv_list)))



</code>
</pre>

</details>

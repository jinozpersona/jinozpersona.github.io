---
title: Practice Coding - Lv1 seperate character-set to string / int
author:
  name: jinozpersona
  link: 
date: 2022-02-10 13:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1]
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

문자와 숫자가섞인 문자열을 입력받을때 구별하여출력해라

input:

"c910m6ia 1ho"

output:

str : cma ho

int : 91061

출처 : [codingdojang](<https://codingdojang.com/scode/646?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. character string 분리하기
>    > 2. list의 각 원소를 string type으로 전환
>    > 3. int는 string이 아닌 int type으로 전환


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
input_charset = "c910m6ia 1ho"
print("input : {}\n type : {}\n\n".format(input_charset, type(input_charset)))

strset = []
intset = []
intset_int = []

for tstr in input_charset:
  if tstr.isdigit():
    intset.append(tstr)
    intset_int.append(int(tstr))
  else:
    strset.append(tstr)

print("str : {}".format(', '.join(strset).replace(', ','')))
print("int : {}".format(', '.join(intset).replace(', ','')))
print("----****----")
print("strset string list : {}".format(strset))
print("intset string list : {}".format(intset))
print("intset int list : {}".format(intset_int))
print("----****----")
conv_intset = int(', '.join(intset).replace(', ',''))
print("convert to int type from intset: {}, converted type: {}".format(conv_intset, type(conv_intset)))

</code>
</pre>

</details>

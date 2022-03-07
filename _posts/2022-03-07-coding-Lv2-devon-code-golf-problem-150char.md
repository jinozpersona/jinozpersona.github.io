---
title: Practice Coding - Lv2 devon code golf problem
author:
  name: jinozpersona
  link: 
date: 2022-03-07 22:00:00 +0900
categories: [Practice, Lv2]
tags: [coding, practice, lv2, devon, code, golf, problem, 150char]
---

디브온 코드골프 문제
---------------

***

디브온에서 미니대안언어축제가 진행되던 M2 밖에 텍스트큐브 부스에서 
 재미있는 코드골프 문제 풀기가 있었습니다. 
 150자 이하로 푸신 분들에게는 즉석에서 제공되는 원두커피와 텀블러가 상으로 주어졌다고 합니다.

문제는 아래와 같습니다. 이 결과가 나와야 하는데 언어 제약은 없답니다.

     *
     *
    * *
   *   *
  *     *
**       **
  *     *
   *   *
    * *
     *
     *

출처 : [codingdojang](<https://codingdojang.com/scode/433?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. replace binary 
>    > 2. normal algorithm
>    > 3. List Comprehesion


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
## data
ns=[32,32,80,136,260,1539,260,136,80,32,32]

## List Comprehension #1
# nb=["{0:b}".format(i).zfill(11) for i in ns]
# [print(n.replace('1', '*').replace('0',' ')) for n in nb]

## List Comprehension #2
[print("{0:b}".format(n).zfill(11).replace('1', '*').replace('0',' ')) for n in ns]


## algorithm
# for i in ns:
#   nb = "{0:b}".format(i).zfill(11)
#   print("{}".format(nb.replace('1', '*').replace('0',' ')))

</code>
</pre>

</details>

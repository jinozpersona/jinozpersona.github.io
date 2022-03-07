---
title: Practice Coding - Lv2 number counting
author:
  name: jinozpersona
  link: 
date: 2022-02-26 23:00:00 +0900
categories: [Practice, Lv2]
tags: [coding, practice, lv2, google, number, counting]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

구글 입사문제 중에서
---------------

***

1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

출처 : [codingdojang](<https://codingdojang.com/scode/393?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. counting function
>    > 2. number element separate & counting


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
def counting_fun(input_num):
  input_num = str(input_num)
  cnt = 0
  for element in input_num:
    if element == "8":
      cnt = cnt + 1
    else:
      pass
  return cnt

num_range = range(1,10000)
cnt_list = []
for i in num_range:
  cnt_output = counting_fun(i)
  cnt_list.append(cnt_output)

print(" total_conting:{} \n counting_sum of number 8 :{}".format(len(cnt_list), sum(cnt_list)))

</code>
</pre>

</details>

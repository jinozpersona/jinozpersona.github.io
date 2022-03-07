---
title: Practice Coding - Lv2 Kaprekar Self-Number
author:
  name: jinozpersona
  link: 
date: 2022-02-26 22:00:00 +0900
categories: [Practice, Lv2]
tags: [coding, practice, lv2, Nexon, Kaprekar, self number]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

넥슨 입사문제 중에서
---------------

***

d(91) = 9 + 1 + 91 = 101

이 때, n을 d(n)의 제네레이터(generator)라고 한다. 
위의 예에서 91은 101의 제네레이터이다.

어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 
101의 제네레이터는 91 뿐 아니라 100도 있다. 
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 
이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

출처 : [codingdojang](<https://codingdojang.com/scode/365?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. Kaprekar Self-Number Algorithm 이해
>    > 2. gen_num 입력으로 얻어지는 dn function
>    > 3. dn이 5000 보다 작거나 같은 범위의 dn_list 
>    > 4. dn_list의 중복 제거 dn_list_set
>    > 5. dn_list_set을 제외한 self-number 출력 및 총합


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
def kaprekar_fun(gen_num):
  gen_num = str(gen_num)
  gen_num_list = []
  for element in gen_num:
    gen_num_list.append(int(element))
  gen_num_list.append(int(gen_num))
  dn = sum(gen_num_list)
  print("gen_num: {},{} | d(n):{}".format(gen_num,gen_num_list,dn))
  return dn

num_range = range(1,5000)
kaprekar_output = []# for i in range(1,110):  
for i in num_range: 
  dn = kaprekar_fun(i)
  if dn >= 5000:
    # i = 4975 then dn = 5000
    print(i,dn)
    break
  else:
    kaprekar_output.append(dn)

kaprekar_output_sorted_set = list(set(sorted(kaprekar_output)))
print("d(n)_set:\n{}".format(kaprekar_output_sorted_set))


kaprekar_self_num = []
for n in num_range:
  if n not in kaprekar_output_sorted_set:
    kaprekar_self_num.append(n)
  else:
    pass

print("kaprekar_self_numbers:\n{}".format(kaprekar_self_num))
print("Sum of kaprekar_self_numbers:\n{}".format(sum(kaprekar_self_num)))


</code>
</pre>

</details>

---
title: Practice Coding - Lv2 cycle length 3n+1 problem
author:
  name: jinozpersona
  link: 
date: 2022-02-27 13:00:00 +0900
categories: [Practice, Lv2]
tags: [coding, practice, lv2, Paul Erd'os, 3n+1, cycle length]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

3n+1 Problem
------------

***

어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 
홀수면 3을 곱한 다음 1을 더한다. 
이렇게 해서 새로 만들어진 숫자를 n으로 놓고, 
n=1 이 될때까지 같은 작업을 계속 반복한다. 
예를 들어, n=22이면 다음과 같은 수열이 만들어진다.

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

n이라는 값이 입력되었을때 1이 나올때까지 
만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다. 
위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다. 
i와 j라는 두개의 수가 주어졌을때, 
i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.

입력 예

1    10
100  200
201  210
900  1000

출력 예

1    10    20
100  200   125
201  210   89
900  1000  174
※ 참고

어떤 자연수 n에 대해서도, 이 조작을 유한 번 시행하면 1이 될 것이라고 
예상하는데, 700,000,000,000보다 작은 모든 짝수에 대해 
성립한다는 것이 밝혀져 있긴 하지만, 아직 아무도 증명하지 못했습니다. 
유명한 헝가리 수학자 폴 에르되시(Paul Erd' os)는, 
"우리의 수학은 아직 이 문제를 풀 준비가 되어 있지 않다." 라고 했습니다.

출처 : [codingdojang](<https://codingdojang.com/scode/409?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. Paul Erd'os Algorithm 이해
>    > 2. for n in range(i+1,j)
>    > 3. if even: else: function
>    > 4. paul_erdos_fun return
>    > 5. max(cycle_list)


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
def paul_erdos_fun(i,j):
  i = int(i)
  j = int(j)
  cycle_list = []
  for n in range(i+1,j):
    input_num = int(n)
    paul_series = [input_num]
    while input_num != 1:
      if input_num%2 == 0:
        input_num = int(input_num/2)
        paul_series.append(input_num)
        # print("even fun:{}".format(input_num))
      else:
        input_num = int(input_num*3 + 1)
        paul_series.append(input_num)
        # print("odd fun:{}".format(input_num))
    cycle_list.append(len(paul_series))
    print("{} | cycle_length:{}".format(n,len(paul_series)))
    # print("paul_series:{}".format(paul_series))
  return cycle_list


cycle_list = paul_erdos_fun(900,1000)
print("cycle_list:{}".format(cycle_list))
print("max_cycle:{}".format(max(cycle_list)))

</code>
</pre>

</details>

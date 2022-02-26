---
title: Coding Study - fibonacci_series
author:
  name: jinozpersona
  link: 
date: 2022-02-17 12:00:00 +0900
categories: [Coding, Study]
tags: [coding, study, fibonacci, series]
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

피보나치 수열
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

***


## platform : python
> ### 접근방법
>    > 1. fibonacci series algorithm
>    > 2. function : f(t) = f(t-1) + f(t-2)
>    > 3. try except : plus integer


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>

def fib_series():
  fib_lists = [0, 1]

  while True:
    try:
      n = int(input("input target number:"))
      if n < 0:
        print("please input plus integer")
        continue

    except ValueError as v:
      print(v)

    else:
      if n == 0:
        print("wrong number")
      else:
        for n in range(n):
          fib_lists.append(fib_lists[n]+fib_lists[n+1])
        print("fib_series:{}".format(fib_lists))
        break

fib_series()



</code>
</pre>

</details>

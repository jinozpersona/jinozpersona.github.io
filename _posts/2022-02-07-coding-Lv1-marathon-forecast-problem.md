---
title: Practice Coding - Lv1 marathon-forecast-problem
author:
  name: jinozpersona
  link: 
date: 2022-02-07 10:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

기계의 마라톤 기록
-------------

***

항상 일정한 속도로 달리는 기계가 있다고 합시다.
이 기계의 100m 달리기 기록을 입력받으면 마라톤에서의 기록을 구하시면 됩니다. 
마라톤 경기에서 달리는 거리는 42.195km입니다. 
100m 달리기와 마라톤의 코스는 모두 직선이라고 합니다
(회전 시 걸리는 시간을 고려하지 않습니다). 
기계의 파손 및 배터리 방전 시간도 고려하지 않습니다.

출처 : [codingdojang](<https://codingdojang.com/scode/702?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. input number
>    > 2. try except 실수 확인, 양의 정수 판별
>    > 3. forecast time function
>    > 4. output


## My Answer!
<details><summary>Click Here</summary>


<pre>
<code>
input_num = input("robot lap time(sec) for 100m: ")

try:
  float(input_num)
  it_is = True
  input_num = float(input_num)

except ValueError:
  it_is = False


if it_is == True and input_num >= 0:
  do_forecast = round(42.195/(0.1/(input_num/60)),1)
  print("forecast time for marathon 42.195km: {} min\n".format(do_forecast,1))

else:
  print("Your input_num is wrong, please input positive float number.")


</code>
</pre>

</details>

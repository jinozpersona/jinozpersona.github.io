---
title: Practice Coding - Lv1 baskin robbins 31 game
author:
  name: jinozpersona
  link: 
date: 2022-02-07 11:00:00 +0900
categories: [Practice, Lv1]
tags: [coding, practice, lv1, baskin robbins 31]
# math: true
# mermaid: true
# image:
  # src: #/commons/devices-mockup.png
  # width: #800
  # height: #500
---

배스킨라빈스31게임
-------------

***

게임의 참여자들은 차례를 정해 1부터 31까지의 수를 순차적으로 부른다. 
한번에 1~3개까지 수를 연달아 부를 수 있으며, 마지막 31을 부른 사람이 진다.
- 컴퓨터가 무조건 먼저 시작하고,1P는 무조건 2번째로 말한다.컴퓨터가 무조건 이기게 만들어라.
- LEVEL1 예상
- 힌트1:4n-2라는 공식을 사용하면 됩니다.
- 힌트2:이 게임은 31을 부르면 지는 게임이니 30을 부르면 이깁니다.

출처 : [codingdojang](<https://codingdojang.com/scode/700?answer_mode=hide>){:target="_blank"}

***


## platform : python
> ### 접근방법
>    > 1. king_number 4n+2 이해
>    > 2. try except : force input number to player
>    > 3. Algorithm for king win!
>    > 4. Grame Process print...


## My Answer
<details><summary>Click Here</summary>


<pre>
<code>
game_cnt = 0
ttl_cnt = 0
player_cnt = 0


print("*********************")
print("****---31 Game---****")
print("*********************\n")

# king_number = [int(4*n+2) for n in range(8)]
king_run = 2

while ttl_cnt != 31:
  game_cnt = game_cnt + 1
  print("--*-- Game Count : {}번째 --*-- ".format(game_cnt))

  for king_input in range(king_run):
    print("king : {}".format(ttl_cnt+1))
    ttl_cnt = ttl_cnt + 1
    king_input = ttl_cnt

  player_run = 0
  while player_run <= 2:
    if player_run == 0:
      player_input = input("player(press Enter): {}".format(ttl_cnt + 1))
      player_input = int(ttl_cnt + 1)
      player_run = player_run + 1
      ttl_cnt = ttl_cnt + 1

    else:
      player_input = input("palyer(turn over press Enter): ")
      if player_input == '':
        player_input = ttl_cnt
        # print("player turn over")
        break

      else:
        try:
          int(player_input)
          it_is = True
          player_input = int(player_input)

        except ValueError:
          it_is = False
        
        if it_is == True and player_input == ttl_cnt + 1:
          player_run = player_run + 1
          ttl_cnt = ttl_cnt + 1

        else:
          print("Your input_num is wrong, please input positive integer number.")

    if int(player_input) == 31:
      print("\n")
      print("--**********************--")
      print("--****--King Win!!--****--")
      print("--**********************--")
      break

    elif int(king_input) == 31:
      print("\n")
      print("--*--Unbelievable!!--*--")
      print("--**--Player Win!!--**--")
      print("--********************--")
      break

    else:
      king_run = 4 - player_run

</code>
</pre>

</details>

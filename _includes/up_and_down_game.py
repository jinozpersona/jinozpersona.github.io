# -*- coding: utf-8 -*-
# src : coding dojang
# link : https://codingdojang.com/scode/711?answer_mode=hide
# title : up and down game
# platform : macOS, sublimetext, python

'''
컴퓨터가 1~100 숫자(정수 범위) 중 하나를 랜덤으로 정합니다. (이를 알려주지 않습니다.)
사용자는 이 숫자를 맞추어야 합니다.
입력한 숫자보다 정답이 크면 → "UP" 출력,
입력한 숫자보다 정답이 작으면 → "DOWN" 출력.
정답을 맞추면 → "정답"을 출력하고, 지금까지 숫자를 입력한 횟수를 알려줍니다.
'''

'''
접근 방법
랜텀 숫자 추출
try except 정수 확인
양의 정수 판별
while 반복문 안에서 if 조건에 맞는 내용 출력
'''

import random

target_num = random.randrange(1,101)
# test try
# target_num = 10

try_cnt = 1
while try_cnt > 0:
	input_num = input("Please input number: ")

	try:
		int(input_num)
		it_is = True
		input_num = int(input_num)

	except ValueError:
		it_is = False

	# print(it_is)

	if it_is == True and input_num >= 1:
		if input_num == target_num:
			print("정답 : Target Num = {}, Your Answer = {}\n시도 횟수 : {}\n".format(target_num,input_num, try_cnt))
			break
		elif input_num < target_num:
			print("UP : {} --- Target Num, try_cnt = {}\n".format(input_num, try_cnt))
			try_cnt = try_cnt + 1
		elif input_num > target_num:
			print("DOWN : Target Num --- {}, try_cnt = {}\n".format(input_num, try_cnt))
			try_cnt = try_cnt + 1
	else:
		print("Your input_num is wrong, please input positive integer number.")


	

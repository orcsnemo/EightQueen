#!/usr/bin/python
# -*- coding:utf-8 -*-
#by orcsnemo
def conflict(state,nextX):
	nextY= len(state)
	for i in range(nextY):
		#注意，要判断该皇后位是否与前面冲突0表示同一水平位置，nextY-i表示在对角线上：
		if abs(state[i]-nextX) in (0,nextY-i):
			return True
	return False

def queens(num=8, state=()):
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num-1:
				yield (pos,)
			else:
				for result in queens(num, state+(pos,)):
					yield (pos,)+result

#print list(queens(4,(1,3,0)))
#处理输出 
def prettyprint(solution):
	#函数内部的函数为助手函数
	def line(pos, length=len(solution)):
		return '. '*pos+'* '+'. '*(length-pos-1)
	for pos in solution:
		print line(pos)

print len(list(queens(8)))

prettyprint(list(queens(8))[1])

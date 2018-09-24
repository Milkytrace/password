#密碼重試程式

i = 0
password = 'a123456'


print('最多輸入三次密碼')
while True:
	p = input('請輸入密碼')
	i = i + 1
	if p == 'a123456':
		print('登入成功！')
		break
	elif i == 1 or i == 2:
		print('密碼錯誤！還有',3 - i,'次機會')
	if i == 3:
		print('錯誤太多次，賬號被鎖 登楞')
		break


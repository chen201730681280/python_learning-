#coding=gbk
#存储游戏的所有设置
class Settings():
	def __init__(self):
		#屏幕设置
		self.screen_width=1200
		self.screen_height=600
		self.bg_color=(230,230,230)
		#飞船的速度
		self.ship_speed_factor=1.5
		# 子弹设置
		self.bullet_speed_factor = 1 
		self.bullet_width = 3 
		self.bullet_height = 15 
		self.bullet_color = 60, 60, 60
		self.bullets_allowed=3

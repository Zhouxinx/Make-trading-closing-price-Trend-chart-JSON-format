import json

filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)



dates = []
months = []
weeks = []
weekdays =[]
closes =[]

for btc_dict in  btc_data:
	dates.append (btc_dict['date'])
	months.append (int(btc_dict['month']))
	weeks.append (int(btc_dict['week']))
	weekdays.append  (btc_dict['weekday'])
	closes.append (int(float(btc_dict['close'])))

import pygal
import math

line_chart = pygal.Line(x_label_rotation = 20 ,show_minor_x_labels = False)
line_chart.title = '收盘价￥'
line_chart.x_labels = dates
N = 20
line_chart.x_labels = dates[::N]
closes_log = [math.log10(_) for _ in closes]
line_chart.add('log收盘价',closes_log)
line_chart.render_to_file('收盘价对数折线图(￥).svg')

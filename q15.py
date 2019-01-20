#coding:utf-8
print("現在の時刻を「18:45」のように入力してください")
current_time = input(">>")
print("提示を「17:00」のように入力してください")
out_time = input(">>")
print("1時間あたりの残業代（円）を「1500」のように入力してください")
hour_money = float(input(">>"))

current_h = float(current_time[0:2])
current_m = float(current_time[3:5])
current_time_min = (60 * current_h) + current_m #分単位に統一
out_h = float(out_time[0:2])
out_m = float(out_time[3:5])
out_time_min = 60 * out_h + out_m
leave_time_min = current_time_min - out_time_min
leave_time_h = round((leave_time_min/60),2)
cal_money = leave_time_h * hour_money

print("あなたの残業時間は{0}時間です。残業代金は{1}円になります。".format(leave_time_h,cal_money))
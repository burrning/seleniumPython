import os

path = os.getcwd()
print(path)
# 通过getcwd.py文件的绝对路径来拼接日志存放路径
all_log_path = os.path.join(path + '\All_Logs')
error_log_path = os.path.join(path + '\Error_Logs')
print(all_log_path)
print(error_log_path)
path = os.path.join(os.getcwd(), 'screenshots/')
from auto_daka import auto_daka
import time

test_flag = False
users = {
    '2019500118': '044118',
    '1907200051': '110971',
    '2019500106': '174053',
}
num = 0
suc = []
date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f'当前打卡时间为:{date}\n')
start_time = time.time()
tt_error = 0
sleep_time = 6
for user in users:
    temp = True
    while temp:
        try:
            auto_daka(user, users[user], test_flag, sleep_time)
        except:
            sleep_time += 3
            print(f'学号{user}打卡失败,等待时间加3秒,现参数为{sleep_time},重新执行\n')
            tt_error += 1
        else:
            temp = False
    num += 1
    print(f'第{num}次打卡完成,学号{user}\n')
    suc.append(user)
end_time = time.time()
print(f'全部打卡完成,完成{num}人次打卡,学号为{suc}\n共用时{int(end_time - start_time)}秒,发生错误{tt_error}次')

# import tqdm
from tqdm import tqdm
from progressbar import ProgressBar
progress=ProgressBar()
import os

import time
# for i in tqdm(range(100)):
#     # print(i)
#     time.sleep(0.1)
#     pass

# for i in progress(range(100)):
#     time.sleep(0.1)
#     # print(i)

# set_description和set_postfix都用的kwargs传参，所以我们可以：

# 用字典传参 -> pbar.set_postfix({"key_1": "value_1", ...})
# 直接用关键字传参 -> pbar.set_postfix(key_1 = value_1, key_2 = value_2, ...)
# 混着用 -> pbar.set_postfix({"key_1": value_1, "key_2": value_2, ...}, key_3 = value_3, ...)

iter_object = range(10, 21)
pbar = tqdm(iter_object, 
                 total=len(iter_object),
                 leave=True, 
                 ncols=100, 
                 unit="个", 
                 unit_scale=False, 
                 colour="blue")

for idx, element in enumerate(pbar):
    time.sleep(0.5)
    pbar.set_description(f"No.{idx+1}")
    pbar.set_postfix({"正在处理的元素为": element})

# def progressBarDisplay(miniNum, maxNum, addNum):
#     '''
#      作者:小蓝枣
#      作用:模拟进度条
#      参数1:最小值
#      参数2:最大值
#      参数3:递增比例
#     '''
#     # 填充符号
#     fill_symbol = "#"
#     # 默认符号
#     default_symbol = "-"
#     # 进度条长度
#     bar_length = int((maxNum-miniNum)/addNum)
#     for i in range(0, bar_length + 1, 1):
#         # 【核心】清除屏幕
#         os.system('cls')
#         print("下载进度条: [" + i * fill_symbol + (bar_length - i) * default_symbol + "]")
#         print("进度百分比: (" + str(int((i / bar_length)*100)) + "%)")
#         # 延迟
#         time.sleep(0.2)

# progressBarDisplay(0, 100, 4)

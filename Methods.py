# 检测数据中对于时间，数据类型的处理方法
# 数值大小比较，异常数值取舍，特殊数值表示方式的处理方法
import pandas as pd

def fx():
    datas = pd.DataFrame([1,2,4,9,7,8,6,9,4,5,6,8,3])
    return datas.mean()

print(fx())
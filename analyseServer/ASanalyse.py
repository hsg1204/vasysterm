# coding: utf-8
'''
获取配置信息 @from管理服务器
    读取管理服务器数据库中分析任务信息，解析其中相机编码列表
获取待分析图片 @from存储服务器
    根据上面获得的相机编码列表依次从存储服务器中获取相应图片
根据模型检测图片内容
    根据任务类型进行深度学习前向推理检测，得到检测物体框
分析策略
    根据配置文件分析类型和检测结果分析城管相关业务
结果上报 @to存储服务器 @to管理服务器
    结果图片上传到存储服务器，结果内容添加到管理服务器上报事件信息数据库中
'''

def gettaskinfo():
    camlist = []
    taskidx = 0
    return camlist, taskidx

def getimage(camcode):
    camimg = ''
    caminfo = ''
    return camimg, caminfo

def analyse(camimg, caminfo):
    # detect image
    # strategy
    # upsend the result
    return

if __name__ == "__main__":
    print "analyse task"
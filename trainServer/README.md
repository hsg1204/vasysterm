# training server
主要功能
    服务器注册 @to管理服务器
        使用配置文件存储管理服务器信息，通过握手机制将服务器添加到管理服务器数据库中
    服务器状态上报 @to管理服务器
        定时上报服务器状态，服务器GPU使用情况，显存剩余情况
    定时获取图片 @from存储服务器
        定时从存储服务器中下载图片
    图片标注
    ​   根据任务类型标注需要识别和检测的内容​​​
        其实可以另开一个服务器专门做标注任务，不将标注任务放在训练服务器中​
    模型训练
        也可纳入管理中
    模型生成 @to存储服务器 @to管理服务器
        #训练模型信息 存入管理服务器数据库中，模型文件存入存储服务器中
实现方式
    Linux后台任务，人工控制

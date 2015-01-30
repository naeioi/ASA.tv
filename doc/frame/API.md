Command-line-API
===========================

用正则表达式来匹配url:

	^cms/(?P<path>(([a-z0-9A-Z-_]+/)*))(?P<command>([a-z0-9A-Z-_ /.])+)$
	

* cd 如果成功后台会以json的消息返回{"msg":"OK"}(后台只会告诉你这个文件存在不存在)，如果失败，后台会返回{"msg":"{{path}}"}，期中path表示第一个不存在的folder
* mkdir [-p] 创建文件，基本同unix-like系统的操作
* rm [-r] 删除文件，基本同unix-like系统的操作



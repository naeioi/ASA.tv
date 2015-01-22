CMS由两个部分组成：用户系统，文件系统

=====================================
1.文件系统:

    大概是做成unix-like的那样
    /
        home
        public
        files

    /home 同unix-like的home一样，会存放所用用户的名字对应的
    文件夹，这些目录下会含有该用户上传的视频，可以有子目录，
    可以嵌套

    /public 下是显示在视频站上的结构。同样的,可以有子目录，
    可嵌套

    /files 这一部分其实是CDN-director在CMS的API，通过视频的
    token返回几个可用的URL

    逻辑视频文件使用引用计数规则（如果一个逻辑视频文件没有在
    任何文件夹里面存在，则会被删除，同时对CDN-director发出
    删除指令)
    
    文件以及文件夹使用ACL(access control list)规则进行权限管理

=====================================
2.用户系统:

	super admin:
		站长，可以任免副站长，含有所有权限
	admin:
   		副站长，除了不能任免副站长一万，有站长其他所有的权限
   	user:
   		普通用户，在/home下有自己的独立的文件夹
   	group:
    	用户组，在/group下有该组独立的文件
    group super host:
    	用户组主，由super admin和admin任免，越过该组对应的ACL权限系统(下面介绍)
	group host:
		用户组副主，由group super host任免，除此之外有group super host的所有权限
		    	
======================================
另外之一:

	文件和文件夹的acl
	read属性，文件(文件夹)对于哪些用户(用户组)可见。特别地，对文件来说,如果该文件对A用户(用户组)可见,则A用户(用户组)可以在[网盘层面]上面播放(下载)这个视频
	read_by_user(最多可以指定20个,包括自己)
	read_by_group(最多可以指定20个)
	
	remove属性，哪些用户(用户组)可以删除这个文件(文件夹)
	removed_by_user(最多可以指定5个,包括自己,最少一个)
	removed_by_group(最多可以指定3个)
	
	create属性，哪些用户(用户组)可以在这个文件夹下添加文件
	created_by_user(最多可以指定5个，包括自己，最少一个)
	created_by_group(最多可以指定3个)
	
	特别地, super admin和admin和该组的group host在此规则之外，拥有查看删除创建所有文件的权限。
	
========================================
另外之二:
	
	视频从上传完视频到审核再到放到视频站过程
	需要反复说明的几点：
		1./public下的文件夹直接对应到视频站的分类，所以文件被连接到/public/xxxxx下就表示审核通过，可以被任何用户看到
		2./public下的文件夹实际上是一个group, group super host就是版主, group host是副版主
		3.在逻辑组织中有一个group叫做all,所有用户(如果没有注册就是ip作为用户名)都在这个group里面.还有一个group叫做ASAer，所有注册用户都在这里面.
		4./public/xxxxx和/public/xxxxx下的所有文件的read_by_group都含有all
		5./public/xxxxx会对应一个/home/xxxxx_upload,/home/xxxxx_upload的
		created_by_group都有ASAer,同时/public/xxxxx的group host(super host)
		也是/home/xxxxx_upload的group host(super host)
		/
			home/
				xxxxx_upload
					group host: a0,a1,...an
					group super host: b
				...
			public/
				xxxxx
					group host: a0,a1,...an
					group super host: b
					(the same as /home/xxxxx_upload/)
				...
			

	下面开始介绍过程：
		1.用户上传文件到/home/xxxxx_upload
		2.group admin(super admin)看到视频，审核
		3.审核通过，admin把文件移动到/public/xxxxx,并把原来在/home/xxxxx_upload的文件删除
CMS由两个部分组成：用户系统，文件系统

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

2.用户系统:
    还是做成unix-like的那样, 对应的组会有一个文件夹，对应的
    用户会有一个文件夹。

    用户系统会包括几种类型
    super admin, admin, category admin, user

    super admin     :   超级站长（只有一个)
                        拥有所有权限
    admin:              站长     (可以多个)
                        被超级站长任免
                        拥有所有权限
    category admin  :   版主    （每个版面只有一个)
                        被站长任免
                        拥有该版面下的所有权限
    user            :   普通用户
                        注册即可
                        只有在该用户下的所有的权限

    group: group在/home下也会单独建立一个文件夹(可以和
    用户重名,但不能和其他group重名), group文件夹会另外记录
    一些用户的信息，这些用户被称为该group的member,这些member
    拥有该group的所有权限

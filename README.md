### 介绍
Tblog是个人博客系统。

### 基本功能
* 发布博文，查看博文
* 评论和点赞
* 反垃圾系统

### 集成的开源代码
* DjnagoSuit
* django-imagekit
* duoshuo
* pagination
* django-wmd-editor

## 前台
纯属手写，很难看吧～～

## 分页
用了django-pagination

## 评论
使用多说（之后改成Django自带的，不过效果很差，得找个时间定制）


## markdonw编辑器
使用了`django-wmd-editor`

## markdown渲染器
`markdown_deux`


### 图片处理
本来是想用django-stdimage的，因为它是个神器，详见[Xadmin中形成缩略图](http://tulpar008.github.io/xadmin-list_displayzhong-xian-shi-suo-lue-tu.html)    
##### 后来偶遇看到一个神器django-imagekit，决定用它，原因很简单，没用过。

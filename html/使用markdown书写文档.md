
# 使用markdown书写文档


[返回文档中心](/index.html)

文档中心采用了Markdown语言作为富文本编辑器。
借助 Mantels Markdown 用户可以简单的完成文本、图片等多媒体信息和超链接的添加和排版。

## 什么是Markdown

Markdown是一种纯文本标记语言，通过简单的符号，用户便可以创作出排版精致，富含大量信息的文本。
同时，得益于纯文本书写，Markdown文件可以非常轻松的保存、共享。

## 快速入门

本站支持标准Markdown语法，如果您已经有Markdown使用经验，可以非常快的上手使用。
并且通过本页面，您可以实时查看渲染后的效果。

如果您没有使用过Markdown，可以查看 [《入门手册》](入门手册.md)。

`tip`: 当前版本的文档中心的文档渲染功能由MDwiki提供，部分语法规则和标准Markdown有所区别，在入门手册中对此进行了说明，在后续版本中会提供标准的Markdown渲染和拓展。

## 使用html

除了使用Markdown语法，您也可以直接内嵌html标签来实现部分markdown较难实现的复杂功能。

例如添加一个音乐播放器：

HTML代码如下（网易云外链播放器）：
```
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=462290&auto=0&height=66"></iframe>

```

效果：
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=462290&auto=0&height=66"></iframe>



## Markdown解析器

Mantels Markdown基于Markdown语法解析器marked( [github](https://github.com/chjj/marked) ).

最后由[MatthiasHua](https://github.com/MatthiasHua)编辑于`2018/2/3`

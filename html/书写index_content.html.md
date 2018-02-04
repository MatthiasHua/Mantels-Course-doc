书写index_content.html
==========

[返回文档中心](/index.html) | [关于文档中心](content.html)

index_content.html
------

index_content.html文件中包含了index的内容和简单的排版信息，通过它，我们可以快速生成一个index文件。
例如:

```
t:标题名称
tab-number:4
tab1:tab名称
tab2:tab名称
tab3:tab名称
tab4:tab名称

tab:
-标题-
left:
endleft
right:
endright
endtab

tab:
-标题-
left:
endleft
right:
endright
endtab

tab:
-标题-
left:
endleft
right:
endright
endtab

tab:
-标题-
left:
endleft
right:
endright
endtab

```

t:为整个文档中心的大标题，例如本站大标题为`Mantels Courese文档中心`
`tab-number`为`tab`的数量，限制为2~4个

自动生成初始化index_content.html
------
index_content.html可以自动初始化。

使用`create_index.py`生成index。
```
python create_index.py init //生成一个初始化文件 文件名为index_content.html tab数量为3个
python create_index.py init -o 文件名 -t tab数量 //生成一个初始化文件 文件名和tab数量自定义
python create_index.py -h //查看帮助
```

最后由[MatthiasHua](https://github.com/MatthiasHua)编辑于`2018/2/4`

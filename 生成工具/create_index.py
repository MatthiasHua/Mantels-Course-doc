import os
import sys

path = os.path.dirname(os.path.realpath(__file__))

def get_head(title, tab_number, tablist):
	return '''
<html>
<head>
	<meta charset="utf-8">
	<title>Mantels Courese文档中心</title>
	<link rel="stylesheet" href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
	<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<style>
		h1 {
			color: #666;
		}

		.nav-tabs {
			border: 0px;
		}

		.nav-tabs>li.active>a, .nav-tabs>li.active>a:focus, .nav-tabs>li.active>a:hover {
			border: 0px;
		}

		.nav-tabs>li>a {
			border: 0px;
		}

		.nav-tabs>li>a:hover {
			background: white;
			border: 0px;
		}

		.nava, .nav-tabs>li.active>a, .nav-tabs>li.active>a:focus, .nav-tabs>li.active>a:hover{
			color: #bbb;
		}

		input::-ms-input-placeholder {
			text-align: center;
		}

		input::-webkit-input-placeholder {
			text-align: center;
		}

		a {
			color: #3090e4;
		}

		a:hover {
			color: #2571b3;
			text-decoration: none;
		}

		p {
			color: #888;
		}

		span {
			color: #666;
		}

		.head {
			color: #666;
			font-size: 16px;
		}

		.foot {
			color: #bbb;
			padding: 10px;
		}

		.foot:hover {
			color: #3090e4;
			text-decoration: none;
		}

		div.a-button {
			float: left;
			width: 120px;
			border-radius: 5px;
			text-align: center;
			background: #ebf6ff;
			margin: 4px 10px 14px 0px;
			padding: 10px 20px 10px 20px;
		}

		a.a-button:hover {
			color: white;
		}

		.a-button:hover {
			background: #3090e4;
			cursor: pointer;
		}

	</style>
</head>
<body  onload="load()">
	<div class="container">
		<h1 style ="text-align:center ">''' + title +'''</h1>
		<hr>
		<br>
		<div class ="col-md-6" style="float: none;display: block;margin-left: auto;margin-right: auto; text-align: center;">
				<div class="input-group" style="width: 100%; position: relative; text-align: center;">
            <input type="text" class="form-control" placeholder="搜索" style="width: 100%; font-size: 18px; font-weight: 300; height: 42px; border-radius: 5px;">
				</div>
    </div>
		<br><br>
		<div class="col-md-6" style="float: none;display: block;margin-left: auto;margin-right: auto;">
			<ul class="nav nav-tabs" id="myTab">''' + get_tab(tab_number, tablist) + '''
			</ul>
		</div>
	</div>
	<br><br>
	<div class="container">
		<div id="myTabContent" class="tab-content">
'''

def get_tab(tab_number, tablist):
	if tab_number in [2, 3, 4]:
		returntext = ""
		for i in range(tab_number):
			if len(tablist[i].split('-')) != 2:
				print("请检查tab是否填写正确")
				quit()
			returntext += '''<li class="col-sm-''' + str(int(12/tab_number)) + '''" style="margin: 0px; text-align: center;">
		<img class="navimg" src="/''' + tablist[i].split('-')[1] + '''" style="width: 50px;"></img>
		<a class="nava" href="#a''' + str(i + 1) + '''" data-toggle="tab">''' + tablist[i].split('-')[0] + '''</a>
	</li>'''
		return returntext
	print("tab数量请控制在2-4个")
	quit()

foot = '''
		</div>
	</div>
	<hr>
	<div style="float: right; height: 50px;">
		<a class="foot">主页</a>
		<a class="foot">源码 </a>
		<a class="foot">问题反馈</a>
	</div>
<script>
	//更改颜色
	function change_color(selector, color) {
		selector.children('.navimg').css("background", color)
		selector.children('.nava').css("color", color)
	}

	function load() {
		//初始化 选中第一个
		$('#myTab li:eq(0) a').tab('show');
		change_color($('li'), "#bbb")
		change_color($('li:eq(0)'), "#3090e4")

		//移入事件
		$('li').mouseover(function(){
			if ($(this).attr("class") == "col-sm-4") {
					change_color($(this), "#555")
			}
		})

		//移出事件
		$('li').mouseout(function(){
			if ($(this).attr("class") == "col-sm-4") {
				change_color($(this), "#bbb")
			}
		})

		//点击事件
		$('li').click(function(){
			change_color($('li'), "#bbb")
			$(this).children('.nava').tab('show');
			change_color($(this), "#3090e4")
		})
	}

	//div绑定链接
	$('div .a-button').click(function(){
		window.location.href = $(this).children('a').attr('href')
	})

	$('div .a-button').mouseover(function(){
		$(this).children('a').css("color", "white")
	})
	$('div .a-button').mouseout(function(){
		$(this).children('a').css("color", "#3090e4")
	})

	$("div.tab-pane:eq(0)").attr("id", "a1")
	$("div.tab-pane:eq(1)").attr("id", "a2")
	$("div.tab-pane:eq(2)").attr("id", "a3")


</script>
</body>
</html>
'''

def headsytle(text):
	return '''
<div class ="text-align: center;">
	<div class="col-sm-5" style="float: left; height:40px;"><div style="position: relative; top:20px; width:100%; border:1px solid #bbb;"></div></div>
	<span class="col-sm-2" style="font-size: 28px; text-align: center;">''' + text + '''</span>
	<div class="col-sm-5" style="float: left; height:40px;"><div style="position: relative; top:20px; width:100%; border:1px solid #bbb"></div></div>
</div>
<div style="height: 70px;"></div>
'''

def hstyle(text):
	return '''<p class="head">'''+ text +'''</p>'''

def pstyle(text):
	return '''<p>'''+ text +'''</p>'''

def astyle(text):
	return '''<p><a href="''' + text.split('-')[1] + '''">''' + text.split('-')[0] + '''</a><br></p>'''

def buttonstyle(text):
	returntext = '''<div  style="height: auto; display: inline-block;">'''
	for i in text.split(' '):
		returntext += '''<div class="a-button"><a href="'''+ i.split('-')[1] +'''">'''+ i.split('-')[0] + '''</a></div>'''
	returntext += '''</div><br>'''
	return returntext

def get(name, lines, errortext):
	for i in lines:
		if i.startswith(name):
			return  i.split(name)[1].split('\n')[0]
	print(errortext)
	quit()

rule = [('tab:',   '''<div class="tab-pane fade">'''),\
	    ('endtab', '''</div>'''),\
	    ('-',      headsytle),\
	    ('left:', '''<div style="height: auto; width: 100%; display:inline-block;"> <div class="col-sm-6">'''),\
	    ('endleft', '''</div>'''),\
	    ('right:', '''<div class="col-sm-6">'''),\
	    ('endright', '''</div></div><br><br>'''),\
	    ('h:', hstyle),\
	    ('p:', pstyle),\
	    ('a:', astyle),\
	    ('b:', buttonstyle),\
	    ('br:', '''<br>'''),\
	    ]

def create_index(input = "index_content.html", output = "index.html"):
	with open(path + '\\' + input, 'r', encoding='UTF-8') as content:
		with open(path + '\\' + output, 'w', encoding='UTF-8') as index:
			lines = content.readlines()
			title = get("t:", lines, "请给定标题,详情见 -h title。")
			tab_number = int(get("tab-number:", lines, "请给定tab数量,详情见 -h tab-number。"))
			tablist = []
			for i in range(tab_number):
				tablist.append(get( "tab" + str(i + 1) + ":", lines, "请给定tab名称,详情见 -h tab-name。"))
			index.write(get_head(title, tab_number, tablist))
			for line in lines:
				for i in rule:
					if line.startswith(i[0]):
						if isinstance(i[1],str):
							index.write(i[1])
						else:
							index.write(i[1](line.split(i[0])[1]))
			index.write(foot)

def printhelp():
	print("Usage:")
	print("  %-20s" % "python create_index.py <command> [options]")
	print()
	print("Commands:")
	print("  %-30s%s" % ("init", "生成一份内容模板"))
	print("  %-30s%s" % ("create", "根据内容模板生成网页"))
	print()
	print("General Options:")
	print("  %-30s%s" % ("-h", "帮助"))
	print("  %-30s%s" % ("-i <path>", "输入文件，默认为index_content.html"))
	print("  %-30s%s" % ("-o <path>", "输出文件，在init模式下默认为index_content.html，在create模式下默认为index.html"))
	print("  %-30s%s" % ("-t <tab-number>", "tab的数量(2-4)"))

def create_content(output = "index_content.html", tab_number = 3):
	with open(path + '\\' + output, 'w', encoding='UTF-8') as content:
		content.write("t:标题名称\n")
		content.write("tab-number:%s\n" % str(tab_number))
		for i in range(tab_number):
			content.write("tab" + str(i + 1) + ":tab名称\n")
		content.write("\n")
		for i in range(tab_number):
			content.write("tab:\n-标题-\nleft:\nendleft\nright:\nendright\nendtab\n\n")
		content.write("#提示:\n#-标题- tab下的大标题\n#h:标题 每个大标题下的小标题\n#p:文字 无链接文字\n#a:文字-链接 带链接文字\n#b:文字-链接 文字-链接... 带链接按钮，可以输入多组\n")


if __name__ == '__main__':
	argv = sys.argv
	argv.pop(0)
	if argv == []:
		create_index()
		quit()
	if argv[0] == '-h':
		printhelp()
	if argv[0] == 'init':
		argv.pop(0)
		output = "index_content.html"
		tab_number = 3
		for i in range(len(argv)):
			if argv[i] == "-o":
				if i == len(argv):
					print("请给出输出文件地址")
					quit()
				else:
					output = argv[i + 1]
			if argv[i] == "-t":
				if i == len(argv):
					print("请给出tab的数量")
					quit()
				else:
					tab_number = int(argv[i + 1])
		create_content(output, tab_number)

	if argv[0] == 'create':
		argv.pop(0)
		input = "index_content.html"
		output = "index.html"
		for i in range(len(argv)):
			if argv[i] == "-i":
				if i == len(argv) - 1:
					print("请给出输入文件地址")
					quit()
				else:
					input = argv[i + 1]
			if argv[i] == "-o":
				if i == len(argv) - 1:
					print("请给出输出文件地址")
					quit()
				else:
					output = argv[i + 1]
		create_index(input, output)

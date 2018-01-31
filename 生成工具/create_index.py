import os

path = os.path.dirname(os.path.realpath(__file__))

head = '''
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
		<h1 style ="text-align:center ">Mantels Courese文档中心</h1>
		<hr>
		<br>
		<div class ="col-md-6" style="float: none;display: block;margin-left: auto;margin-right: auto; text-align: center;">
				<div class="input-group" style="width: 100%; position: relative; text-align: center;">
            <input type="text" class="form-control" placeholder="搜索" style="width: 100%; font-size: 18px; font-weight: 300; height: 42px; border-radius: 5px;">
				</div>
    </div>
		<br><br>
		<div class="col-md-6" style="float: none;display: block;margin-left: auto;margin-right: auto;">
			<ul class="nav nav-tabs" id="myTab">
				<li class="col-md-4" style="margin: 0px; text-align: center;">
					<img class="navimg" src="/help.png" style="width: 50px;"></img>
					<a class="nava" href="#a1" data-toggle="tab">帮助文档</a>
				</li>
				<li class="col-md-4" style="margin: 0px; text-align: center;">
					<img class="navimg" src="/develop-doc.png" style="width: 50px;"></img>
					<a class="nava" href="#a2" data-toggle="tab">开发文档</a>
				</li>
				<li class="col-md-4" style="margin: 0px; text-align: center;">
					<img class="navimg" src="/develop-doc.png" style="width: 50px;"></img>
					<a class="nava" href="#a3" data-toggle="tab">开放api</a>
				</li>
			</ul>
		</div>
	</div>
	<br><br>
	<div class="container">
		<div id="myTabContent" class="tab-content">
'''

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
			if ($(this).attr("class") == "col-md-4") {
					change_color($(this), "#555")
			}
		})

		//移出事件
		$('li').mouseout(function(){
			if ($(this).attr("class") == "col-md-4") {
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
	<div class="col-md-5" style="float: left; height:40px;"><div style="position: relative; top:20px; width:100%; border:1px solid #bbb;"></div></div>
	<span class="col-md-2" style="font-size: 28px; text-align: center;">''' + text + '''</span>
	<div class="col-md-5" style="float: left; height:40px;"><div style="position: relative; top:20px; width:100%; border:1px solid #bbb"></div></div>
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


rule = [('tab:',   '''<div class="tab-pane fade">'''),\
	    ('endtab', '''</div>'''),\
	    ('-',      headsytle),\
	    ('left:', '''<div style="height: auto; width: 100%; display:inline-block;"> <div class="col-md-6">'''),\
	    ('endleft', '''</div>'''),\
	    ('right:', '''<div class="col-md-6">'''),\
	    ('endright', '''</div></div><br><br>'''),\
	    ('h:', hstyle),\
	    ('p:', pstyle),\
	    ('a:', astyle),\
	    ('b:', buttonstyle),\
	    ('br:', '''<br>'''),\
	    ]

with open(path + '\\index_content.html', 'r', encoding='UTF-8') as content:
	with open(path + '\\index.html', 'w', encoding='UTF-8') as index:
		index.write(head)
		for line in content.readlines():
			for i in rule:
				if line.startswith(i[0]):
					if isinstance(i[1],str):
						index.write(i[1])
					else:
						index.write(i[1](line.split(i[0])[1]))
		index.write(foot)

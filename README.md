任务需求:

1. 实现一个基本的联系人管理应用
2. 只需要通过命令行操作, 基于文本存储
3. 支持如下命令: 

        contact list  : 列举所有联系人
        contact add ***/*** 增加新的联系人和手机号
        contact delete ***  删除联系人
        contact update ***/*** 更新联系人信息
        contact search *** 查找联系人

要求:
   基于TDD的方式进行开发
   代码覆盖率90%以上
   语言不限
   <代码整洁之道>阅读分享结束前提供所有源码和测试结果.
   
运行：

######进入到项目目录tdd_coding中
1. python app/manager.py add Tom
2. python app/manager.py list
3. python app/manager.py delete Tom
4. python app/manager.py search Tom
5. python app/manager.py update Tom
   

测试：
1. 进入项目目录：J:\pro\tdd_coding
2. 执行： python -m unittest discover -v

覆盖率：
1. coverage run -m unittest discover -v
2. coverage report
```
Name                          Stmts   Miss  Cover
-------------------------------------------------
app\__init__.py                   0      0   100%
app\config.py                     8      0   100%
app\manager.py                  132     11    92%
app\test\__init__.py              0      0   100%
app\test\test_db.py              24      1    96%
app\test\test_functional.py      74      1    99%
app\utils.py                     17      1    94%
-------------------------------------------------
TOTAL                           255     14    95%
```
3. coverage html -d covhtml  生成html文档
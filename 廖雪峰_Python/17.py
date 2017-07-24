# 1 错误处理
# try...
# except: division by zero
# finally...
# END

# 2 调试
# print()调试法
# assert 调试法：凡是用print()来辅助查看的地方，都可以用断言（assert）来替代 < 启动Python解释器时可以用-O参数来关闭assert >
# logging(): 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
# pdb: python3 -m pdb err.py (l 查看代码；n 跳到下一条语句； p var 查看变量var的值；q 退出)
# pdb设置断点： import pdb ； 断点处 pdb.set_trace() < 运行到此处会暂停 >
# IDE : Pycharm     

# 3 测试
# 单元测试：TDD unittest
# 文档测试
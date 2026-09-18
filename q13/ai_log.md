核心提示：修改cli.py，name仅包含空白字符时，返回退出码为2
智能体改动：在main中添加if条件判断“if not a.name.strip()"
人工检查：删除main函数后运行部分
人工验证：pytest两个用例全部通过，空白输入返回退出码2

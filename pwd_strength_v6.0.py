# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 9:16'

# 判断密码强度
# 循环终止
# 保存密码及强度到文件中
# 定义一个文件工具类


class PasswordTool:
    """
    密码工具类
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print("密码长度要求至少8位！")

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print("密码要求包含数字！")

        # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print("密码要求包含字母！")

    def check_number_exist(self):
        """
        判断字符串是否含有数字
        :param password_str:
        :return:
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
        判断字符串是否含有字母
        :param password_str:
        :return:
        """
        has_letter = False

        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    """
    文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath)
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
    主函数
    :return:
    """
    try_times = 5
    filepath = 'password_6.0.txt'
    # 实例化文件工具对象
    file_tool = FileTool(filepath)

    pwd_s = {1: "非常弱", 2: "弱", 3: "强"}

    while try_times > 0:
        password = input("请输入密码：")

        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = "密码：{}，强度：{}\n".format(password, pwd_s[password_tool.strength_level])
        # 写操作
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print("恭喜！密码强度合格！")

            break
        else:
            print("密码强度不合格！")
            try_times -= 1
        print()

    if try_times <= 0:
        print("尝试次数过多，密码设置失败")


    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()

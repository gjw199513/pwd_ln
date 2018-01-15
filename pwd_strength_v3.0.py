# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/15 0015 上午 9:16'

# 判断密码强度
# 循环终止
# 保存密码及强度到文件中


def check_number_exist(password_str):
    """
    判断字符串是否含有数字
    :param password_str:
    :return:
    """
    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
    判断字符串是否含有字母
    :param password_str:
    :return:
    """
    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
    主函数
    :return:
    """
    try_times = 5
    pwd_s = {1: "非常弱", 2: "弱", 3: "强"}
    while try_times > 0:
        password = input("请输入密码：")

        # 密码强度
        strength_level = 0

        # 规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print("密码长度要求至少8位！")

        # 规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print("密码要求包含数字！")

        # 规则3：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print("密码要求包含字母！")

        f = open('password_3.0.txt', 'a')
        f.write("密码：{}，强度：{}\n".format(password, pwd_s[strength_level]))
        f.close()

        if strength_level == 3:
            print("恭喜！密码强度合格！")

            break
        else:
            print("密码强度不合格！")
            try_times -= 1
        print()



    if try_times <= 0:
        print("尝试次数过多，密码设置失败")


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-

import re
import json
import os

def read_config():
    """
    读取配置文件，获取 Java错误码文件位置 和 错误信息文件位置

    :return: 一个包含两个元素的数组。第0位元素为Java错误码文件位置，第1位元素为错误信息文件位置。
    """
    config_file_path = 'D:\python\config'
    with open(config_file_path, 'r') as f:
        config_file_str = f.read()

    # 考虑找不到路径的场景
    code_java_path = re.findall("error_code_java_file_path.*=.*\"(.+)\"", config_file_str)[0]
    error_msg_json_path = re.findall("error_msg_json_file_path.*=.*\"(.+)\"", config_file_str)[0]

    return [code_java_path, error_msg_json_path]

def cmp_error_code(code_java_path, error_msg_json_path):

    with open(code_java_path, 'r') as code_file:
        code_file_str = code_file.read()

    with open(error_msg_json_path, 'r') as msg_file:
        msg_json = json.load(msg_file)

    # 考虑对错误码做去重校验
    code_arr = re.findall("String.+\"(.+)\"", code_file_str)

    print '=========== Error codes which has no error message ======================'
    need_2_translate_code_arr = []
    for code in code_arr:
        if not code in msg_json:
            need_2_translate_code_arr.append(code)

    print need_2_translate_code_arr

if __name__ == "__main__":
    while(True):
        config_arr = read_config()

        # 需要考虑找不到路径的场景
        code_java_path = config_arr[0]
        error_msg_json_path = config_arr[1]

        print "======================== Configuration ==============================="
        print "error code Java file path: " + code_java_path
        print "error message JSON file path: " + error_msg_json_path

        print "=========================== Command =========================="
        print "Please input your command:"
        print "1: Begin to compare."
        # print "2: Config the file path"

        str = raw_input("\n Your command is: ")

        if str == "1":
            print "Begin to compare."
            cmp_error_code(code_java_path, error_msg_json_path)
            os.system("pause")
            break;
        # elif str == "2":
        #     code_path = raw_input("Please input the error code Java file path:")
        #     err_msg_path = raw_input("Please input the error message JSON file path:")
        #
        #     print "Configuration has been saved."
        else:
            print "Invalid input. Please try again."






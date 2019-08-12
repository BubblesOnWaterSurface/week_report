import os
import re
import time
import win32api
import creat_txt as ct


# 显示list下files
def print_filesn(list):
    n = 1
    for thing in list:
        print('\t' + str(n) + '、' + thing)
        n += 1
    time.sleep(0.2)
    # print('【按Ctrl + C可随时退出程序】\n')


# 循环将in同类型文件归类
def grouping_files(inputed_list, output_list, filetype):
    m = 0
    for i in inputed_list:
        (shotname, extension) = os.path.splitext(inputed_list[m])
        filetype_firm = '.' + str(filetype)
        if str(extension) == filetype_firm:
            output_list.append(inputed_list[m])
        m += 1
    return output_list


# 重组完整文件名
def recombination(path, name):
    return os.path.join(path, name)


# 说明以及配置文件相关
# 检测是否存在paths_info文件，判断是否生成并引导
def check_paths_info_txt(info_file):
    try:
        with open(info_file) as k:
            print('\n---正在核对%s的内容---' % ct.ph_name)
    except (OSError, FileNotFoundError):
        ct.path_info()
        input('\n---初次生成%s文件，请参考readme说明更改%s的内容---\n'
              '\n【更改内容后请返回此处按任意键继续】:' % (ct.ph_name, ct.ph_name))


# 检测是否存在web_info文件，判断是否生成并引导
def check_web_info_txt(info_file):
    try:
        with open(info_file) as k:
            print('\n---正在核对%s内容---' % ct.web_name)
    except (OSError, FileNotFoundError):
        ct.web_info()
        input('\n---初次生成%s文件，请参考readme说明更改%s的内容---\n'
              '\n【更改内容后请返回此处按任意键继续】:' % (ct.web_name, ct.web_name))


def open_filter(path):
    # win32api.ShellExecute(0, 'open', path, '', '', 1)
    try:
        win32api.ShellExecute(0, 'open', path, '', '', 1)
    except Exception:
        print('---%s里文件路径错了---' % ct.ph_name)
    else:
        pass




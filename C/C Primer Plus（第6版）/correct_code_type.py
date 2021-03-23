import os
import re

class CorrectCodeLanguage:
    """
        纠正 markdown 文件中的代码标签中语言类型
    """


    def __init__(self, path, old_lang, new_lang, debug=False):
        """
            初始化方法

            args:
                path (str): 文件目录
                old_lang (str): 要替换的编程语言
                new_lang (str): 替换的编程语言
                debug (bool): 是否打印日志
            
        """
        self.path = path
        self.old_lang = old_lang
        self.new_lang = new_lang
        self.debug = debug

    
    def correct(self):
        """
            执行纠正
        """
        dirs = self.__get_dirs()
        for dir in dirs:
            self.__correct_code_language(dir)


    def __get_dirs(self):
        """
            获取路径下所有目录（不包含子目录）

            args:
                path (str): 目录路径
            
            return:
                返回目录数组
        """
        dirs = []
        files = os.listdir(self.path)
        for file in files:
            if os.path.isdir(self.path + file):
                # 过滤掉 images 目录
                if file == 'images' or file == '__pycache__':
                    continue

                print(f'dir: {file}')
                dirs.append(self.path + file)
        return dirs


    def __correct_code_language(self, path):
        """
            纠正代码语言
        """
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(path + '/' + file):
                with open(path + '/' + file, mode='r+', encoding='utf-8') as f:
                    contents = f.readlines()
                    f.seek(0)
                    f.truncate()
                    for line in contents:
                        line = line.replace('```{}'.format(self.old_lang), '```{}'.format(self.new_lang))
                        f.writelines(line)
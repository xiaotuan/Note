import os
import re

class ReplaceImage:
    """
        替换文件中的 "./images" 为 "../images"
    """

    
    def __init__(self, path, debug=False):
        """
            初始化方法

            args:
                path (str)：目录路径
                debug (bool)：是否打印日志信息

        """
        self.path = path
        self.debug = debug


    def replace_image(self):
        """
            替换图片
        """
        print(f'replace image')
        dirs = self.__get_dirs()
        for dir in dirs:
            self.__replace_image_path(dir)


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


    def __replace_image_path(self, path):
        """
            替换图像路径
        """
        files = os.listdir(path)
        # print(f'__replace_image_path path: {path}, length: {len(files)}')
        for file in files:
            # print(f'__replace_image_path file: {file}')
            if os.path.isfile(path + '/' + file):
                # print(f'replace file: {file}')
                with open(path + '/' + file, mode='r+', encoding='utf-8') as f:
                    contents = f.readlines()
                    header = re.compile('# |## ')
                    # print(f'first； {contents[0]}， match: {re.match(header, contents[0])}')
                    if header:
                        contents[0] = re.sub(header, '### ', contents[0], count=1)
                    f.seek(0)
                    f.truncate()
                    for line in contents:
                        line = line.replace('./images', '../images')
                        f.writelines(line)
                
                        
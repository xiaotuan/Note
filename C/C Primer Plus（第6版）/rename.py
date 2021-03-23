import os
import re

class Rename:
    """
        重命名数据文章名称
    """


    def __init__(self, path, debug=False):
        """
            初始化方法

            args:
                path (str): 目录路径
                debug (bool): 是否打印调试信息

        """
        self.path = path
        self.debug = debug


    def rename(self):
        """
            执行重命名
        """
        dirs = self.__get_dirs(self.path)
        for dir in dirs:
            self.__rename_dir_file(dir)


    def __compare(self, item1, item2):
        """
            比较 item1 和 item2 文件名中小节的大小（比如文件为"1.2 选择C语言的理由.md"，则比较的是 1.2 的值的大小），
            用于文件排序；当 item1 大于 item2 时返回 1；当 item1 等于 item2 时返回 0；
            当 item1 小于 item2 时返回 -1。

            args:
                item1 (str)：文件名
                item2 (str): 文件名
                
            return (int): 当 item1 大于 item2 时返回 1；当 item1 等于 item2 时返回 0；当 item1 小于 item2 时返回 -1
        """
        # 小节标签的正则表达式，例如 1.2，1.10.2 等等
        subsection = re.compile('\w{1,2}(.\d{1,2})?(.\d{1,2})?(.\d{1,2})?')
        match = re.match(subsection, item1)
        # 获取 item1 的小节值
        item1Prefix = item1[match.span()[0]:match.span()[1]].strip()
        match = re.match(subsection, item2)
        # 获取 item2 的小节值
        item2Prefix = item2[match.span()[0]:match.span()[1]].strip()
        # 使用 "." 字符分割小节值，比如 1.10.2 会被分割成 [1, 10, 2]
        item1Prefixs = item1Prefix.split(".")
        item2Prefixs = item2Prefix.split(".")
        # 默认两个文件的小节值相等
        result = 0
        # 取小节值数组长度最小的作为循环下标
        length = len(item1Prefixs) if len(item1Prefixs) < len(item2Prefixs) else len(item2Prefixs)
        for i in range(length):
            # 如果小节值的长度相等，则直接比较它们的大小
            if (len(item1Prefixs[i]) == len(item2Prefixs[i])):
                if item1Prefixs[i] > item2Prefixs[i]:
                    result = 1
                    break
                elif item1Prefixs[i] < item2Prefixs[i]:
                    result = -1
                    break
            else:
                # 如果小节值的长度不相等，则比较它们的长度
                result = 1 if len(item1Prefixs[i]) > len(item2Prefixs[i]) else -1
                break

        # 如果循环比较后值仍然为 0，则比较小节值数组的长度
        if result == 0:
            if len(item1Prefixs) > len(item2Prefixs):
                result = 1
            elif len(item1Prefixs) < len(item2Prefixs):
                result = -1

        return result


    def __bubbleSort(self, arr):
        """
            冒泡排序

            args:
                arr (array): 要排序的数组对象
                
        """
        n = len(arr)
        # 遍历所有数组元素
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                if self.__compare(arr[j], arr[j+1]) > 0 :
                    arr[j], arr[j+1] = arr[j+1], arr[j]


    def __get_dirs(self, path):
        """
            获取路径下所有目录（不包含子目录）

            args:
                path (str): 目录路径
            
            return:
                返回目录数组
        """
        dirs = []
        files = os.listdir(path)
        for file in files:
            if os.path.isdir(path + file):
                # 过滤掉 images 目录
                if file == 'images':
                    continue
                print(f'dir: {file}')
                dirs.append(path + file)
        return dirs


    def __rename_dir_file(self, path):
        """
            重命名目录下的文件名成类似 "01-xxxx.md" 格式

            args:
                path (str): 目录路径

        """
        if self.debug:
            print(f'rename path: {path}')
        index = 1
        mdFiles = []
        files = os.listdir(path)
        if self.debug:
            print(f'file length: {len(files)}')
        # 第几章 正则表达式
        chapter = re.compile("第\d*章")
        # 小节文件 正则表达式
        subsection = re.compile('\w{1,2}(.\d{1,2})?(.\d{1,2})?(.\d{1,2})? .*')
        # 附录 正则表达式
        appendix = re.compile('附录\w*')
        for file in files:
            if self.debug:
                print(f'fileName: {file}')
            if os.path.isfile(path + '/' + file):
                if re.match(chapter, file):
                    print(f'章节: {file}')
                    match = re.match(chapter, file)
                    filename = file[match.span()[1]:len(file)]
                    os.rename(path + '/' + file, path + '/' + '01-{}'.format(filename.strip()))
                    index += 1
                elif re.match(appendix, file):
                    if self.debug:
                        print(f'附录：{file}')
                    match = re.match(appendix, file)
                    filename = file[match.span()[1]:len(file)]
                    os.rename(path + '/' + file, path + '/' + '01-{}'.format(filename.strip()))
                    index += 1
                elif re.match(subsection, file):
                    if self.debug:
                        print(f'file: {file}')
                    mdFiles.append(file)

        self.__bubbleSort(mdFiles)

        for file in mdFiles:
            if self.debug:
                print(f'rename file: {file}')
            subsection = re.compile('\w{1,2}(.\d{1,2})?(.\d{1,2})?(.\d{1,2})?')
            match = re.match(subsection, file)
            fileName = file[match.span()[1]:len(file)].strip()
            prefix = str(index) if index >= 10 else '0{}'.format(index)
            os.rename(path + '/' + file, path + '/' + '{}-{}'.format(prefix, fileName))
            index += 1
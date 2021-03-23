from replace_image import ReplaceImage
from rename import Rename
from correct_code_type import CorrectCodeLanguage

path = "./"
rn = Rename(path)
rn.rename()
ri = ReplaceImage(path)
ri.replace_image()
ccl = CorrectCodeLanguage(path, 'css', 'c')
ccl.correct()
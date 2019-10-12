# coding utf-8

"""
你需要设计一个能提供下面两个函数的文件系统：

create(path, value): 创建一个新的路径，并尽可能将值 value 与路径 path 关联，然后返回 True。
如果路径已经存在或者路径的父路径不存在，则返回 False。
get(path): 返回与路径关联的值。如果路径不存在，则返回 -1。
“路径” 是由一个或多个符合下述格式的字符串连接起来形成的：在 / 后跟着一个或多个小写英文字母。

例如 /leetcode 和 /leetcode/problems 都是有效的路径

{
    'leet':{
        val: 1,
        children:{
        code:{
            val: 2
            children:{
            }
        }
        }
   }
}



"""

from typing import List
class FileSystem:
    def __init__(self):
        self.val = None
        self.children = {}
    
    def _create(self, comps:List[str], value:int) -> bool:
        parent = comps[0]
        fs = self.children.get(parent)
        if len(comps) == 1: # top file level
            if fs: 
                return False # existed
            else:
                sub_fs = FileSystem()
                sub_fs.val = value
                self.children[parent] = sub_fs
                return True
        else:
            if not fs:
                return False # parent file path not existed
            return fs._create(comps[1:], value)

        
    def create(self, path:str, value:int) -> bool:
        comps = path.split('/')[1:]
        return self._create(comps, value)

    def get(self, path:str) -> int:
        comps = path.split('/')[1:]
        parent_fs = self
        for i, comp in enumerate(comps):
            sub_fs = parent_fs.children.get(comp)
            if not sub_fs:
                return -1
            parent_fs = sub_fs
        return parent_fs.val



        
        
def test():
    fs1 = FileSystem()
    assert fs1.create('/a', 1)
    assert fs1.get('/a') == 1

    fs2 = FileSystem()
    assert fs2.create('/leet', 1)
    assert fs2.create('/leet/code', 2)
    assert fs2.create('/leet/test', 3)
    assert fs2.get('/leet/code') == 2
    assert not  fs2.create('/leet', 1)
    assert fs2.get('/leet/test') == 3
    
    
'''节点管理模块主类
'''

import modelNode


class NodeManager(object):
    def __init__(self):
        print("Load NodeManager module...")
        self.node = modelNode.Node()

    def init_db(self):
        '''
        初始化数据库
        '''
        modelNode.Base.metadata.create_all(modelNode.Engine)

    def drop_db(self):
        '''
        删除所有数据表
        '''
        modelNode.Base.metadata.drop_all(modelNode.Engine)

    def show_all_node(self):
        '''
        获取所有的node信息
        '''
        all_node = self.node.search_all_node()
        return all_node

    def add_node(self, name, ip):
        '''
        添加一个节点
        '''
        self.node.add_node(name, ip)

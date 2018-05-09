'''
节点类
'''

import hashlib
import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # 创建对象的基类
Engine = create_engine('sqlite:///Node.db', encoding='utf-8')
Session = sessionmaker(bind=Engine)
session = Session()


class Node(Base):
    __tablename__ = 'node'

    index = Column(Integer, primary_key=True)  # 节点序号，自增
    passcode = Column(String(32))  # 使用md5生成唯一验证码
    name = Column(String(64))  # 节点自定义名称
    ip = Column(String(15))  # 节点ip
    update_time = Column(String(64))  # 节点更新时间

    def generate_passcode(self, name, update_time):
        '''
        根据传输的name和update_time计算md5值
        '''
        hash = hashlib.md5()
        hash.update(name.encode("utf8"))
        hash.update(update_time.encode("utf8"))
        passcode = hash.hexdigest()
        print("Test: generated passcode = ", passcode)
        return passcode

    def generate_update_time(self):
        '''
        根据当前时间生成updatetime字符串
        '''
        update_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print("Test: generated update_time = ", update_time)
        return update_time

    def add_node(self, name, ip):
        '''
        添加一个节点信息到数据库中
        '''
        self.name = name
        self.ip = ip
        self.update_time = self.generate_update_time()
        self.passcode = self.generate_passcode(self.name, self.update_time)
        session.add(self)
        session.commit()

    def update_node(self):
        '''
        更新节点信息
        以后再写，一般只更新name和ip
        '''
        pass

    def delete_node(self):
        '''
        删除节点信息
        '''
        pass

    def search_all_node(self):
        '''
        查询并返回全部节点信息
        返回值：[Node]
        '''
        result = session.query(Node).all()
        print("Test: result = ", result)
        print("Test: result[0].passcode = ", result[0].passcode)
        return result

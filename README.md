# 毕业设计：分布式渲染管理系统
实际名称：分布式集群渲染管理系统的构建与优化

### 源码说明
- .gitignore
    - __pycache__ 运行临时文件，python自带
    - .vscode vscode配置文件
    - upload 上传文件存储路径
    - download 下载文件存储路径
    - venv python虚拟环境目录
    - server.db 服务器端数据库
- 路径
    - doc 一些文档文件
    - docker dockerfile文件，requirements.txt文件
    - static flask的静态资源文件
    - templates flask的前端资源文件
- 入口文件
    - test.py 测试环境的入口文件
    - server.py 服务器端启动文件
    - node.py 节点端启动文件
    - client.py 客户端启动文件
    - init_db.py 服务器端初始化数据库

### 流程
- git clone https://github.com/fkworld/my_graduation_project.git
- cmd下进入所在目录
- python -m venv venv
- venv\Scripts\activate
- (venv) pip install -r docker\requirements.txt
- (venv) mkdir database
- (venv) python server_start.py
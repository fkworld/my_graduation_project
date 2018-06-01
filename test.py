import NodeSourceManager

def main():
    s = NodeSourceManager.NodeSourceManager()
    s.init_blender_path()
    s.run_blender("untitled.blend")


if __name__ == '__main__':
    main()

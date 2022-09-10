"""
    本项目被托管在 https://github.com/umeiko/XMU_Reporter 
    GPL-3.0 开源许可
"""
import code_editor
import sys

def main():
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        code_editor.open_file(fname)
    else:
        code_editor.main()

if __name__ == "__main__":
    main()
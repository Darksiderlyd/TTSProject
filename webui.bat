@echo off
chcp 65001

call venv\python.exe web_ui.py

@echo 启动完毕，请按任意键关闭
call pause
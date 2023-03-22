""" import importlib
importlib.import_module('.some_main_script','MyMainPackage').report_main()

importlib.import_module('.mysubscript','MyMainPackage.SubPackage').sub_report() """


from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()
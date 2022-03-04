
# import subprocess
# import sys
# import re
 
# def run(cmd):
#     proc = subprocess.Popen(cmd,
#         stdout = subprocess.PIPE,
#         stderr = subprocess.PIPE,
#     )
#     stdout, stderr = proc.communicate()
 
#     return proc.returncode, stdout, stderr
 
# code, out, err = run(['python3', 'test/test_add.py', 'TestCalcAdd.test_add_pos'])
# # x = re.search("^\nRan.*test$", error.decode('utf-8'))
# print("out: '{}'".format(out))
# print("err: '{}'".format(err))
# print("exit: {}".format(code))
# print(x)

x = 1
print ("Yes" if x==1 else "No")
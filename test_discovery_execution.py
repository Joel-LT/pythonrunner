import os, fnmatch
import sys, inspect
import hashlib
import json
import importlib
import time
import subprocess
from subprocess import call
test_dir = 'tests'
test_discovery = { 
    "testCases" : {},
    "testSuites": {}
}
test_execution = {
    "testCases" : {},
    "testSuites" : {}
}
test_discovery_json = ""
test_execution_json = ""

allfiles = fnmatch.filter(os.listdir(test_dir), 'test_*.py')

class CallPy(object):  #for calling other files
    def __init__(self, path):
        self.path=path
    
    def call_python_file(self):
        start_time = time.time()
        call(self.path)
        total_time = (time.time() - start_time)
        return total_time 

def getHash(file): #evaluates hash of a python file
    return hashlib.sha256(str(file).encode('utf-8')).hexdigest()

def get_locator(module):
    locator_list = []
    for class_name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            for func_name, func_obj in inspect.getmembers(obj):
                if inspect.isfunction(func_obj):
                    if (func_name.startswith('test_')):
                        locator_file = '.'.join([class_name, func_name])
                        locator_suite = class_name
                        locator_list.append([locator_file,locator_suite])
    return locator_list

def run_case(path):
    c = CallPy(path)
    return c.call_python_file()

def get_logs(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

testCasesDisc = []
testSuitesDisc = []
testCasesExec = []
testSuitesExec = []
testSuiteMap = {}


def test_discovery_function():
    for index in range(allfiles.__len__()):
        currfile = allfiles[index]
        module = importlib.import_module('tests.'+currfile.replace('.py',''))
        locator_list = get_locator(module)
        for locator in locator_list:
            func_path = ' '.join([os.path.join(test_dir,currfile), locator[0]])
            suite_path = ' '.join([os.path.join(test_dir,currfile), locator[1]])
            file = {
                "id": getHash(func_path),
                "label": func_path,
                "file": os.path.join(test_dir,currfile),
                "test-suites": suite_path
            }
            suite = {
                "id": getHash(suite_path),
                "label": suite_path,
                "file": os.path.join(test_dir,currfile)
            }
            if testSuiteMap.get(suite['id']) == None:
                testSuiteMap[suite['id']] = 1
                testSuitesDisc.append(suite)
            else:
                testSuiteMap[suite['id']] = testSuiteMap.get(suite['id']) + 1
            testCasesDisc.append(file)
        # run_case(os.path.join(test_dir,currfile))

    test_discovery["testCases"] = testCasesDisc
    test_discovery["testSuites"] = testSuitesDisc
    # print(test_discovery_json)
    return test_discovery

def test_execution_function():
    for testCase in test_discovery['testCases']: # for test Cases
        execute = ['python3'] + testCase['label'].split()
        exit_code, output, logs = get_logs(execute)
        time_taken = run_case(execute)
        file = {
                "id": testCase['id'],
                "label": testCase['label'],
                "file": testCase['file'],
                "status": "passed" if exit_code==0 else "failed",
                "duration": time_taken,
                "failureMsg": logs.decode('utf-8') if exit_code==1 else "NA"
            }
        testCasesExec.append(file)
    test_execution["testCases"]=testCasesExec

    for testSuite in test_discovery['testSuites']: # for test Suites
        execute = ['python3'] + testSuite['label'].split()
        exit_code, output, logs = get_logs(execute)
        time_taken = run_case(execute)
        file = {
                "id": testSuite['id'],
                "label": testSuite['label'],
                "file": testSuite['file'],
                "status": "passed" if exit_code==0 else "failed",
                "duration": time_taken,
                "numTests": testSuiteMap.get(testSuite['id']),
                "failureMsg": logs.decode('utf-8') if exit_code==1 else "NA"
            }
        testSuitesExec.append(file)
    test_execution["testSuites"]=testSuitesExec
    

if __name__ == "__main__":
    test_discovery_function()
    test_discovery_json = json.dumps(test_discovery, indent=2)
    print(test_discovery_json) # Final test discovery json
    test_execution_function()
    test_execution_json = json.dumps(test_execution, indent=2)
    print(test_execution_json) # final test execution json
import sys, inspect, re
from os.path import basename, split
## import /nbdoctest.py ## see below

__all__ = ['this_tests']

def this_tests(testedapi):
     RegisterTestsperAPI.this_tests(testedapi)

def full_name_with_qualname(klass):
     return f'{klass.__module__}.{klass.__qualname__}' 

def set_default(obj):
     if isinstance(obj, set):
          return list(obj)
     raise TypeError 

## TO DO: next two functions should go out and get imported from /nbdoctest.py#L92
def get_parent_func(lineno, lines):
    for idx,l in enumerate(reversed(lines[:lineno])):
        if re.match(f'^def test', l):
            return (lineno - (idx+1)), l
    return None

def get_lines(file):
    with open(file, 'r') as f:
          return f.readlines()

class RegisterTestsperAPI:
    apiTestsMap = dict()
    @staticmethod
    def this_tests(testedapi):
        previous_frame = inspect.currentframe().f_back.f_back 
        (pathfilename, line_number, test_function_name, lines, index) = inspect.getframeinfo(previous_frame)
## TO DO: these prints go out later
        print('\n\n\n\n###############################################################')
        print('\n\n############ previous_frame: filename =' + basename(pathfilename))
        print('\n############ previous_frame: line_number =' + str(line_number))
        print('\n############ previous_frame: test_function_name =' + test_function_name)
        print('\n############ previous_frame: lines =' + str(lines))
        print('\n############ previous_frame: index =' + str(index))
 
        
        ###
        lineno_parentfunc, parent_func = get_parent_func(line_number, get_lines(pathfilename)) 

        print('\n############ previous_frame: parent_func =' + str(parent_func))
        print('\n############ previous_frame: lineno_parentfunc =' + str(lineno_parentfunc))

        print('###############################################################\n\n\n\n')    
        ###

        list_test = [{'file': basename(pathfilename), 'test': test_function_name , 'line': str(lineno_parentfunc)}]

        #list_test = [{'file: '+ basename(pathfilename), 'test: ' + test_function_name , 'line: ' + str(lineno_parentfunc)}]
        print('\n############ list_test =' + str(list_test))
        fq_apiname = full_name_with_qualname(testedapi)
        print('\n############ fq_apiname =' + str(fq_apiname))
        if(fq_apiname in RegisterTestsperAPI.apiTestsMap):
            RegisterTestsperAPI.apiTestsMap[fq_apiname] = RegisterTestsperAPI.apiTestsMap[fq_apiname]  + list_test
        else:
            RegisterTestsperAPI.apiTestsMap[fq_apiname] =  list_test   
        print('\n############ RegisterTestsperAPI.apiTestsMap[fq_apiname] =' + str(RegisterTestsperAPI.apiTestsMap[fq_apiname]))

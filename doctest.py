import pytest, sys, re, json, inspect
from os.path import abspath, dirname
from utils.mem import use_gpu

__all__ = ['this_tests']

def this_tests(testedapi):
     RegisterTestsperAPI.this_tests(testedapi)

def full_name_with_qualname(klass):
     return f'{klass.__module__}.{klass.__qualname__}' ##  __name__ for of qualname for short version

def set_default(obj):
     if isinstance(obj, set):
          return list(obj)
     raise TypeError 

class RegisterTestsperAPI:
    apiTestsMap = dict()
    @staticmethod
    def this_tests(testedapi):
        
        print('\n\n\n\n###############################################################')

        previous_frame = inspect.currentframe().f_back.f_back ##.f_back 
        (filename, line_number, test_function_name, lines, index) = inspect.getframeinfo(previous_frame)
        list_test = [{'file: '+ filename, 'test: ' + test_function_name}]
        print('\n\n############ previous_frame: filename =' + filename)
        print('\n############ previous_frame: line_number =' + str(line_number))
        print('\n############ previous_frame: test_function_name =' + test_function_name)
        print('\n############ previous_frame: lines =' + str(lines))
        print('\n############ previous_frame: index =' + str(index))
       
        print('###############################################################\n\n\n\n')     
        fq_apiname = full_name_with_qualname(testedapi)
        if(fq_apiname in RegisterTestsperAPI.apiTestsMap):
            RegisterTestsperAPI.apiTestsMap[fq_apiname] = RegisterTestsperAPI.apiTestsMap[fq_apiname]  + list_test
        else:
            RegisterTestsperAPI.apiTestsMap[fq_apiname] =  list_test   
        
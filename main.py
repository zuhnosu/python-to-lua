# 19.07.2022

import random 

# LUA TO PYTHON
# USE MY CUSTOM LUA LIBRARY TO MAKE IT FULLY WORK

class table:
    def insert(tbl, element):
        tbl.append(element)
    def remove(tbl, element):
        tbl.remove(element)

class math:
    def random(min, max):
        return random.randint(min, max)

class string:
    def sub(inputstr, start, end):
        end += 1
        return inputstr[start:end]
    def gsub(inputstr, replace, value):
        return inputstr.replace(replace, value)
    def find(inputstr, pattern):
        return inputstr.find(pattern)
    def match(inputstr, pattern):
        return string.find(inputstr, pattern)
    def gmatch(inputstr, pattern):
        return string.find(inputstr, pattern)
    def split(inputstr, seperator):
        return inputstr.split(seperator)
    def upper(inputstr):
        return inputstr.upper()
    def lower(inputstr):
        return inputstr.lower() 

# MAIN "PARSER"

a = '''
local nigga = 'test'
local nigga2 = [[
    test
]]
if nigga == true then 
    nigga = false
    if nigga == false then 
        print('test)
    end
end 
'''

a = a.replace('local ', '')
a = a.replace('true', 'True')
a = a.replace('false', 'False')
a = a.replace('then', '):')
a = a.replace('if', 'if (')
a = a.replace('end', '')
a = a.replace('and', '&')
a = a.replace('[[', '"""')
a = a.replace(']]', '"""')
a = a.replace('{', '[')
a = a.replace('}', ']')
a = a.replace('--', '#')

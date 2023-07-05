from extraction.height import *
from extraction.size import *
from extraction.diameter import *
from extraction.largest_level import *
def start_analysis(root):
    print('\n\n')
    
    print('analysis starts')
    print('size is ',size(root))
    print('height is ',h(root))
    print('diameter',diameter(root))
    print('largest level ')
    largest_level(root)
    print()
    print('analysis over')
    print()
    print()
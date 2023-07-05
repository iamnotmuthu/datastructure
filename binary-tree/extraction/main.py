from extraction.height import *
from extraction.size import *
from extraction.diameter import *
from extraction.largest_level import *
from extraction.lowest_com_ancestor import *
def start_analysis(root):
    print('\n\n')
    
    print('analysis starts')
    print('size is ',size(root))
    print('height is ',h(root))
    print('diameter',diameter(root))
    print('largest level ')
    largest_level(root)
    print()
    print('lowest parent',lowest_anc(root,5,7))
    print('analysis over')
    print()
    print()
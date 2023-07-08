from extraction.height import *
from extraction.size import *
from extraction.diameter import *
from extraction.largest_level import *
from extraction.lowest_com_ancestor import *
from extraction.kthlevelnodes import *
from extraction.maxpathsum import *
from extraction.topview import *
from extraction.leftview import *
from extraction.rightview import *

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
    print('kth level')
    kthlevel(root,1,0)
    print()
    print('maxpathsum',maxpathsum(root))
    print('top view')
    topview(root)
    print()
    print('top viw over')
    print('left view')
    leftview(root)
    print()
    print('right view')
    rightview(root)
    print()
    print('analysis over')
    print()
    print()

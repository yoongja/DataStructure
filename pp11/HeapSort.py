
def reheap_down(elements, root, bottom):
    leftChild = root*2+1
    rightChild = root*2+2
    maxChild=0
    if leftChild<=bottom:
        if leftChild == bottom:
            maxChild = leftChild
        else:
            if elements[leftChild] <=elements[rightChild]:
                maxChild=rightChild
            else:
                maxChild = leftChild
        if elements[root]<elements[maxChild]:
            elements[root],elements[maxChild]=elements[root],elements[ maxChild]
            reheap_down(elements,maxChild,bottom)

def heap_sort(values, numValues):

    '''[3]'''

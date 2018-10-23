'''Q4: Write a function that combines two lists by alternatingly taking elements, e.g.
[a,b,c], [1,2,3] → [a,1,b,2,c,3].
[1,2,5,8,0], [9,4,8,7,6] → [1, 9, 2, 4, 5, 8, 8, 7, 0, 6].'''

def merge(array1,array2):
    array3=[]
    for item1,item2 in zip(array1,array2): #for inserting values of two list
        array3.append(item1)
        array3.append(item2)
    return array3

if __name__ == '__main__':
    array1=['a','b','c','d']
    array2=[1,2,3,4]
    array3=merge(array1,array2)
    print(array3)
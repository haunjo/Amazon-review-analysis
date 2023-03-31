from circularDoublyLinkedList import *
import pandas as pd

def load_data(dataset : CircularDoublyLinkedList):
    with open('amazon_shoes_100kreviews.tsv', 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            if len(fields) == 15:
                dataset.append(fields)
        ##insert data into list
        

def get_data(dataset : CircularDoublyLinkedList):
    filtered = list(dataset.filter(CircularDoublyLinkedListFilter(dataset)))
    i = 0
    df = pd.DataFrame(filtered)
    print(df.head())
        
    
if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    dataset.pop(0)
    # for i in range(0,10):
    #     print(dataset.get(i))
    get_data(dataset)
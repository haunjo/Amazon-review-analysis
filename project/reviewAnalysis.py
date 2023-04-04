from src.circularDoublyLinkedList import *
import pandas as pd
from collections import Counter

def load_data(dataset : CircularDoublyLinkedList):
    with open('amazon_shoes_100kreviews.tsv', 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            if len(fields) == 15:
                dataset.append(fields)
        ##insert data into list
        

def get_data(dataset : CircularDoublyLinkedList):
    filtered = dataset.filter(CircularDoublyLinkedListFilter(dataset))
    print(filtered.head())
    return filtered
    
def analyze_data(df):
    print("-------- TOP 30 Hottest purchases on Spring season 2015 --------")
    cnt = df.value_counts('product_title')
    print(cnt)
    result = pd.DataFrame({"product_title": cnt.index, "review_cnt" : cnt.values})
    print(result[:30])
if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    dataset.pop(0)
    data = get_data(dataset)
    print('\n');print('\n');print('\n')
    analyze_data(data)
# to read csv file
import csv
import pandas as pd
class Test_CRUD(object):

    def test_update_1(self):
        with open('test_automation/26072024/testdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print (row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('test_automation/26072024/testdata.csv')
        print(df)

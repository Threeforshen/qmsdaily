import pandas as pd

# number= int( input("请输入列数："))
#
# df=pd.read_csv(path,usecols=[0,1,number])
# print(df)
#
# print('----------------')
def opendata(path,number):
	df=pd.read_csv(path,usecols=[0,1,number])

	print(df)

if __name__=='__main__':
    path = r'D:/completed.csv'
    number=int(input('请输入列数：'))
    opendata(path,number)
    i=input('看完了吗？')
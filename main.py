# import libraries ต่างๆ ที่จำเป็น
import pandas as pd
from sklearn.cluster import KMeans

# read mall customer data
df = pd.read_csv("mall_200customers.csv",sep=",")
print(df)
def train_model(df):


     # เลือกเฉพาะ feature 'Age'  และ  'Spending Score (1-100)' ดูก่อน
     X1 = df[['Age' ,'Annual Income (k$)', 'Spending Score (1-100)']].copy()

     Model1 = (KMeans(n_clusters = 3 ,max_iter=300,  random_state= 111))

     # ใช้คำสั่ง .fit() เพื่อเทรนโมเดล
     Model1.fit(X1)
     return (predict_model)
def predict_model():
    df = pd.read_csv("mall_200customers.csv", sep=",")
    print(df)
    # เรียกใช้ เมธอด
    model1 = train_model(df)
    #สร้างข้อมูล testuser
    x_test = ['Age','Annual','Spending']
    pd.DataFrame([x_test],columns=['Age' ,'Annual Income (k$)', 'Spending Score (1-100)'])
    # ทำนายโมเดล
    result = model1.predict(x_test)
    print(result)
    if result==0:
        print()
        return
    elif result==1:
        print()
        return
    else:
        print()
        return
predict_model (20,50,10)

train_model(df)
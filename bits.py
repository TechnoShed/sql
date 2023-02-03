
import pandas as pd
from sqlalchemy import create_engine



def copymysql( df,tablename ):
    mydb = create_engine("mysql+pymysql://root:TSD704153TSD@technoshed.duckdns.org/inspectionDB")
    try:
        frame = df.to_sql(tablename, mydb);
    except ValueError as vx:#
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("done");
        print("Table %s created successfully."%tablename);

    finally:
        print("ended")


print("load dataframe")

df = pd.read_excel("/media/bass/603D-E572/DEV/sql/files/newdata.xlsx", index_col=[0])
print(df)

print("\nCOpying to DB")

result = copymysql(df, "vehicles")

print("dondione DONEDONEoneoddnee")
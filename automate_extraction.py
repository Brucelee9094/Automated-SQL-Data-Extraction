import pandas as pd
import logging 
import pyodbc as pyb
import sys
import smtplib as em
from email.message import EmailMessage
from config import DB_CONFIG, EMAIL_CONFIG


Q1="Select * from ProductSales"

OUTPUT_CSV="extractedPrint.csv"

LOG_FILE="extractionLog.log"

#logging setup
import logging
import sys
def loggingSetup():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s-%(levelname)s-%(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE,mode='a'),
            logging.StreamHandler(sys.stdout)
        ],
        force=True
        
    )


#creating database Function

def get_db_Connection():
    try:
        conn=None
        if DB_CONFIG['DRIVER']=='sqllite3':
            import sqlite3
            conn = sqlite3.connect(DB_CONFIG['database'])
            logging.info("Successfully connected to SQLite database.")

        else:
            connect_Str=(
                f"DRIVER={DB_CONFIG['DRIVER']};"
                f"SERVER={DB_CONFIG['SERVER']};"
                f"DATABASE={DB_CONFIG['DATABASE']};"
            )
            if 'uid' in DB_CONFIG and 'pwd' in DB_CONFIG:
                connect_Str += f"UID={DB_CONFIG['uid']};PWD={DB_CONFIG['pwd']}"
            else:
                connect_Str =connect_Str + f"Trusted_Connection={DB_CONFIG['Trusted_Connection']}"

            conn=pyb.connect(connect_Str)
            logging.info(f"Successfully Connected to the DataBase {DB_CONFIG['SERVER']} \ {DB_CONFIG['SERVER']}")
    except Exception as e :
        logging.error(f"DataBase connection Failed :{e}",exc_info=True)
        raise
    return conn


# dataExtractiob function 
def data_extraction(Connection):
    df=None
    try:
        logging.info(f"Eecuing SQL Query :{Q1}")
        df=pd.read_sql_query(Q1,Connection)
        logging.info(f"Query Executed Successfully")
    except Exception as e:
        logging.error(f"Extraction Error Occurred:{e}",exc_info=True)
        raise
    return df
        
#DataExporting 

def dataExport(dataframe,filename):
    if dataframe is None or dataframe.empty:
        logging.warning("NO data to extract")
    try:
        dataframe.to_csv(filename,index=False,encoding='Utf-8')
        logging.info(f"Data extracted Successfully")  
    except Exception as e:
            logging.error(f"Data Extracion Failed :{e}",exc_info=True)
            raise  
#email function 
def send_email(subject,body):
    try:
        logging.info("Error message Started")
        msg=EmailMessage()
        msg['From']=EMAIL_CONFIG['SENDEREMAIL']
        msg['To']=EMAIL_CONFIG['RECEIVEREMAIL']
        msg['Subject']=subject
        msg.set_content(body)

        #connect to smtp erver 
        with em.SMTP(
            EMAIL_CONFIG['SMTPSERVER'],
            EMAIL_CONFIG['SMTPPORT']
        )as server:
            server.starttls()

            server.login(
                EMAIL_CONFIG['SENDEREMAIL'],
                EMAIL_CONFIG['SENDERPASSWORD']
            )

            server.send_message(msg)
        logging.info("Email notification sent Successfully")
        
    except Exception as e:
        logging.error(f"Message not sent:{e}",exc_info=True)
    raise        

# main 
def main():
    loggingSetup()
    logging.info("AUtomaticdata Extraction WorkFlow Started")
    con=None
    try:
        logging.info("trying to get DB Connction")
        con=get_db_Connection()
        if con:
            logging.info("DataBase Connection Succcessful")
            product_data=data_extraction(con)
            dataExport(product_data,OUTPUT_CSV)
            logging.info(f"Data Sucessfully xtracted to the {OUTPUT_CSV} file ")
    except Exception as e :
        logging.critical(f"eror occured in main function :{e}",exc_info=True)
        send_email(f"Data Extraction failed ",f"there is an error at :\n\n{e}")
    finally:
        if con:
            con.close()
            logging.info("DataBase Conection Closed !")

if __name__=="__main__":
    main()
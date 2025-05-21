import requests
from bs4 import BeautifulSoup
import mysql.connector

column_list=['Designer','Type',	'Year_Released','CPU_Function','Width_of_Machine_Word','Supported_Instruction_Sets','Type_of_processor_cores','Number_of_processor_cores','Memory_Interfaces','Max_Clock_Frequency_of_Memory_IF','Data_Bus_Width','Number_of_data_bus_channels','Max_Data_Rate','Non_volatile_Memory_Interface','Recommended_Maximum_Clock_Frequency','Feature_Size','Semiconductor_Technology','Fab','Embedded_GPU','GPU_Clock','Supported_Cellular_Data_Links','Data_Integrity','Added','Total_L2_Cache','Number_of_GPU_cores','Address_Bus_Width']
cookies = {
    '_ga': 'GA1.2.995458678.1746700102',
    '_gid': 'GA1.2.69579357.1746700102',
    'viewed_device': '.24599.',
    '_ga_3LYF7SMBX2': 'GS2.2.s1746700103$o1$g1$t1746702121$j60$l0$h0',
    '__gads': 'ID=98c5bd9b39f8984e:T=1746700102:RT=1746702121:S=ALNI_MbPtTBoZnsPRIO2kP0ElHyx5gdTog',
    '__gpi': 'UID=000010b93a09f44d:T=1746700102:RT=1746702121:S=ALNI_Maa8L9ZKB1wvGxubKEJTR2YCMesnw',
    '__eoi': 'ID=ac44b7886f45d54e:T=1746700102:RT=1746702121:S=AA-AfjaBsHiLZ2W3nosJVTsJZ2JO',
    'FCNEC': '%5B%5B%22AKsRol-TA4htL0GGhlru_yAPJu2woPmrItTe12gFEWXlcphawB6OEudURNyCi_f1skZLT5PWq7mOe__yyG7LBMZeHwZ-HlFOd4MgVFnjYYc6TFBU3KRC7zTogx0p6po7kW4l6_BKEDcZhFW-VtzbVQMNzkwRwvLCjQ%3D%3D%22%5D%5D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Referer': 'https://phonedb.net/index.php?m=device&s=list',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': '_ga=GA1.2.995458678.1746700102; _gid=GA1.2.69579357.1746700102; viewed_device=.24599.; _ga_3LYF7SMBX2=GS2.2.s1746700103$o1$g1$t1746702121$j60$l0$h0; __gads=ID=98c5bd9b39f8984e:T=1746700102:RT=1746702121:S=ALNI_MbPtTBoZnsPRIO2kP0ElHyx5gdTog; __gpi=UID=000010b93a09f44d:T=1746700102:RT=1746702121:S=ALNI_Maa8L9ZKB1wvGxubKEJTR2YCMesnw; __eoi=ID=ac44b7886f45d54e:T=1746700102:RT=1746702121:S=AA-AfjaBsHiLZ2W3nosJVTsJZ2JO; FCNEC=%5B%5B%22AKsRol-TA4htL0GGhlru_yAPJu2woPmrItTe12gFEWXlcphawB6OEudURNyCi_f1skZLT5PWq7mOe__yyG7LBMZeHwZ-HlFOd4MgVFnjYYc6TFBU3KRC7zTogx0p6po7kW4l6_BKEDcZhFW-VtzbVQMNzkwRwvLCjQ%3D%3D%22%5D%5D',
}

conn=mysql.connector.connect(
    host='192.168.1.9',
    user='root',
    password='mySQL1!',
    database='devicespecifications'
)

cursor=conn.cursor()

def join_and_filter(column):
    words=column.split(" ")
    new_word='_'.join(words)
    new_word=new_word.replace('//','_OR_').replace('.','').replace(':','').replace('-','_')
    new_word=new_word.replace('(','').replace(')','')
    return new_word


def get_from_database():
    # query='SELECT CPU_LINK FROM phonedb_data GROUP BY CPU_LINK'
    # cursor.execute(query)
    # rows=cursor.fetchall()
    # for row in rows[6:]:
    #     get_data(row[0])
    urls=['the website...not disclosing it here']
    for url in urls:
        get_data(url)


def insert_into_database(inner_list):
    column_str=','.join(column_list)
    placeholders=','.join(['%s']*len(column_list))
    query=f"insert into CPU_Details ({column_str}) values ({placeholders})"
    print(query)
    
    print(inner_list)
    # print("_________________________________________________________________________________________")
    cursor.execute(query,tuple(inner_list))
    conn.commit()

def add_col_to_database(column):
    query=f"alter table CPU_Details add column `{column}` text"
    cursor.execute(query)
    conn.commit()  




def add_column(column):
    if column not in column_list:
        column_list.append(join_and_filter(column))
        add_col_to_database(column)
        
        

def valid_column(column):
    if column not in column_list:
        
        return False
    else:
        return True


def list_the_data(my_dict):
    inner_list=[]
    for item in column_list:
        inner_list.append(my_dict.get(item,"NULL"))
    # print(inner_list)
    insert_into_database(inner_list)

def get_data(url):
    r=requests.get(url,cookies=cookies,headers=headers,verify=False)
    soup=BeautifulSoup(r.text,'html.parser')
    div=soup.find('div',class_='canvas')
    div=div.table
    trs=[]
    for tr in div.find_all('tr'):
        if not tr.find('td',colspan='2'):
            trs.append(tr)
                      
    my_dict={}
    for tr in trs:
        column=tr.find('td').text.strip()
        value=tr.find_all('td')[1].text.strip()
        # print(f"{column}--->{value}")
        if column =='Function':
            column='CPU_Function'
        column=join_and_filter(column)
        if not valid_column(column):
            add_column(column)
            
        value=value.replace('\n','')
        my_dict[column]=value
                
    # for item in my_dict.items():
    #     print(item)
    list_the_data(my_dict)
        
            
                                
                         
# url='https://phonedb.net/index.php?m=processor&id=962&c=qualcomm_snapdragon_7s_gen_2_5g_sm7435-ab'
# url='https://phonedb.net/index.php?m=processor&id=945&c=mediatek_dimensity_7020_mt6855'
# get_data(url)
get_from_database()

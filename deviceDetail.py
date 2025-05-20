import requests
from bs4 import BeautifulSoup
import mysql.connector

conn=mysql.connector.connect(
    host='192.168.1.9',
    user='root',
    password='mySQL1!',
    database='devicespecifications'
)

cursor=conn.cursor()
base_url='https://phonedb.net'

# column_list=['A','B','C','D']

# # function to see info of a particular page
# def content_info(seq,Page_link):
#     final_list=[]
#     response = requests.get(Page_link, params=params, cookies=cookies, headers=headers,verify=False)
#     soup=BeautifulSoup(response.text,'html.parser')
#     divs=soup.find_all('div',class_='content_block')
#     print(f"sequence number is:{seq}")
#     for div in divs:
#         inner_list=[]
#         my_dict={}
#         if div.text.strip():
#             # seq =int(seq)
#             seq +=1
#             content_block_title=div.find('div',class_='content_block_title')
#             anchor_tag=content_block_title.find('a')
#             link_text=anchor_tag.text
#             my_dict['A']=link_text
#             link=base_url+'/'+anchor_tag.get('href')
#             my_dict['B']=link
#             # print(link_text)
#             detail_anchor=div.find('a',title='See detailed datasheet')
#             detail_link=base_url+'/'+detail_anchor.get('href')
#             my_dict['C']=detail_link
#             # print(detail_link)
#             direct_text=div.find_all(string=True,recursive=False)
#             details=''.join(direct_text).strip()
#             text_content=details.replace('|','')
#             my_dict['D']=text_content
#             # print(text_content)
#         for item in column_list:
#             inner_list.append(my_dict.get(item,'NULL'))
#         final_list.append(tuple(inner_list))
#     query='INSERT INTO phoneDB(LINK_TEXT,LINK,DETAIL_LINK,TEXT_CONTENT) VALUES(%s,%s,%s,%s)'
#     cursor.executemany(query,final_list)
#     conn.commit()
#         # print("___________________________________________________________________________________________")
#     # print(final_list)
    
            
           
            
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

# params = {
#     'm': 'device',
#     's': 'list',
# }


              
# r=requests.get('https://phonedb.net/index.php',params=params, cookies=cookies, headers=headers,verify=False)
# soup=BeautifulSoup(r.text,'html.parser')

# # seq=input("enter the sequence number:")
# sequence1=0
# link_div=soup.find_all('div',class_='container')
# for link in link_div:
#     if "Device Specs Pages:" in link.text:
#         a_tags=link.find_all('a')
#         for a in a_tags[:166]:
#             if "Jump to page" in a.get('title'):
#                 sequence1 +=1
#                 # sequence1=a.text.split("-")[0]
#                 # sequence2=a.text.split("-")[1]
#                 # if int(seq) >= int(sequence1) and int(seq)<=int(sequence2):
#                 #     sequence_link=a.get('href')
#                 #     # print(f"{sequence}:{base_url+sequence_link}")
#                 #     full_url=base_url+''+sequence_link
#                 #     final_list.append(content_info(sequence1,full_url))
#                 # else:
#                 #     continue
#                 sequence_link=a.get('href')
#                 full_url=base_url+''+sequence_link
#                 content_info(sequence1,full_url)





column_list=['Brand','Model','Device Category','Operating System','CPU Clock','CPU','CPU_LINK','RAM Type','RAM Capacity','Non-volatile Memory Capacity','Display Diagonal','Resolution','Pixel Density','Display Refresh Rate','Graphical Controller','GPU Clock:','USB','Bluetooth','Market Countries','Market Regions','Added']
final_list=[]
def listing_data(my_dict):
    inner_list=[]
    for item in column_list:
        inner_list.append(my_dict.get(item,'NULL'))  
    final_list.append(tuple(inner_list))
        

def valid_column(column):
    if column.strip() in column_list:
        return True
    return False
   
def find_link(td_tag):
    a=td_tag.find_all('a') 
    link=base_url+'/'+a[1].get('href') 
    return link     



# url='https://phonedb.net/index.php?m=device&id=23902&c=sharp_aquos_sense_9_5g_td-lte_id_sh-m29id_256gb__sharp_naze&d=detailed_specs'
def Page_detail(url):
    r=requests.get(url, cookies=cookies, headers=headers,verify=False)
    soup=BeautifulSoup(r.text,'html.parser')
    div=soup.find('div',class_='canvas')
    # print(div.text.strip())
    div=div.table
    trs=[]
    for tr in div.find_all('tr'):
        if not tr.find('td',colspan='2'):
            trs.append(tr)
                        
    data_link_column=['CPU']

    my_dict={}
    i=1
    for tr in trs:
        col=tr.find('td').text
        if valid_column(col) or tr.find('td').text =='':
            column=tr.find('td').text.strip()      
            value=tr.find_all('td')[1].get_text(strip=True)        
            if column =='Device Category':  #if the details are of not smartphone 
                if value !='Smartphone': 
                    return 
                else:
                    my_dict[column]=value          
            elif column == '':
                prev_col=tr.find_previous_sibling().find('td').text.strip()
                prev_col_dict=list(my_dict.keys())[-1]
                if prev_col == prev_col_dict:
                    last_key=list(my_dict.keys())[-1]
                    if prev_col !='Display Diagonal':
                        prev_value=my_dict[last_key]
                        value=prev_value+','+value  
                    my_dict[last_key]=value  
            elif column in data_link_column:
                link=find_link(tr.find_all('td')[1])
                my_dict[column]=value
                column=column+"_LINK"
                my_dict[column]=link
            else:
                my_dict[column]=value
    
    listing_data(my_dict)

def insert_into_database(final_list):
    query='insert into phonedb_data(Brand,Model,Device_Category,Operating_System,CPU_Clock,CPU,CPU_LINK,RAM_Type,RAM_Capacity,Non_volatile_Memory_Capacity,Display_Diagonal,Resolution,Pixel_Density,Display_Refresh_Rate,Graphical_Controller,GPU_Clock,USB,Bluetooth,Market_Countries,Market_Regions,Added) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.executemany(query,final_list)
    conn.commit()
    cursor.close()
    conn.close()


# cursor.execute('select DETAIL_LINK from phonedb')
# rows=cursor.fetchall()
# i=1
# for row in rows[401:501]:
#     print(i)
#     i+=1
#     if row[0] !='NULL':
#         print(row[0])
#         Page_detail(row[0])
# print(final_list)
# insert_into_database(final_list)
# cursor.close()
# conn.close()

urls=['https://phonedb.net/index.php?m=device&id=23546&c=nothing_cmf_phone_1_5g_premium_edition_global_dual_sim_td-lte_256gb_a015__nothing_tetris&d=detailed_specs','https://phonedb.net/index.php?m=device&id=23545&c=nothing_cmf_phone_1_5g_premium_edition_global_dual_sim_td-lte_128gb_a015__nothing_tetris&d=detailed_specs','https://phonedb.net/index.php?m=device&id=23544&c=nothing_cmf_phone_1_5g_standard_edition_global_dual_sim_td-lte_128gb_a015__nothing_tetris&d=detailed_specs']
for url in urls:
    # print(url)
    Page_detail(url)

print(final_list)
insert_into_database(final_list)
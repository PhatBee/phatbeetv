import requests
import xml.etree.ElementTree as ET
from io import BytesIO
import gzip

# Danh sách URL EPG của bạn
urls = [
   'http://lichphatsong.site/schedule/epg.xml',
   'https://tvbvn.quanlehong539.workers.dev/xml',
    # 'https://vnepg.site/epg.xml',
    # 'https://live.qphim.xyz/epg.xml',
    # 'http://onnaonlinetv.xyz/epg.xml',
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400477', #TNT Sports 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400480', #TNT Sports 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400479', #TNT Sports 3
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400478', #TNT Sports 4
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=219100', #Premier Sports 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=219104', #Premier Sports 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=465355', #Fox Sports 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369719', #Rock Entertainment
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=517640', #Rock Action
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=4196', #Love Nature
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=2580', #Bein Sports 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=4146', #Bein Sports 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=3118', #Bein Sports 3
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=496586', #Bein Sports 4
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369840', #HBO Hits
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369786', #HBO Family
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369758', #HBO Singature
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=444724', #Eurosports 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=444725', #Eurosports 2



]

# Tạo root element <tv>
tv = ET.Element('tv')

# Tải và merge từng nguồn
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        if url.endswith('.gz'):
            with gzip.open(BytesIO(response.content), 'rt', encoding='utf-8') as f:
                tree = ET.parse(f)
        else:
            tree = ET.parse(BytesIO(response.content))
        root = tree.getroot()
        # Thêm tất cả <channel> và <programme> từ nguồn này
        for elem in root:
            tv.append(elem)
    else:
        print(f"Error fetching {url}: {response.status_code}")

# Lưu file merged
tree = ET.ElementTree(tv)
tree.write('merged_epg.xml', encoding='utf-8', xml_declaration=True)
print("Merged EPG saved to merged_epg.xml")

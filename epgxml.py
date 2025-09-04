import requests
import xml.etree.ElementTree as ET
from io import BytesIO
import gzip

# Danh sách URL EPG của bạn
urls = [
   # 'https://lichphatsong.xyz/schedule/epg.xml.gz',
    'https://vnepg.site/epg.xml',
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369848', #Animax
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=9396', #BabyTV
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=448553',
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=54963', #FR:beIN SPORTS 3
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=55773', #FR:beIN SPORTS 1
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=450289', #Sky Sports Football
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=12453', #SkySp PL
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=212145', #SkySp Tennis
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=430092', #FR: Canal+ Foot
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=381881', #SkySp+
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=403788', #Disney - Eastern
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=403576', #Boomerang - US
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400477', #TNT Sports 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400480', #TNT Sports 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400479', #TNT Sports 3
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=400478', #TNT Sports 4
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369822', #Hub Premier 2
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=369784', #Hub Premier 1
   'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=219100', #Premier Sports 1
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

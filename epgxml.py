import requests
import xml.etree.ElementTree as ET
from io import BytesIO
import gzip

# Danh sách URL EPG của bạn
urls = [
    # 'https://lichphatsong.xyz/schedule/epg.xml.gz',
    'https://vnepg.site/epg.xml',
    'https://lichphatsong.xyz/schedule/detail?id=dmax',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=369848',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=9396',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=448553',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=54963',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=55773',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=450289',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=12453',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=212145',
    'https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9Ib19DaGlfTWluaA%3D%3D&channel_id=430092',
    'https://epg.pw/api/epg.xml?lang=en&channel_id=381881'
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

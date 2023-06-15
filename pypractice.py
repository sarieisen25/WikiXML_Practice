import xml.etree.ElementTree as ET
# tree = ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', ('start', 'end'))
with open('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', 'rt') as f:
    tree = ET.parse(f)
    root = tree.getroot()

# for node in tree.iter():
#     t = node.tag
#     print(t.replace('{http://www.mediawiki.org/xml/export-0.10/}', ''))

# page_count = 0
# for node in tree.findall('.//sha1'):
#     page_count += 1
# print (str(page_count)+' pages')

# for page in root:
#     t = page.attrib.get('title')
#     id = page.attrib.get('id')
#     if t != None:
#         print(str(t)+', id: '+str(id))

# for page in root:
#     for child in page:
#         if child.tag == 'title':
#             print('Title: '+child.attrib.get('title'))

# for (event, node) in ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', ('start', 'end')):
#     if node.attrib.get('title') != 'None ':
#         print(node.attrib.get('id'))

for page in root.iter():
    print (page.attrib)

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docs']
print(list(filter(lambda x: x.endswith('.jpg') or x.endswith('.png'), files)))
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

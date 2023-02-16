import sys

for line in sys.stdin:
    items = []
    for item in line.split(','):
        if item[0].isdigit():
            item = 'Q' + item

        item = item.replace('-', '_')

        items.append(item)

    print(','.join(items))

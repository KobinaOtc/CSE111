# Define Main

def main():
    province_list = make_provinces('provinces.txt')
    province_list.pop(0)
    province_list.pop()
    print(province_list)
    alberta_count = 0
    for province in province_list:
        if province == 'Alberta':
            alberta_count += 1
    print(f'Alberta occurs {alberta_count} times in the modified list.')

def make_provinces(filename):
    provinces = []
    with open(filename, 'rt') as text_file:
        for item in text_file:
            clean_item = item.strip()
            if clean_item == 'AB':
                provinces.append('Alberta')
            else:
                provinces.append(clean_item)
    return provinces

if '__main__' == __name__:
    main()
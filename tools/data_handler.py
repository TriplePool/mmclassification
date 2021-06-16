import csv


def csv_to_txt(input_fp, output_fp):
    with open(input_fp, encoding='utf-8') as f:
        opt_str = ''
        for i, row in enumerate(csv.reader(f)):
            if i == 0: continue
            if not len(row[1]) * len(row[2]):
                print(row[0], row[1])
                continue
            fn, clsid = row[1], int(row[2])
            if clsid < 0: continue
            opt_str += '{} {}\n'.format(fn, clsid)
        with open(output_fp, 'w', encoding='utf-8') as opt_f:
            opt_f.write(opt_str)


if __name__ == '__main__':
    ipt_fp = '/home/wbl/workspace/data/raster_data.csv'
    opt_fp = '/home/wbl/workspace/data/raster_data.txt'
    csv_to_txt(ipt_fp, opt_fp)

import csv
import os
import random


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


def csv_to_txt_split_class(input_fp, output_fp):
    with open(input_fp, encoding='utf-8') as f:
        opt_str_0 = ''
        opt_str_1 = ''
        opt_str_2 = ''
        count_0, count_1, count_2 = 0, 0, 0
        for i, row in enumerate(csv.reader(f)):
            if i == 0: continue
            if not len(row[1]) * len(row[2]):
                print(row[0], row[1])
                continue
            fn, clsid = row[1], int(row[2])
            if clsid < 0: continue
            if clsid == 0:
                opt_str_0 += '{} {}\n'.format(fn, clsid)
                count_0 += 1
            elif clsid == 1:
                opt_str_1 += '{} {}\n'.format(fn, clsid)
                count_1 += 1
            else:
                opt_str_2 += '{} {}\n'.format(fn, clsid)
                count_2 += 1
        with open('{}-0.txt'.format(output_fp), 'w', encoding='utf-8') as opt_f:
            opt_f.write(opt_str_0)
        with open('{}-1.txt'.format(output_fp), 'w', encoding='utf-8') as opt_f:
            opt_f.write(opt_str_1)
        with open('{}-2.txt'.format(output_fp), 'w', encoding='utf-8') as opt_f:
            opt_f.write(opt_str_2)

        print(count_0, count_1, count_2)  # 13516 565 55


def split_train_val(label_fp_0, label_fp_1, output_fp, val_rate=0.2):
    with open(label_fp_0, encoding='utf-8') as f:
        lines_0 = f.readlines()
    with open(label_fp_1, encoding='utf-8') as f:
        lines_1 = f.readlines()
    min_len = min(len(lines_0), len(lines_1))
    val_len = int(min_len * val_rate)
    random.shuffle(lines_0)
    random.shuffle(lines_1)

    train_lines = lines_0[val_len:] + lines_1[val_len:]
    val_lines = lines_0[:val_len] + lines_1[:val_len]

    random.shuffle(train_lines)
    random.shuffle(val_lines)

    with open('{}-train.txt'.format(output_fp), 'w', encoding='utf-8') as opt_f:
        opt_f.writelines(train_lines)
    with open('{}-val.txt'.format(output_fp), 'w', encoding='utf-8') as opt_f:
        opt_f.writelines(val_lines)


if __name__ == '__main__':
    ipt_fp = '/home/wbl/workspace/data/raster_data.csv'
    opt_fp = '/home/wbl/workspace/data/raster_data.txt'
    csv_to_txt(ipt_fp, opt_fp)
    csv_to_txt_split_class(ipt_fp, opt_fp)

    ipt_fp_0 = '/home/wbl/workspace/data/raster_data.txt-0.txt'
    ipt_fp_1 = '/home/wbl/workspace/data/raster_data.txt-1.txt'
    opt_fp = '/home/wbl/workspace/data/raster_data'
    split_train_val(ipt_fp_0, ipt_fp_1, opt_fp, val_rate=0.2)

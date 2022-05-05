import subprocess
import pyautogui as py
import time
#import pandas

run = True
while run:
    scan_storage = []
    data_storage = []
    ds = data_storage
    scan = input('\nScan Barcode: ')
    if scan == 'exit':
        run = False
        break
    scan = scan.translate({ord(i):None for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-+={}[]\|:;,<>/?" '})
    scan_storage.append(scan)
    print(scan_storage)
    print(len(scan_storage))
    barcode = scan_storage[0]
    #barcode = barcode.replace('.', '')
    for data in barcode:
        ds.append(data)
    print(data_storage)
    print(len(data_storage))

    #x = type(ds[0])
    x = ds[0]+ds[2]
    y = float(ds[0])+float(ds[2])
    #print(x+y)

    if len(ds) != 40:
        print('Wrong barcode')
        for x in range(40):
            ds.append('0')
        continue

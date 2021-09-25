import os
import random
import sys
import glob

def main_nocontext(init_dir):
    """
    choose the data from _test_remadd.txt, _valid_remadd.txt, _train_remadd.txt
    
    """
    path = init_dir + "/nocontext/train/"
    files = glob.glob(path + '*')
    
    for f in files:
        ftitle, fext = os.path.splitext(f)
        os.rename(f, ftitle + '_1' + fext)
        
    test_meta_path = path + '_test_meta.txt'
    test_remadd_path = path + '_test_remadd.txt'
    valid_meta_path = path + '_valid_meta.txt'
    valid_remadd_path = path + '_valid_remadd.txt'
    train_meta_path = path + '_train_meta.txt'
    train_remadd_path = path + '_train_remadd.txt'
    
    files = [train_meta_path, train_remadd_path, test_meta_path,
             test_remadd_path, valid_meta_path, valid_remadd_path]
    files1 = glob.glob(path + '*')
    
    print(files)
    print(files1)
    
    for i,f in enumerate(files1):
        add =[]
        print('----------------------')
        print(f)
        print(files[i])
        print('----------------------')
        if f == path + '_train_remadd_1.txt' or f == path + '_train_meta_1.txt':
            with open (f) as org_f:
                with open (files[i], 'w') as new_f:
                    lines1 = org_f.readlines()
                    if len(lines1) >= 10000:
                        for j in range (10000):
                            add_line = lines1[j]
                            add_line = add_line.replace('\n', '')
                            add.append(add_line)
                        new_f.write('\n'.join(add))
        else:
            with open (f) as org_f:
                with open (files[i], 'w') as new_f:
                    lines1 = org_f.readlines()
                    if len(lines1) >= 2500:
                        for j in range (2500):
                            add_line = lines1[j]
                            add_line = add_line.replace('\n', '')
                            add.append(add_line)
                        new_f.write('\n'.join(add))
                    
def main(data_dir, context):
    print("take 10000 code")
    if context == "nocontext":
        print("nocontext")
        main_nocontext(data_dir)
    else:
        print("error")

main(sys.argv[1], sys.argv[2])
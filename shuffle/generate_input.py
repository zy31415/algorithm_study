fid = open('input.txt', 'wt')

for ii in range(100):
    fid.write('%d\n'%ii)

fid.close()
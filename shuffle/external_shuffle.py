import math
import random
import os
import shutil

from shuffle import shuffle


def get_num_entries(fn):
    out = 0

    for ln in open(fn, 'rt'):
        out += 1

    return out


def shuffle_a_file(fn):
    fid = open(fn, 'r+t')
    arr = []

    for ln in fid:
        if len(ln.strip()) == 0:
            continue
        arr.append(ln)

    shuffle(arr)

    fid.seek(0)

    for ii in arr:
        fid.write(ii)

    fid.close()


class ExternalShuffle(object):
    # decide how many external files needed.
    # How many entries you can hold in memory for shuffle
    MAX_ENTRY = 10

    def external_shuffle(self, fn):
        num_lines = get_num_entries(fn)

        num_files = int(math.ceil(num_lines/self.MAX_ENTRY))

        self._create_temp_files(num_files)

        for ln in open(fn, 'rt'):
            if len(ln.strip()) == 0:
                continue
            fout = self._get_a_temp_file()
            with open(fout, 'at') as fid:
                fid.write(ln)

        for fn in self._temp_files:
            shuffle_a_file(fn)

        self._concatenate_temp_files()

    def _create_temp_files(self, num_files):
        out = []

        if os.path.exists('temp'):
            shutil.rmtree('temp')

        os.mkdir('temp')

        for ii in range(num_files):
            fn = 'temp/_tmp_%09d.txt'%ii
            out.append(fn)

        self._temp_files = out

    def _get_a_temp_file(self):
        return self._temp_files[random.randrange(0, len(self._temp_files))]

    def _concatenate_temp_files(self):
        fid = open('output.txt', 'wt')
        for _fn in self._temp_files:
            with open(_fn, 'rt') as _fid:
                for ln in _fid:
                    if len(ln.strip()) == 0:
                        continue
                    fid.write(ln)
        fid.close()


if __name__ == "__main__":
    # test cases
    fn = 'input.txt'
    eshuffle = ExternalShuffle()
    eshuffle.external_shuffle(fn)



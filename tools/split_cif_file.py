import os
import argparse
from shutil import copyfile


parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_dir", type=str, default='/mnt/smile1/protein_proj/codes/github/openfold/data/pdb_mmcif/mmcif_files/',
    help="""Path to directory containing mmCIF, FASTA and/or ProteinNet
            .core files"""
)
parser.add_argument(
    "--out_dir", type=str, default='/mnt/smile1/protein_proj/dataset/open_fold/splited_mmcif_files/',
    help="""Path to splited mmCIF, FASTA and/or ProteinNet
            .core files"""
)
parser.add_argument(
    "--split_num", type=int, default=5000,
    help="""file num in each splited folder"""
)

args = parser.parse_args()

path_dict = {}
for f in os.listdir(args.input_dir):
    path = os.path.join(args.input_dir, f)
    path_dict[f] = path

print('file num:', len(path_dict))

save_idx = 0
for idx, fname in enumerate(path_dict):
    if (idx+1) % args.split_num == 0:
        save_idx += 1
    save_dpath = os.path.join(args.out_dir, '{}'.format(save_idx))
    if not os.path.exists(save_dpath):
        os.mkdir(save_dpath)
    save_fpath = os.path.join(save_dpath, fname)
    copyfile(path_dict[fname], save_fpath)







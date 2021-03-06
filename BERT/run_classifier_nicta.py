import os
import sys

MODEL_PATH = sys.argv[1]

command = 'python bert_classifier.py --data_dir ../data/nicta_piboso ' \
          '--bert_model {} ' \
          '--task_name nicta --output_dir results/nicta/biobert_crf ' \
          '--train_batch_size 2 --tag_space 0 --max_seq_length 60 --use_crf ' \
          '--do_train --do_eval --do_lower_case --num_train_epochs 3 ' \
          '--rnn_hidden_size 512 --dropout 0.3 '.format(MODEL_PATH)

os.system(command)
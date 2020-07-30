import os
import json

import torch

class Config:
    save_dir = './ckpts/v11'
    data_folder = '/home/alex/Desktop/data_mid_clean_wonumber'
    #data_folder = './data/meta_wstyle/data_mid_clean_wonumber'
    data_name = 'flickr8k_1_cap_per_img_1_min_word_freq'
    #checkpoint_file = './ckpts/v8/BEST_checkpoint_flickr8k_1_cap_per_img_1_min_word_freq.pth'
    checkpoint_file = None
    word_embedding_weight = './pretrained/embedding.npy'
    #word_embedding_weight = None
    word_map_file = f'{data_folder}/WORDMAP_{data_name}.json'
    
    attention_dim = 512
    emb_dim = 200
    decoder_dim = 512
    dropout = 0.5

    device = 'cuda' # 'cpu'
    epochs = 25
    workers = 1
    batch_size = 64

    optimizer = 'ranger'
    fine_tune_encoder = False
    encoder_lr = 1e-4
    decoder_lr = 4e-3 # 4e-4
    grad_clip = 5.
    alpha_c = 1.
    confidence_c = 2. # None

    best_bleu4 = 0.
    print_freq = 50
    tolerance_epoch = 8
    adjust_epoch = 2
    adjust_step = 0.6
    decay_epoch = 2
    decay_step = 0.8

    
    def save_config(self, save_path):
        # exclude private properties and generic methods
        attrs = [name for name, val in Config.__dict__.items() if not name.endswith('_') and not callable(val)]
        attrs_dict = dict()
        for attr in attrs:
            val = getattr(self, attr, None)
            attrs_dict[attr] = val
        
        with open(save_path, 'w') as f:
            json.dump(attrs_dict, f, indent = 2)

    
    

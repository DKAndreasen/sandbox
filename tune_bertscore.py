# BERTScore "tune"/test which layer in varius encoder models gives the best correlation with human evaluation on
# sentence translation
# See https://github.com/Tiiiger/bert_score/blob/master/tune_layers/tune_layers.py

#from collections import defaultdict  # dict subclass that calls a factory function to supply missing values
from tqdm.auto import tqdm, trange
#from pathlib import Path
import json
import torch
import bert_score
#import pandas as pd
import random
#from scipy.stats import pearsonr

#enable_idf = False

with open('data/preprocessed/loop_q_and_a_w_meta.json', 'r') as f:
    q_and_a_list = json.load(f)

questions = []
answers = []
for q_and_a in q_and_a_list:
    if q_and_a['response'] is not None:
        questions.append(q_and_a['question'])
        answers.append(q_and_a['response'])
        # total 711 pairs, all responses verified by an editor

torch.set_grad_enabled(False)
batch_size = 16
md_summeries = {}
networks = [
    'KennethTM/bert-base-uncased-danish',  # Danish bert model with danish tokenizer
    'bert-base-multilingual-cased',  # The multilingual model that BERTScore suggest for other languages (ie. also Danish)
    'AI-Sweden-Models/roberta-large-1160k',
    "KennethEnevoldsen/dfm-sentence-encoder-large-exp1",
    "KennethEnevoldsen/dacy-large-encoder",
    # These models break something
    #'vesteinn/DanskBERT'  # RuntimeError: The expanded size of the tensor (640) must match the existing size (514) at non-singleton dimension 1.  Target sizes: [16, 640].  Tensor sizes: [1, 514],
]
for network in networks:
    md_summeries[network] = {}
    for enable_idf in [True, False]:
        model_type = network
        print("processing: " + model_type + (" with idf" if enable_idf else ""))

        scorer = bert_score.scorer.BERTScorer(
            model_type=model_type, num_layers=100, idf=enable_idf, all_layers=True
        )

        if scorer.idf:
            scorer.compute_idf(questions)

        print("Calc bert F1 scores for test set")
        _, _, F1_scores = scorer.score(answers, questions, verbose=False, batch_size=batch_size)
        # These scores represent the scores of a set of "gold"-standard question/answers
        mean_F1_scores = torch.mean(F1_scores, dim=1)
        # max_length = scorer._tokenizer.max_len_single_sentence

        # To determine a baseline for the F1 scores we shuffle the answers, and compute these confused F1 scores,
        # this we do ten times to have an average baseline
        print("Calc confused F1 scores for test set")
        mult_confused_scores = []
        for i in trange(10):
            _, _, confused_F1_scores = scorer.score(random.sample(answers, len(answers)), questions, verbose=False,
                                                    batch_size=batch_size)
            mult_confused_scores.append(confused_F1_scores)
        mean_confused_F1_scores = torch.mean(torch.mean(torch.stack(mult_confused_scores), dim=0), dim=1)

        # Determine which layer displays greatest difference between mean F1 scores and the baseline scores set by the
        # confused set of question-responses
        mean_offsetted_F1_scores = mean_F1_scores - mean_confused_F1_scores

        # Format markdown table with info on scores
        nb_layers = len(mean_F1_scores)
        md_table = "|     | " + " | ".join(["layer " + str(i+1) for i in range(nb_layers)]) + " |"
        md_table = md_table + '\n' + (nb_layers + 1) * '| --- ' + "|"
        mean_F1_scores_strs = []
        for i, f1_score in enumerate(mean_F1_scores): 
            if i == int(torch.argmax(mean_F1_scores)):
                mean_F1_scores_strs.append(f"**{f1_score:0.4f}**")
            else:
                mean_F1_scores_strs.append(f"{f1_score:0.4f}")
        md_table = md_table + '\n| mean F1 score | ' + " | ".join(mean_F1_scores_strs) + ' |'

        mean_confused_F1_scores_strs = []
        for i, f1_score in enumerate(mean_confused_F1_scores):
            if i == int(torch.argmax(mean_confused_F1_scores)):
                mean_confused_F1_scores_strs.append(f"**{f1_score:0.4f}**")
            else:
                mean_confused_F1_scores_strs.append(f"{f1_score:0.4f}")
        md_table = md_table + '\n| mean confused F1 score | ' + " | ".join(mean_confused_F1_scores_strs) + ' |'

        mean_offsetted_F1_scores_strs = []
        for i, f1_score in enumerate(mean_offsetted_F1_scores):
            if i == int(torch.argmax(mean_offsetted_F1_scores)):
                mean_offsetted_F1_scores_strs.append(f"**{f1_score:0.4f}**")
            else:
                mean_offsetted_F1_scores_strs.append(f"{f1_score:0.4f}")

        md_table = md_table + '\n| *mean offsetted F1 score* | ' + " | ".join(mean_offsetted_F1_scores_strs) + ' |'
        md_summeries[network]['idf' if enable_idf else 'no_idf'] = md_table
        del scorer

        print(md_table)

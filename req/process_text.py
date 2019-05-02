import numpy as np
import editdistance
sentence_map = np.load('req/control.npy', allow_pickle = True).item()
sentence_list = list(sentence_map)
def calculate_edit_distance_error(y_true, y_pred, normalize = False):
    m=len(y_true)+1
    n=len(y_pred)+1
    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if y_true[i-1] == y_pred[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+3, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
    result = tbl[i,j]
    if(normalize):
        result = tbl[i,j]/len(y_true)
    return result

def find_nearast_sentence(sentence):
    min_error = np.inf
    template = None
    for template_sentence in sentence_list:
        edit_distance = calculate_edit_distance_error(sentence, template_sentence)
        #print(edit_distance, sentence, template_sentence)
        if(min_error > edit_distance):
            min_error = edit_distance
            template = template_sentence
    print(min_error, template)
    return { "command" : template, "command_id" : sentence_map[template]}

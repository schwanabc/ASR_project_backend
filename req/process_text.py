import numpy as np
import editdistance
sentence_map = np.load('req/control.npy', allow_pickle = True).item()
sentence_list = list(sentence_map)
def find_nearast_sentence(sentence):
    min_error = np.inf
    template = None
    for template_sentence in sentence_list:
        edit_distance = editdistance.eval(sentence, template_sentence)
        if(min_error > edit_distance):
            min_error = edit_distance
            template = template_sentence
    return { "command" : template, "command_no" : sentence_map[template]}

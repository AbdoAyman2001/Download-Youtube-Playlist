def ask_q_multiple_choices_on_terminal(question, choices):
    answer_text = " "
    for id_,choice in enumerate(choices) :
        if id_ == 0 :
            answer_text +="(" + choice + "/"
        elif id_ == len(choices)-1 :
            answer_text += choice +")"        
        else:
            answer_text +=choice+"/"
    answer = input(question+answer_text)
    while not(answer in choices):
        answer = input(question+" "+answer_text)
    return answer


def ask_q_num_on_terminal(question, end_point, starting_point=1):
    answer_text = f" ({starting_point}:{end_point})"
    answer = input(question + answer_text)
    if not(int(answer) >= starting_point and int(answer)<= end_point ):
        answer = input(question + answer_text)
    return int(answer)

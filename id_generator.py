
#замикання

def id_generator(starting_id: int =0): #зовнішня фун-я
    id = starting_id
    def generate_next_id(): #внутрішня фун-я
        nonlocal id #звертається до зовнішньої фун-ї
        id += 1
        return id
    return generate_next_id

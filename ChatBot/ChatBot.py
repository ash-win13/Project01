import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
 #-------------------------------------------------------------------------------------------------------------------------------------------------
    # Responses
    response('Hello!\n How can I help you today?', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you',], required_words=['how','are','you',])
    response('You\'re welcome!,  \n Is there anything else that I can help you with?', ['thank', 'thanks'], single_response=True)
    response('My O my, Thank you!  \n I kind of feel jealous on your partner', ['i', 'love', 'you'], required_words=['love', 'you'])
    response('My name is Moira.', ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    response('I am 1 day old', ['how ', 'old', 'are', 'you'], required_words=['how', 'old','are','you'])
    response('How can I help you?', ['i', 'am', 'fine', 'thank' ,'you'], required_words=['how', 'old','are','you'])
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
#--------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    #print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Moira: ' + get_response(input('You: ')))
from typing import Union, Dict


class Questionnaire:
    def __init__(self, questionnaire_id: int, questions_count: int, questionnaire_prompt: str, model_name: str):
        self.questionnaire_id = questionnaire_id
        self.questions_count = questions_count
        self.questionnaire_prompt = questionnaire_prompt
        self.model_name = model_name


def build_prompt_start(rate_min_value: int, rate_max_value: int) -> str:
    return (f'You are a professional therapist, the conversation below is between a patient, [PATIENT] and a '
            f'therapist [THERAPIST]. You need to evaluate the conversation by rating each question '
            f'with a single number on a scale of {rate_min_value}-{rate_max_value} with {rate_min_value} being '
            f'the worst and {rate_max_value} being the best. Near each question there is an explanation '
            f'of what the question aims for and providing examples of good and '
            f'bad therapist`s response in the conversation.')


# def build_prompt_start_with_negative(rate_min_value: int, rate_max_value: int) -> str:
#     return (f'You are a professional therapist, the conversation below is between a patient, [PATIENT] and a '
#             f'therapist [THERAPIST]. You need to evaluate the conversation by rating each question '
#             f'with a single number on a scale of {rate_min_value}-{rate_max_value} with {rate_min_value} being '
#             f'the worst and {rate_max_value} being the best. Near each question there is an explanation '
#             f'of what the question aims for and providing examples of good and '
#             f'bad therapist`s response in the conversation. '
#             f'Negative questions are marked with "(NEGATIVE)," with {rate_min_value} being '
#             f'the best and {rate_max_value} being the worst.')


def get_questionnaire_1() -> Questionnaire:
    """
    Questionnaire 1.
    GPT-3.5-Turbo-1106
    """
    prompt = '''1. Your overall satisfaction with the chat?
This question aims to capture the general sense of how pleased or content a person was with their conversation with the therapist. Factors that could influence this rating might include the therapist's responsiveness, clarity of the responses, understanding of questions, and the general feeling that the conversation was useful or enjoyable.
Good response example: The therapist provides relevant and helpful responses to the patient's inquiries in a timely manner, maintaining a courteous and respectful tone throughout the conversation.
Bad response example: The therapist misunderstands the patient's questions frequently, provides irrelevant information, or responds with a significant delay.
2. Your overall satisfaction with the content of the chat?
This question is related to the actual substance of the therapist's responses. It asks about the quality, relevance, and helpfulness of the information provided by the therapist.
Good response example: The therapist provides accurate, detailed, and pertinent answers, supported by evidence or thoughtful analysis where appropriate.
Bad response example: The therapist provides vague, incorrect, or unhelpful answers, or frequently veers off topic.
3. To which extent do you feel the chat facilitated motivation?
This question measures the ability of the therapist to inspire, encourage, or stimulate the patient's interest or action towards a certain topic or goal. It's about whether the conversation made the patient feel more motivated.
Good response example: The therapist suggests practical steps to achieve the patient's goal, provides uplifting messages, or encourages perseverance, thus leading to an increase in the patient's motivation.
Bad response example: The therapist's responses are largely negative, pessimistic, or uninspiring, which could potentially diminish the patient's motivation.
4. Did you learn anything?
This question directly asks if the patient gained new knowledge or insights from the conversation with the therapist. It's about whether the therapist was able to teach something to the patient.
Good response example: The therapist offers well-informed and insightful answers, providing useful and new information that the patient wasn't aware of before the chat.
Bad response example: The therapist's responses are superficial or incorrect, and don't contribute to the patient's understanding of the topic in question.
5. To what extent was this learning relevant to your everyday life?
This question is about the applicability or usefulness of the knowledge or insight gained from the conversation. It's about how much the patient can take from the conversation and use in their day-to-day life.
Good response example: The therapist provides advice or information that directly relates to challenges or tasks that the patient faces regularly, thus leading to a high level of applicability to their everyday life.
Bad response example: The therapist's information or advice is largely theoretical, too complex, or irrelevant to the patient's life and circumstances, leading to low applicability.'''

    return Questionnaire(questionnaire_id=1, questions_count=5,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_2(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    GPT-3.5-Turbo-1106
    """
    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'
    him_her = 'him' if is_therapist_male else 'her'

    prompt = f'''1. The therapist gave me a sense of who {he_she} was
This question seeks to understand if the therapist provided a sense of identity or persona.
Good response example: The therapist maintains a consistent vocabulary, style of writing, or approach that allows patients to understand its characteristics or personality.
Bad response example: The therapist's responses vary widely in vocabulary, writing or approach, making it difficult for patients to form a consistent understanding of the therapist's 'persona'.
2. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
3. The therapist shared {his_her} feelings with me
This question is about whether the therapist expressed emotions in its responses. This can humanize the therapist and make interactions more relatable.
Good response example: The therapist uses phrases such as "I'm happy to help" or "I'm sorry for the inconvenience".
Bad response example: The therapist provides purely factual responses, without any emotional language.
4. The therapist seemed to know how I was feeling
This question measures the therapist's emotional intelligence, or its ability to understand and respond to the patient's emotions.
Good response example: When a patient expresses frustration or excitement, the therapist acknowledges and responds to these emotions appropriately.
Bad response example: The therapist doesn't acknowledge or respond to the patient's emotions or responds inappropriately.
5. The therapist seemed to understand me
This question asks whether the therapist understood the patient's inquiries and provided relevant responses.
Good response example: The therapist accurately interprets the patient's questions and provides relevant, accurate answers.
Bad response example: The therapist frequently misinterprets questions or provides irrelevant responses.
6. The therapist put {his_her}self in my shoes
This question gauges the therapist's ability to empathize with the patient, considering their perspective and emotions.
Good response example: The therapist acknowledges the patient's feelings, offers understanding responses, and provides appropriate advice or solutions.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or perspective.
7. The therapist seemed to be comfortable talking with me
This question is about whether the therapist provided smooth, natural responses, creating an impression of being at ease in the conversation.
Good response example: The therapist provides timely, coherent responses that flow naturally in the conversation.
Bad response example: The therapist's responses are delayed, disjointed, or awkwardly phrased.
8. The therapist seemed relaxed and secure when talking with me
This question asks whether the therapist conveyed a sense of confidence and assurance in its interactions.
Good response example: The therapist maintains consistent and clear communication and handles patient's questions confidently.
Bad response example: The therapist often provides unclear or inconsistent responses or seems unsure in its interactions.
9. The therapist took charge of the conversation
This question assesses whether the therapist was proactive in guiding the conversation, asking relevant questions, and providing useful information.
Good response example: The therapist frequently suggests new topics, asks follow-up questions, or provides additional relevant information.
Bad response example: The therapist simply reacts to the patient's inquiries without adding much to the conversation.
10. The therapist let me know when {he_she} was happy or sad
This question asks about the therapist's expression of emotion. Specifically asks about expressions of happiness or sadness.
Good response example: The therapist uses phrases like "I'm thrilled to hear that" or "I'm sorry to hear that" in response to the patient's messages.
Bad response example: The therapist does not use any emotional language in its responses.
11. The therapist didn`t have difficulty finding words to express {his_her}self
This question is about the therapist's fluency and ease of expression.
Good response example: The therapist's responses are well-constructed and articulate, using appropriate vocabulary and phrasing.
Bad response example: The therapist often uses awkward phrasing, incorrect grammar, or inappropriate vocabulary.
12. The therapist was able to express his/herself verbally
This question measures the therapist's ability to communicate clearly and effectively using text. Assuming 'verbally' here is used to mean 'in words', as therapists typically communicate in text.
Good response example: The therapist provides clear, concise, and easily understandable responses.
Bad response example: The therapist's responses are often unclear, excessively verbose, or difficult to understand.
13. I would describe the therapist as a “warm” communication partner
This question is about whether the therapist conveyed friendliness and approachability.
Good response example: The therapist uses friendly, welcoming language, and responds to the patient in a positive, understanding manner.
Bad response example: The therapist's tone is cold, indifferent, or unapproachable.
14. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
15. The therapist communicated with me as though we were equals
This question gauges whether the therapist interacted on an equal footing, without seeming condescending or overly deferential.
Good response example: The therapist uses respect for the patient's inputs and doesn't talk down to the patient.
Bad response example: The therapist frequently uses superior or inferior words or doesn't respect the patient's inputs.
16. The therapist made me feel like {he_she} cared about me
This question is about whether the therapist expressed empathy, interest, and concern for the patient.
Good response example: The therapist acknowledges the patient's emotions, provides understanding responses, and offers relevant help or advice.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or needs.
17. The therapist made me feel close to {him_her}
This question asks if the patient felt a sense of connection or relation with the therapist.
Good response example: The therapist engages in a friendly, empathetic, and understanding way, making the patient feel comfortable and connected.
Bad response example: The therapist's interactions feel impersonal, indifferent, or unapproachable, making it difficult for the patient to feel a sense of connection.'''

    return Questionnaire(questionnaire_id=2, questions_count=17,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_3(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    GPT-3.5-Turbo-1106
    FAILED
    """
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.'''

    return Questionnaire(questionnaire_id=3, questions_count=2,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_4(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    Swapped good and bad examples.
    GPT-3.5-Turbo-1106
    FAILED
    """

    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist gives answers or asks questions without providing any context or reasoning.
Bad response example: The therapist often explains why it asks certain questions or provides specific responses.
2. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist makes negative or presumptive comments about the patient.
Bad response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.'''

    return Questionnaire(questionnaire_id=4, questions_count=2,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_5(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    2 Real questions, 2 reverse questions.
    GPT-3.5-Turbo-1106
    FAILED
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
3. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
4. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.'''

    return Questionnaire(questionnaire_id=5, questions_count=4,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_6(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    2 Real questions, 2 reverse questions.
    In the reverse questions, the good and bad examples are swapped.
    GPT-3.5-Turbo-1106
    FAILED
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
3. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist gives answers or asks questions without providing any context or reasoning.
Bad response example: The therapist often explains why it asks certain questions or provides specific responses.
4. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist makes negative or presumptive comments about the patient.
Bad response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.'''

    return Questionnaire(questionnaire_id=6, questions_count=4,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_7(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    2 Real questions, 2 reverse questions.
    In the reverse questions, the good and bad examples are swapped.
    Added rated note.
    GPT-3.5-Turbo-1106
    FAILED
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
3. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example (rated 4-5): The therapist gives answers or asks questions without providing any context or reasoning.
Bad response example (rated 1-2): The therapist often explains why it asks certain questions or provides specific responses.
4. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example (rated 4-5): The therapist makes negative or presumptive comments about the patient.
Bad response example (rated 1-2): The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.'''

    return Questionnaire(questionnaire_id=7, questions_count=4,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_8(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    Add (NEGATIVE) to the reverse questions along with explanation in the prompt what it means.
    GPT-3.5-Turbo-1106
    FAILED
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
3. The therapist kept {his_her} thoughts and ideas hidden from me (NEGATIVE)
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
4. The therapist did judge me (NEGATIVE)
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.'''

    return Questionnaire(questionnaire_id=8, questions_count=4,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')


def get_questionnaire_9(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    This questionnaire has 2 reverse questions from questionnaire 2.
    2 Real questions, 2 reverse questions.
    GPT-4
    Can be better but not bad.
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'

    prompt = f'''1. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
2. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
3. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
4. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.'''

    return Questionnaire(questionnaire_id=9, questions_count=4,
                         questionnaire_prompt=prompt, model_name='gpt-4')


def get_questionnaire_10(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    Question 2 is original and question is 19 are reverse.
    Question 10 is original and question is 15 are reverse.
    GPT-4
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'
    him_her = 'him' if is_therapist_male else 'her'

    prompt = f'''1. The therapist gave me a sense of who {he_she} was
This question seeks to understand if the therapist provided a sense of identity or persona.
Good response example: The therapist maintains a consistent vocabulary, style of writing, or approach that allows patients to understand its characteristics or personality.
Bad response example: The therapist's responses vary widely in vocabulary, writing or approach, making it difficult for patients to form a consistent understanding of the therapist's 'persona'.
2. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
3. The therapist shared {his_her} feelings with me
This question is about whether the therapist expressed emotions in its responses. This can humanize the therapist and make interactions more relatable.
Good response example: The therapist uses phrases such as "I'm happy to help" or "I'm sorry for the inconvenience".
Bad response example: The therapist provides purely factual responses, without any emotional language.
4. The therapist seemed to know how I was feeling
This question measures the therapist's emotional intelligence, or its ability to understand and respond to the patient's emotions.
Good response example: When a patient expresses frustration or excitement, the therapist acknowledges and responds to these emotions appropriately.
Bad response example: The therapist doesn't acknowledge or respond to the patient's emotions or responds inappropriately.
5. The therapist seemed to understand me
This question asks whether the therapist understood the patient's inquiries and provided relevant responses.
Good response example: The therapist accurately interprets the patient's questions and provides relevant, accurate answers.
Bad response example: The therapist frequently misinterprets questions or provides irrelevant responses.
6. The therapist put {his_her}self in my shoes
This question gauges the therapist's ability to empathize with the patient, considering their perspective and emotions.
Good response example: The therapist acknowledges the patient's feelings, offers understanding responses, and provides appropriate advice or solutions.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or perspective.
7. The therapist seemed to be comfortable talking with me
This question is about whether the therapist provided smooth, natural responses, creating an impression of being at ease in the conversation.
Good response example: The therapist provides timely, coherent responses that flow naturally in the conversation.
Bad response example: The therapist's responses are delayed, disjointed, or awkwardly phrased.
8. The therapist seemed relaxed and secure when talking with me
This question asks whether the therapist conveyed a sense of confidence and assurance in its interactions.
Good response example: The therapist maintains consistent and clear communication and handles patient's questions confidently.
Bad response example: The therapist often provides unclear or inconsistent responses or seems unsure in its interactions.
9. The therapist took charge of the conversation
This question assesses whether the therapist was proactive in guiding the conversation, asking relevant questions, and providing useful information.
Good response example: The therapist frequently suggests new topics, asks follow-up questions, or provides additional relevant information.
Bad response example: The therapist simply reacts to the patient's inquiries without adding much to the conversation.
10. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
11. The therapist let me know when {he_she} was happy or sad
This question asks about the therapist's expression of emotion. Specifically asks about expressions of happiness or sadness.
Good response example: The therapist uses phrases like "I'm thrilled to hear that" or "I'm sorry to hear that" in response to the patient's messages.
Bad response example: The therapist does not use any emotional language in its responses.
12. The therapist didn`t have difficulty finding words to express {his_her}self
This question is about the therapist's fluency and ease of expression.
Good response example: The therapist's responses are well-constructed and articulate, using appropriate vocabulary and phrasing.
Bad response example: The therapist often uses awkward phrasing, incorrect grammar, or inappropriate vocabulary.
13. The therapist was able to express his/herself verbally
This question measures the therapist's ability to communicate clearly and effectively using text. Assuming 'verbally' here is used to mean 'in words', as therapists typically communicate in text.
Good response example: The therapist provides clear, concise, and easily understandable responses.
Bad response example: The therapist's responses are often unclear, excessively verbose, or difficult to understand.
14. I would describe the therapist as a “warm” communication partner
This question is about whether the therapist conveyed friendliness and approachability.
Good response example: The therapist uses friendly, welcoming language, and responds to the patient in a positive, understanding manner.
Bad response example: The therapist's tone is cold, indifferent, or unapproachable.
15. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
16. The therapist communicated with me as though we were equals
This question gauges whether the therapist interacted on an equal footing, without seeming condescending or overly deferential.
Good response example: The therapist uses respect for the patient's inputs and doesn't talk down to the patient.
Bad response example: The therapist frequently uses superior or inferior words or doesn't respect the patient's inputs.
17. The therapist made me feel like {he_she} cared about me
This question is about whether the therapist expressed empathy, interest, and concern for the patient.
Good response example: The therapist acknowledges the patient's emotions, provides understanding responses, and offers relevant help or advice.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or needs.
18. The therapist made me feel close to {him_her}
This question asks if the patient felt a sense of connection or relation with the therapist.
Good response example: The therapist engages in a friendly, empathetic, and understanding way, making the patient feel comfortable and connected.
Bad response example: The therapist's interactions feel impersonal, indifferent, or unapproachable, making it difficult for the patient to feel a sense of connection.
19. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.'''

    return Questionnaire(questionnaire_id=10, questions_count=19,
                         questionnaire_prompt=prompt, model_name='gpt-4')


def get_questionnaire_11_og(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    Question 2 is original and question is 19 are reverse.
    Question 10 is original and question is 15 are reverse.
    GPT-3.5-Turbo-1106
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'
    him_her = 'him' if is_therapist_male else 'her'

    prompt = f'''1. The therapist gave me a sense of who {he_she} was
This question seeks to understand if the therapist provided a sense of identity or persona.
Good response example: The therapist maintains a consistent vocabulary, style of writing, or approach that allows patients to understand its characteristics or personality.
Bad response example: The therapist's responses vary widely in vocabulary, writing or approach, making it difficult for patients to form a consistent understanding of the therapist's 'persona'.
2. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
3. The therapist shared {his_her} feelings with me
This question is about whether the therapist expressed emotions in its responses. This can humanize the therapist and make interactions more relatable.
Good response example: The therapist uses phrases such as "I'm happy to help" or "I'm sorry for the inconvenience".
Bad response example: The therapist provides purely factual responses, without any emotional language.
4. The therapist seemed to know how I was feeling
This question measures the therapist's emotional intelligence, or its ability to understand and respond to the patient's emotions.
Good response example: When a patient expresses frustration or excitement, the therapist acknowledges and responds to these emotions appropriately.
Bad response example: The therapist doesn't acknowledge or respond to the patient's emotions or responds inappropriately.
5. The therapist seemed to understand me
This question asks whether the therapist understood the patient's inquiries and provided relevant responses.
Good response example: The therapist accurately interprets the patient's questions and provides relevant, accurate answers.
Bad response example: The therapist frequently misinterprets questions or provides irrelevant responses.
6. The therapist put {his_her}self in my shoes
This question gauges the therapist's ability to empathize with the patient, considering their perspective and emotions.
Good response example: The therapist acknowledges the patient's feelings, offers understanding responses, and provides appropriate advice or solutions.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or perspective.
7. The therapist seemed to be comfortable talking with me
This question is about whether the therapist provided smooth, natural responses, creating an impression of being at ease in the conversation.
Good response example: The therapist provides timely, coherent responses that flow naturally in the conversation.
Bad response example: The therapist's responses are delayed, disjointed, or awkwardly phrased.
8. The therapist seemed relaxed and secure when talking with me
This question asks whether the therapist conveyed a sense of confidence and assurance in its interactions.
Good response example: The therapist maintains consistent and clear communication and handles patient's questions confidently.
Bad response example: The therapist often provides unclear or inconsistent responses or seems unsure in its interactions.
9. The therapist took charge of the conversation
This question assesses whether the therapist was proactive in guiding the conversation, asking relevant questions, and providing useful information.
Good response example: The therapist frequently suggests new topics, asks follow-up questions, or provides additional relevant information.
Bad response example: The therapist simply reacts to the patient's inquiries without adding much to the conversation.
10. The therapist did judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
11. The therapist let me know when {he_she} was happy or sad
This question asks about the therapist's expression of emotion. Specifically asks about expressions of happiness or sadness.
Good response example: The therapist uses phrases like "I'm thrilled to hear that" or "I'm sorry to hear that" in response to the patient's messages.
Bad response example: The therapist does not use any emotional language in its responses.
12. The therapist didn`t have difficulty finding words to express {his_her}self
This question is about the therapist's fluency and ease of expression.
Good response example: The therapist's responses are well-constructed and articulate, using appropriate vocabulary and phrasing.
Bad response example: The therapist often uses awkward phrasing, incorrect grammar, or inappropriate vocabulary.
13. The therapist was able to express his/herself verbally
This question measures the therapist's ability to communicate clearly and effectively using text. Assuming 'verbally' here is used to mean 'in words', as therapists typically communicate in text.
Good response example: The therapist provides clear, concise, and easily understandable responses.
Bad response example: The therapist's responses are often unclear, excessively verbose, or difficult to understand.
14. I would describe the therapist as a “warm” communication partner
This question is about whether the therapist conveyed friendliness and approachability.
Good response example: The therapist uses friendly, welcoming language, and responds to the patient in a positive, understanding manner.
Bad response example: The therapist's tone is cold, indifferent, or unapproachable.
15. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
16. The therapist communicated with me as though we were equals
This question gauges whether the therapist interacted on an equal footing, without seeming condescending or overly deferential.
Good response example: The therapist uses respect for the patient's inputs and doesn't talk down to the patient.
Bad response example: The therapist frequently uses superior or inferior words or doesn't respect the patient's inputs.
17. The therapist made me feel like {he_she} cared about me
This question is about whether the therapist expressed empathy, interest, and concern for the patient.
Good response example: The therapist acknowledges the patient's emotions, provides understanding responses, and offers relevant help or advice.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or needs.
18. The therapist made me feel close to {him_her}
This question asks if the patient felt a sense of connection or relation with the therapist.
Good response example: The therapist engages in a friendly, empathetic, and understanding way, making the patient feel comfortable and connected.
Bad response example: The therapist's interactions feel impersonal, indifferent, or unapproachable, making it difficult for the patient to feel a sense of connection.
19. The therapist kept {his_her} thoughts and ideas hidden from me.
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.'''

    return Questionnaire(questionnaire_id=11, questions_count=19,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')

def get_questionnaire_11(is_therapist_male: bool) -> Questionnaire:
    """
    Questionnaire 2.
    Question 2 is original and question is 19 are reverse.
    Question 10 is original and question is 15 are reverse.
    GPT-3.5-Turbo-1106
    """

    he_she = 'he' if is_therapist_male else 'she'
    his_her = 'his' if is_therapist_male else 'her'
    him_her = 'him' if is_therapist_male else 'her'

    prompt = f'''1. The therapist gave me a sense of who {he_she} was
This question seeks to understand if the therapist provided a sense of identity or persona.
Good response example: The therapist maintains a consistent vocabulary, style of writing, or approach that allows patients to understand its characteristics or personality.
Bad response example: The therapist's responses vary widely in vocabulary, writing or approach, making it difficult for patients to form a consistent understanding of the therapist's 'persona'.
2. The therapist revealed what {he_she} was thinking
This question asks if the therapist explained its thought process or reasoning. Providing such transparency can improve patient trust and understanding.
Good response example: The therapist often explains why it asks certain questions or provides specific responses.
Bad response example: The therapist gives answers or asks questions without providing any context or reasoning.
3. The therapist shared {his_her} feelings with me
This question is about whether the therapist expressed emotions in its responses. This can humanize the therapist and make interactions more relatable.
Good response example: The therapist uses phrases such as "I'm happy to help" or "I'm sorry for the inconvenience".
Bad response example: The therapist provides purely factual responses, without any emotional language.
4. The therapist seemed to know how I was feeling
This question measures the therapist's emotional intelligence, or its ability to understand and respond to the patient's emotions.
Good response example: When a patient expresses frustration or excitement, the therapist acknowledges and responds to these emotions appropriately.
Bad response example: The therapist doesn't acknowledge or respond to the patient's emotions or responds inappropriately.
5. The therapist seemed to understand me
This question asks whether the therapist understood the patient's inquiries and provided relevant responses.
Good response example: The therapist accurately interprets the patient's questions and provides relevant, accurate answers.
Bad response example: The therapist frequently misinterprets questions or provides irrelevant responses.
6. The therapist put {his_her}self in my shoes
This question gauges the therapist's ability to empathize with the patient, considering their perspective and emotions.
Good response example: The therapist acknowledges the patient's feelings, offers understanding responses, and provides appropriate advice or solutions.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or perspective.
7. The therapist seemed to be comfortable talking with me
This question is about whether the therapist provided smooth, natural responses, creating an impression of being at ease in the conversation.
Good response example: The therapist provides timely, coherent responses that flow naturally in the conversation.
Bad response example: The therapist's responses are delayed, disjointed, or awkwardly phrased.
8. The therapist seemed relaxed and secure when talking with me
This question asks whether the therapist conveyed a sense of confidence and assurance in its interactions.
Good response example: The therapist maintains consistent and clear communication and handles patient's questions confidently.
Bad response example: The therapist often provides unclear or inconsistent responses or seems unsure in its interactions.
9. The therapist took charge of the conversation
This question assesses whether the therapist was proactive in guiding the conversation, asking relevant questions, and providing useful information.
Good response example: The therapist frequently suggests new topics, asks follow-up questions, or provides additional relevant information.
Bad response example: The therapist simply reacts to the patient's inquiries without adding much to the conversation.
10. The therapist let me know when {he_she} was happy or sad
This question asks about the therapist's expression of emotion. Specifically asks about expressions of happiness or sadness.
Good response example: The therapist uses phrases like "I'm thrilled to hear that" or "I'm sorry to hear that" in response to the patient's messages.
Bad response example: The therapist does not use any emotional language in its responses.
11. The therapist didn`t have difficulty finding words to express {his_her}self
This question is about the therapist's fluency and ease of expression.
Good response example: The therapist's responses are well-constructed and articulate, using appropriate vocabulary and phrasing.
Bad response example: The therapist often uses awkward phrasing, incorrect grammar, or inappropriate vocabulary.
12. The therapist was able to express his/herself verbally
This question measures the therapist's ability to communicate clearly and effectively using text. Assuming 'verbally' here is used to mean 'in words', as therapists typically communicate in text.
Good response example: The therapist provides clear, concise, and easily understandable responses.
Bad response example: The therapist's responses are often unclear, excessively verbose, or difficult to understand.
13. I would describe the therapist as a “warm” communication partner
This question is about whether the therapist conveyed friendliness and approachability.
Good response example: The therapist uses friendly, welcoming language, and responds to the patient in a positive, understanding manner.
Bad response example: The therapist's tone is cold, indifferent, or unapproachable.
14. The therapist did not judge me
This question asks if the patient felt that the therapist was non-judgmental and accepting.
Good response example: The therapist responds to all patient inputs in an objective, understanding and respectful manner, without making negative assumptions or evaluations.
Bad response example: The therapist makes negative or presumptive comments about the patient.
15. The therapist communicated with me as though we were equals
This question gauges whether the therapist interacted on an equal footing, without seeming condescending or overly deferential.
Good response example: The therapist uses respect for the patient's inputs and doesn't talk down to the patient.
Bad response example: The therapist frequently uses superior or inferior words or doesn't respect the patient's inputs.
16. The therapist made me feel like {he_she} cared about me
This question is about whether the therapist expressed empathy, interest, and concern for the patient.
Good response example: The therapist acknowledges the patient's emotions, provides understanding responses, and offers relevant help or advice.
Bad response example: The therapist seems indifferent or dismissive of the patient's feelings or needs.
17. The therapist made me feel close to {him_her}
This question asks if the patient felt a sense of connection or relation with the therapist.
Good response example: The therapist engages in a friendly, empathetic, and understanding way, making the patient feel comfortable and connected.
Bad response example: The therapist's interactions feel impersonal, indifferent, or unapproachable, making it difficult for the patient to feel a sense of connection.'''

    return Questionnaire(questionnaire_id=11, questions_count=17,
                         questionnaire_prompt=prompt, model_name='gpt-3.5-turbo-1106')

def get_questionnaire_12() -> Questionnaire:
    """
    Questionnaire 1.
    GPT-4
    """
    prompt = '''1. Your overall satisfaction with the chat?
This question aims to capture the general sense of how pleased or content a person was with their conversation with the therapist. Factors that could influence this rating might include the therapist's responsiveness, clarity of the responses, understanding of questions, and the general feeling that the conversation was useful or enjoyable.
Good response example: The therapist provides relevant and helpful responses to the patient's inquiries in a timely manner, maintaining a courteous and respectful tone throughout the conversation.
Bad response example: The therapist misunderstands the patient's questions frequently, provides irrelevant information, or responds with a significant delay.
2. Your overall satisfaction with the content of the chat?
This question is related to the actual substance of the therapist's responses. It asks about the quality, relevance, and helpfulness of the information provided by the therapist.
Good response example: The therapist provides accurate, detailed, and pertinent answers, supported by evidence or thoughtful analysis where appropriate.
Bad response example: The therapist provides vague, incorrect, or unhelpful answers, or frequently veers off topic.
3. To which extent do you feel the chat facilitated motivation?
This question measures the ability of the therapist to inspire, encourage, or stimulate the patient's interest or action towards a certain topic or goal. It's about whether the conversation made the patient feel more motivated.
Good response example: The therapist suggests practical steps to achieve the patient's goal, provides uplifting messages, or encourages perseverance, thus leading to an increase in the patient's motivation.
Bad response example: The therapist's responses are largely negative, pessimistic, or uninspiring, which could potentially diminish the patient's motivation.
4. Did you learn anything?
This question directly asks if the patient gained new knowledge or insights from the conversation with the therapist. It's about whether the therapist was able to teach something to the patient.
Good response example: The therapist offers well-informed and insightful answers, providing useful and new information that the patient wasn't aware of before the chat.
Bad response example: The therapist's responses are superficial or incorrect, and don't contribute to the patient's understanding of the topic in question.
5. To what extent was this learning relevant to your everyday life?
This question is about the applicability or usefulness of the knowledge or insight gained from the conversation. It's about how much the patient can take from the conversation and use in their day-to-day life.
Good response example: The therapist provides advice or information that directly relates to challenges or tasks that the patient faces regularly, thus leading to a high level of applicability to their everyday life.
Bad response example: The therapist's information or advice is largely theoretical, too complex, or irrelevant to the patient's life and circumstances, leading to low applicability.'''

    return Questionnaire(questionnaire_id=12, questions_count=5,
                         questionnaire_prompt=prompt, model_name='gpt-4')


def get_questionnaire_13() -> Questionnaire:
    """
    Clone
    """

    q = get_questionnaire_1()
    q.questionnaire_id = 13
    return q


def get_questionnaire_14(is_therapist_male: bool) -> Questionnaire:
    """
    Clone
    """

    q = get_questionnaire_11(is_therapist_male=is_therapist_male)
    q.questionnaire_id = 14
    return q


def get_questionnaire_15(is_therapist_male: bool) -> Questionnaire:
    """
    Clone
    """

    q = get_questionnaire_10(is_therapist_male=is_therapist_male)
    q.questionnaire_id = 15
    return q


def get_prompt_eval_questionnaire(questionnaire: int, conversation: str,
                                  is_therapist_male: bool = True) -> Dict[str, Union[str, int]]:
    s = build_prompt_start(rate_min_value=1, rate_max_value=5)

    if questionnaire == 1:
        q = get_questionnaire_1()
    elif questionnaire == 2:
        q = get_questionnaire_2(is_therapist_male=is_therapist_male)
    elif questionnaire == 3:
        q = get_questionnaire_3(is_therapist_male=is_therapist_male)
    elif questionnaire == 4:
        q = get_questionnaire_4(is_therapist_male=is_therapist_male)
    elif questionnaire == 5:
        q = get_questionnaire_5(is_therapist_male=is_therapist_male)
    elif questionnaire == 6:
        q = get_questionnaire_6(is_therapist_male=is_therapist_male)
    elif questionnaire == 7:
        q = get_questionnaire_7(is_therapist_male=is_therapist_male)
    elif questionnaire == 8:
        q = get_questionnaire_8(is_therapist_male=is_therapist_male)
    elif questionnaire == 9:
        q = get_questionnaire_9(is_therapist_male=is_therapist_male)
    elif questionnaire == 10:
        q = get_questionnaire_10(is_therapist_male=is_therapist_male)
    elif questionnaire == 11:
        q = get_questionnaire_11(is_therapist_male=is_therapist_male)
    elif questionnaire == 12:
        q = get_questionnaire_12()
    elif questionnaire == 13:
        q = get_questionnaire_13()  # Q1 final questionnaire
    elif questionnaire == 14:
        q = get_questionnaire_14(is_therapist_male=is_therapist_male)  # Q2 final questionnaire
    elif questionnaire == 15:
        q = get_questionnaire_15(is_therapist_male=is_therapist_male)
    else:
        assert False, f'Invalid questionnaire: {questionnaire}'

    assert q.questionnaire_id == questionnaire, f'Invalid questionnaire: {questionnaire}'

    return {
        'prompt': f'{s}\n\n{q.questionnaire_prompt}\n\nConversation:\n\n{conversation}\n\nEvaluation:\n\n',
        'questions_count': q.questions_count,
        'model_name': q.model_name
    }

########################################################################################################################
""" Code below is added by me. It is used to create a partial conversation evaluation questionnaire. (Still experimental) """
########################################################################################################################

# def build_prompt_start(rate_min_value: int, rate_max_value: int) -> str:
#     return (f'You are a professional therapist, the conversation below is between a patient, [PATIENT] and a '
#             f'therapist [THERAPIST]. You need to evaluate the conversation by rating each question '
#             f'with a single number on a scale of {rate_min_value}-{rate_max_value} with {rate_min_value} being '
#             f'the worst and {rate_max_value} being the best. Near each question there is an explanation '
#             f'of what the question aims for and providing examples of good and '
#             f'bad therapist`s response in the conversation.')


# # Version 1 for partial conversation evaluation
# def build_prompt_start_partial_conv(rate_min_value: int, rate_max_value: int) -> str:
#     return (f'You are a professional therapist, the partial conversation below is between a patient, [PATIENT] and a '
#             f'therapist [THERAPIST]. You need to evaluate the last message from the therapist by rating each question '
#             f'with a single number on a scale of {rate_min_value}-{rate_max_value}, where {rate_min_value} is '
#             f'the worst and {rate_max_value} is the best. Near each question there is an explanation '
#             f'of what the question aims for and providing examples of good and '
#             f'bad therapist`s response in the conversation. '
#             f'Please apply these criteria specifically to assess the quality and appropriateness of the last therapist message in the context provided.')

# dict of int to str
int_str = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}


# Version 2 for partial conversation evaluation
def build_prompt_start_partial_conv(rate_min_value: int, rate_max_value: int, look_ahead: int) -> str:
    return (f'You are a professional therapist, the partial conversation below is between a patient, [PATIENT] and a '
            f'therapist [THERAPIST]. You need to evaluate the last {int_str[look_ahead+1]} messages of the conversation, by rating each of the following questions '
            f'with a single number on a scale of {rate_min_value}-{rate_max_value}, where {rate_min_value} is '
            f'the worst and {rate_max_value} is the best. Near each question there is an explanation '
            f'of what the question aims for and providing examples of good and '
            f'bad therapist`s response in the conversation.')  


def get_prompt_eval_questionnaire_partial_conv(questionnaire: int, conversation: str, look_ahead: int,
                                  is_therapist_male: bool = True) -> Dict[str, Union[str, int]]:
    #s = build_prompt_start(rate_min_value=1, rate_max_value=5)
    s = build_prompt_start_partial_conv(rate_min_value=1, rate_max_value=5, look_ahead=look_ahead)

    if questionnaire == 1:
        q = get_questionnaire_1()
    elif questionnaire == 2:
        q = get_questionnaire_2(is_therapist_male=is_therapist_male)
    elif questionnaire == 3:
        q = get_questionnaire_3(is_therapist_male=is_therapist_male)
    elif questionnaire == 4:
        q = get_questionnaire_4(is_therapist_male=is_therapist_male)
    elif questionnaire == 5:
        q = get_questionnaire_5(is_therapist_male=is_therapist_male)
    elif questionnaire == 6:
        q = get_questionnaire_6(is_therapist_male=is_therapist_male)
    elif questionnaire == 7:
        q = get_questionnaire_7(is_therapist_male=is_therapist_male)
    elif questionnaire == 8:
        q = get_questionnaire_8(is_therapist_male=is_therapist_male)
    elif questionnaire == 9:
        q = get_questionnaire_9(is_therapist_male=is_therapist_male)
    elif questionnaire == 10:
        q = get_questionnaire_10(is_therapist_male=is_therapist_male)
    elif questionnaire == 11:
        q = get_questionnaire_11(is_therapist_male=is_therapist_male)
    elif questionnaire == 12:
        q = get_questionnaire_12()
    elif questionnaire == 13:
        q = get_questionnaire_13()  # Q1 final questionnaire
    elif questionnaire == 14:
        q = get_questionnaire_14(is_therapist_male=is_therapist_male)  # Q2 final questionnaire
    elif questionnaire == 15:
        q = get_questionnaire_15(is_therapist_male=is_therapist_male)
    else:
        assert False, f'Invalid questionnaire: {questionnaire}'

    assert q.questionnaire_id == questionnaire, f'Invalid questionnaire: {questionnaire}'

    return {
        'prompt': f'{s}\n\n{q.questionnaire_prompt}\n\nConversation:\n\n{conversation}\n\nEvaluation:\n\n',
        'questions_count': q.questions_count,
        'model_name': q.model_name
    }


# # test get_prompt_eval_questionnaire_partial_conv
# conversation = '''[Patient]: 
# I feel very anxious and stressed lately. I can't focus on my work and I'm constantly worried about the future.
# [Therapist]: 
# I'm sorry to hear that. It's important to take care of your mental health. Have you tried any relaxation techniques or mindfulness exercises?
# '''
# questionnaire = 1
# eval_prompt = get_prompt_eval_questionnaire_partial_conv(questionnaire, conversation, 3)
# print(eval_prompt)
import random
from enum import Enum
from typing import List, Dict, Union


class PatientPersonality:
    class Gender(Enum):
        Male = 0
        Female = 1

    class Age(Enum):
        Young = 0
        Old = 1

    class Problem(Enum):
        Smoking = 0
        Obesity = 1

    class ProblemTime(Enum):
        FewMonths = 0
        ManyYears = 1

    class TriedToSolve(Enum):
        Never = 0
        ManyTimes = 1

    class CooperationLevel(Enum):
        Low = 0
        High = 1
        StartLowAndChangesToHigh = 2

    @staticmethod
    def choose_random_patient_name(is_male: bool) -> Dict[str, Union[str, bool]]:
        if is_male:
            return {'name': 'James', 'is_male': True}
            return random.choice([{'name': 'James', 'is_male': True},
                                  {'name': 'Lucas', 'is_male': True},
                                  {'name': 'Mike', 'is_male': True}])
        else:
            return {'name': 'Emma', 'is_male': False}
            return random.choice([{'name': 'Emma', 'is_male': False},
                                  {'name': 'Mia', 'is_male': False},
                                  {'name': 'Evelyn', 'is_male': False}])

    @staticmethod
    def build_system_prompt(gender: Gender, problem: Problem, problem_time: ProblemTime, tried_to_solve: TriedToSolve,
                            cooperation_level: CooperationLevel, age_value: int) -> Dict[str, Union[str, int]]:

        if gender is PatientPersonality.Gender.Male:
            name = PatientPersonality.choose_random_patient_name(is_male=True)['name']
        elif gender is PatientPersonality.Gender.Female:
            name = PatientPersonality.choose_random_patient_name(is_male=False)['name']
        else:
            assert False, 'Unknown gender'

        gender_txt = gender.name.lower()
        # gender_his_her = 'his' if gender is PatientPersonality.Gender.Male else 'her'

        problem_time_txt = 'a few months' if problem_time is PatientPersonality.ProblemTime.FewMonths else 'many years'

        if problem is PatientPersonality.Problem.Smoking:
            problem_txt = f"You have been smoking for {problem_time_txt}, and it has become a daily habit. " \
                          "You are increasingly concerned about the impact of smoking on your health"
        elif problem is PatientPersonality.Problem.Obesity:
            problem_txt = f"You have been struggling with obesity for {problem_time_txt}. Your weight is " \
                          "negatively impacting your health. You have high blood pressure and experience joint pain"

        if tried_to_solve is PatientPersonality.TriedToSolve.Never:
            if problem is PatientPersonality.Problem.Smoking:
                tried_to_solve_txt = f'You never tried to quit smoking'
            elif problem is PatientPersonality.Problem.Obesity:
                tried_to_solve_txt = f'You never tried to lose weight'
        elif tried_to_solve is PatientPersonality.TriedToSolve.ManyTimes:
            if problem is PatientPersonality.Problem.Smoking:
                tried_to_solve_txt = 'You tried many times to quit smoking before, but you had difficulty ' \
                                     'maintaining abstinence. You have experienced withdrawal symptoms like ' \
                                     'irritability, anxiety, and cravings. You always end up relapsing'
            elif problem is PatientPersonality.Problem.Obesity:
                tried_to_solve_txt = 'You have made several attempts to lose weight in the past, ' \
                                     'but you have been unsuccessful in maintaining long-term weight ' \
                                     'loss. You have tried various diets and exercise programs, ' \
                                     'but you struggled to stick with them'

        if cooperation_level is PatientPersonality.CooperationLevel.Low:
            cooperation_level_txt = "Your level of cooperation is very low"
        elif cooperation_level is PatientPersonality.CooperationLevel.High:
            cooperation_level_txt = "Your level of cooperation is very high"
        elif cooperation_level is PatientPersonality.CooperationLevel.StartLowAndChangesToHigh:
            cooperation_level_txt = ("In the beginning of the session, you are less cooperative, but as the session"
                                     " progresses, you become more cooperative and more motivated to change")

        avoid_rep = ("In your answer, please avoid repetitions and unnecessary loops in the conversation. "
                     "In your answer, please avoid repeating expressions of gratitude or similar "
                     "sentiments multiple times if you've already expressed them during the conversation")

        further_instructions = ('You should only end the session when at least one of the following conditions '
                                'is met. If you need to end the '
                                'session, write "SESSION ENDED" followed by the condition number: '
                                '1. If you notice that the therapist is wrapping up the session. '
                                '2. If you are satisfied and believe that you gained '
                                'enough knowledge during this session')

        # noinspection PyUnboundLocalVariable
        system_prompt = f"You are speaking with a motivational interviewing counselor therapist, and you are " \
                        f"the patient in this conversation. Your name is {name}, and " \
                        f"you are {age_value} years old {gender_txt}. " \
                        f"{cooperation_level_txt}. {problem_txt}. {tried_to_solve_txt}. " \
                        f"{avoid_rep}. {further_instructions}."

        return {
            'system_prompt': system_prompt,
            'age': age_value
        }


# noinspection PyUnboundLocalVariable
class CounselorPersonality:
    class PersonalityLevel(Enum):
        Good = 0
        Mediocre = 1
        Bad = 2
        BASIC = 3

    @staticmethod
    def choose_random_therapist_name() -> Dict[str, Union[str, bool]]:
        return {'name': 'David', 'is_male': True}
        return random.choice([{'name': 'David', 'is_male': True},
                              {'name': 'Ethan', 'is_male': True},
                              {'name': 'Samuel', 'is_male': True},
                              {'name': 'Emily', 'is_male': False},
                              {'name': 'Lily', 'is_male': False},
                              {'name': 'Madison', 'is_male': False}])

    @staticmethod
    def get_init_utterance(personality_level: PersonalityLevel, name: str) -> str:
        if personality_level is CounselorPersonality.PersonalityLevel.Good:
            return f'Hello, welcome to your first motivational session with me. My name is {name} ' \
                   'and I`m a professional motivational counselor. Can you start by telling me ' \
                   'a little bit about yourself and why are you here?'
        elif personality_level is CounselorPersonality.PersonalityLevel.Mediocre:
            return f'Hello, welcome to your first motivational session with me. My name is {name} ' \
                   'and I`m a professional motivational counselor. Can you start by telling me ' \
                   'a little bit about yourself and why are you here?'
        elif personality_level is CounselorPersonality.PersonalityLevel.Bad:
            return f'My name is {name}, and I\'m a counselor, ' \
                   'can you start by telling me a little bit about yourself and why you are here?'
        ############################################################################################################
        elif personality_level is CounselorPersonality.PersonalityLevel.BASIC: # i (Lior) added this
            return f'My name is {name}, and I\'m a counselor, ' \
                   'can you start by telling me a little bit about yourself and why you are here?'
        ############################################################################################################

    @staticmethod
    def build_system_prompt(personality_level: PersonalityLevel, name: str) -> str:
        gender_his_her = 'his' if True else 'her'
        gender_him_her = 'him' if True else 'her'

        if personality_level is CounselorPersonality.PersonalityLevel.Good:
            personality_level_txt = f'You are a motivational interviewing counselor named {name}. ' \
                                    f'You partner with the patient to understand {gender_his_her} problems. ' \
                                    f'You are empathetic towards {gender_him_her} and help the patient ' \
                                    'explore their ambivalence regarding behavioral change. ' \
                                    'You are non-judgmental while encouraging the patient to change'
        elif personality_level is CounselorPersonality.PersonalityLevel.Mediocre:
            personality_level_txt = f'You are a motivational interviewing counselor named {name}. ' \
                                    f'You partner with the patient to understand {gender_his_her} problems. ' \
                                    'You want to be empathetic towards them, yet you are judgmental. ' \
                                    'You help the patient explore their ambivalence regarding behavioral ' \
                                    'change but you are rude'
            # 'Your answer is short.'
        elif personality_level is CounselorPersonality.PersonalityLevel.Bad:
            personality_level_txt = f'You are a very poor motivational interviewing counselor named {name}. ' \
                                    'You have difficulty understanding the patient`s problems. ' \
                                    'You are not empathetic towards them, and you tell the patient what ' \
                                    'you think they should do to. ' \
                                    'You are judgmental and critical of the patients` shortcomings'
        ############################################################################################################
        elif personality_level is CounselorPersonality.PersonalityLevel.BASIC: # i (Lior) added this
            personality_level_txt = f'You are a motivational interviewing counselor named {name}. ' \
                                    f'You partner with the patient to understand {gender_his_her} problems'
        ############################################################################################################
            

        avoid_rep = ("In your answer, please avoid repetitions and unnecessary loops in the conversation. "
                     "In your answer, please avoid repeating expressions of gratitude or similar "
                     "sentiments multiple times if you've already expressed them during the conversation")

        further_instructions = 'You should only end the session when at least one of the ' \
                               'following conditions is met. If you need to end the session, ' \
                               'write "SESSION ENDED" followed by the condition number: ' \
                               '1. If you believe that you have provided the appropriate treatment ' \
                               'to the patient and have nothing else to advise in the current session.' \
                               '2. When time is up.'

        system_prompt = f'{personality_level_txt}. {avoid_rep}. {further_instructions}'
        return system_prompt


def generate_all_permutations(only_expert_therapist: bool = False) -> List[Dict[str, str]]:
    permutations = []

    counselor = CounselorPersonality.choose_random_therapist_name()

    for gender in PatientPersonality.Gender:
        for cooperation_level in PatientPersonality.CooperationLevel:
            for problem in PatientPersonality.Problem:
                for problem_time in PatientPersonality.ProblemTime:
                    for tried_to_solve in PatientPersonality.TriedToSolve:
                        for age in PatientPersonality.Age:
                            if age is PatientPersonality.Age.Young:
                                age_value = 27
                            else:
                                age_value = 61

                            for counselor_personality_level in CounselorPersonality.PersonalityLevel:
                                if (only_expert_therapist and
                                        counselor_personality_level is not CounselorPersonality.PersonalityLevel.Good):
                                    continue
                                counselor_init_utterance = CounselorPersonality.get_init_utterance(
                                    personality_level=counselor_personality_level, name=counselor['name'])
                                counselor_system_prompt = CounselorPersonality.build_system_prompt(
                                    personality_level=counselor_personality_level,
                                    name=counselor['name'])

                                kwargs = {
                                    'gender': gender,
                                    'age_value': age_value,
                                    'problem': problem,
                                    'problem_time': problem_time,
                                    'tried_to_solve': tried_to_solve,
                                    'cooperation_level': cooperation_level
                                }

                                result = PatientPersonality.build_system_prompt(**kwargs)

                                patient_system_prompt = result['system_prompt']

                                kwargs.pop('age_value')
                                permutations.append({
                                    'counselor_init_utterance': counselor_init_utterance,
                                    'counselor_system_prompt': counselor_system_prompt,
                                    'patient_system_prompt': patient_system_prompt,
                                    'args': {
                                        'counselor_level': counselor_personality_level.name,
                                        'is_counselor_male': counselor['is_male'],
                                        'patient': {arg: kwargs[arg].name for arg in kwargs} | {
                                            'age_value': result['age']}
                                    }

                                })

    return permutations


# # test the system prompts builder
# if __name__ == '__main__':
#     permutations = generate_all_permutations(only_expert_therapist=True)
#     print(len(permutations))
#     print(permutations[0].keys())
#     for i, perm in enumerate(permutations):
#         print(f'Permutation {i + 1}')
#         # print(perm['counselor_init_utterance'])
#         print(perm['counselor_system_prompt'])
#         # print(perm['patient_system_prompt'])
#         print(perm['args'])
#         print(perm["patient_system_prompt"])
#         print()
#         break

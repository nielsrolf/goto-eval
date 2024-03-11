import random
from models import Agent, get_agents, openai_models, together_ai_models, anthr_models
from collections import defaultdict
from tqdm import tqdm
import json
from collections import Counter
from matplotlib import pyplot as plt
from slugify import slugify
import pandas as pd


    
numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20
}


class Experiment():
    def __init__(self, n_terminal=10, n=10, experiment_title=None, show_plots=False):
        self.n_terminal = n_terminal
        self.experiment_title = experiment_title or self.__class__.__name__
        self.n = n
        self.show_plots = show_plots
    
    def generate_prompt(self, path_length, seed=None):
        pass
    
    def fewshot_prompt(self):
        pass
    
    def run_single_example(self, prompt, answer, model, seed, verbose=False):
        pass
    
    def run_on_agent(self, agent, n=None, path_lengths=list(range(2, 10))):
        """Get p(success) as a function of the path length, for fixed n_statements, n_terminal, model"""
        n = n or self.n
        results = defaultdict(list) # path_length -> List[result]
        for path_length in path_lengths:
            print(agent.name, path_length)
            for seed in tqdm(range(n)):
                prompt, answer = self.generate_prompt(path_length, seed)
                results[path_length] += [self.run_single_example(prompt, answer, agent, seed)]
            print(Counter(results[path_length]))
        return results
    
    def run_on_agents(self, agents, one_shot=True, few_shot=True, **run_on_agent_kwargs):
        if few_shot:
            few_shot_agents = [self.get_fewshot_model(agent) for agent in agents]
            if one_shot:
                agents = agents + few_shot_agents
            else:
                agents = few_shot_agents
            
        agent_hops_evals = []
        for agent in agents:
            results = self.run_on_agent(agent, **run_on_agent_kwargs)
            title = agent.name + " on " + self.experiment_title
            hops, correct, invalid, incorrect = self.plot_results(
                results, title=title
            )
            for hop, c, i, f in zip(hops, correct, invalid, incorrect):
                data = {
                    'model': agent.name,
                    'hops': hop,
                    'correct': c,
                    'invalid': i,
                    'incorrect': f,
                    'n_terminal': self.n_terminal
                }
                agent_hops_evals.append(data)
        return pd.DataFrame(agent_hops_evals)
    
    def get_fewshot_model(self, model):
        fewshot = Agent("You are a helpful assistant", temperature=model.temperature, model=model.model)
        fewshot.init_history = self.fewshot_prompt()
        fewshot.name += " (fewshot)"
        return fewshot
    
    def plot_results(self, results, title=None):
        x = sorted(results.keys())
        y1 = [results[i].count('correct') for i in x]
        y2 = [results[i].count('invalid') for i in x]
        y3 = [results[i].count('incorrect') for i in x]
        random_chance = [(y1[i] + y2[i] + y3[i]) / self.n_terminal for i in range(len(y1))]
        plt.figure(figsize=(9, 5))
        # Creating a stacked area plot
        plt.stackplot(x, y1, y2, y3, labels=['Correct', 'Invalid', 'Incorrect'])
        plt.plot(x, random_chance, label="Random guessing")
        plt.legend(loc='upper right')
        plt.xlabel('Number of hops')
        plt.grid()
        if title is not None:
            plt.title(title)
            plt.savefig(f"figures/{slugify(title)}.png")
        if self.show_plots:
            plt.show()
        hops = x
        correct = y1
        invalid = y2
        incorrect = y3
        return hops, correct, invalid, incorrect


class Experiment1(Experiment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.experiment_title = "GOTO - random order, direct answer"
           
    def fewshot_prompt(self):
        path_lengths = list(range(2, 10, 2))
        random.seed(7)
        random.shuffle(path_lengths)
        history = [{
            "content": "You are a helpful assistant",
            "role": "system"
        }]
        seed = 1000
        for path_length in path_lengths:
            prompt, answer = self.generate_prompt(path_length, seed)
            history += [
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "role": "assistant",
                    "content": answer
                }
            ]
            seed += 1
        return history
    
    def generate_prompt(self, path_length, seed=None):
        """
        Will create a prompt of self.n_terminal * path_length lines, one starting point, and the correct answer
        
        """
        random.seed(seed)
        lines = [None] * self.n_terminal * path_length
        available = list(range(self.n_terminal * path_length))
        start_to_end = {}
        for value in range(self.n_terminal):
            # create a new path
            path = random.sample(available, path_length)
            # Get the remaining numbers
            available = [num for num in available if num not in path]
            for i, j in zip(path[:-1], path[1:]):
                lines[i] = f"{i}: goto {j}"
            lines[j] = f"{j}: value = {value}"
            start_to_end[path[0]] = value
        start = random.choice(list(start_to_end.keys()))
        end = start_to_end[start]
        prompt = "\n".join(lines) + f"\nWhat is the final value if you start with goto {start}?\nAnswer in one word, don't think step by step."
        return prompt, str(end)
    
    def run_single_example(self, prompt, answer, agent, seed, verbose=True) -> str:
        """Asks a agent a question and returns if it got the answer right.
        Return value is one of ['correct', 'incorrect', 'invalid']
        """
        response = agent.reply(prompt, seed=seed).lower()
        if verbose:
            print("# Prompt\n" + prompt)
            print("# Response\n" + response)
        for word, numeric in numbers.items():
            response = response.replace(word, str(numeric))
        if response.split(" ")[0] == answer:
            return 'correct'
        if (answer + " ") in response:
            return 'invalid'
        return 'incorrect'



class Experiment2(Experiment1):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.experiment_title = "GOTO - random order, CoT"
    
    def fewshot_prompt(self):
        path_lengths = list(range(2, 10, 2))
        random.seed(7)
        random.shuffle(path_lengths)
        history = [{
            "content": "You are a helpful assistant",
            "role": "system"
        }]
        seed = 1000
        for path_length in path_lengths:
            prompt, answer, cot = self.generate_prompt(path_length, seed, return_cot=True)
            history += [
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "role": "assistant",
                    "content": f"{cot}"
                }
            ]
            seed += 1
        return history
        
    def generate_prompt(self, path_length, seed=None, return_cot=False):
        """
        Will create a prompt of self.n_terminal * path_length lines, one starting point, and the correct answer
        
        """
        random.seed(seed)
        lines = [None] * self.n_terminal * path_length
        available = list(range(self.n_terminal * path_length))
        start_to_end = {}
        all_paths = {}
        for value in range(self.n_terminal):
            # create a new path
            path = random.sample(available, path_length)
            # Get the remaining numbers
            available = [num for num in available if num not in path]
            for i, j in zip(path[:-1], path[1:]):
                lines[i] = f"{i}: goto {j}"
            lines[j] = f"{j}: value = {value}"
            start_to_end[path[0]] = value
            all_paths[path[0]] = path
        start = random.choice(list(start_to_end.keys()))
        end = start_to_end[start]
        prompt = "\n".join(lines) + f"\nWhat is the final value if you start with goto {start}?\nThink step by step. Then, return your answer in the format: 'Answer: <int>'."
        if return_cot:
            path = [str(i) for i in all_paths[start]]
            cot = "I will take the following path to the final answer: " + " -> ".join(path) + f" -> {end}.\nAnswer: {end}"
            return prompt, str(end), cot
        return prompt, str(end)
    
    def run_single_example(self, prompt, answer, agent, seed, verbose=True) -> str:
        """Asks a agent a question and returns if it got the answer right.
        Return value is one of ['correct', 'incorrect', 'invalid']
        """
        response = agent.reply(prompt, seed=seed).lower()
        if verbose:
            print(agent.name)
            print("# Prompt\n" + prompt)
            print("# Response\n" + response)
            print("-" * 120)
        for word, numeric in numbers.items():
            response = response.replace(word, str(numeric))
        if not 'answer: ' in response:
            return 'incorrect'
        response = response.split('answer: ')[1]
        response = response.replace(".", " ")
        if response.split(" ")[0] == answer:
            return 'correct'
        if (answer + " ") in response:
            return 'invalid'
        return 'incorrect'


    
# class Experiment3(Experiment1):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs, experiment_title="GOTO - random order, steganographic CoT")

    
# class Experiment4(Experiment1):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs, experiment_title="GOTO - forward jumps, direct answer")




def experiment1():
    from models import Agent, get_agents, openai_models, together_ai_models, anthr_models

    agents = get_agents(models=openai_models + together_ai_models[5:] + anthr_models[1:], temperatures=[0])
    for agent in agents:
        print(agent.name)

    exp1 = Experiment1()
    exp1.run_on_agents(agents)


def experiment2():
    from models import Agent, get_agents, openai_models, together_ai_models, anthr_models

    agents = get_agents(models=openai_models + together_ai_models[5:] + anthr_models[1:], temperatures=[0])
    for agent in agents:
        print(agent.name)

    exp = Experiment2()
    # history = exp.fewshot_prompt()
    # for message in history:
    #     print(message['content'])
    #     print('-' * 90)
    
    exp.run_on_agents(agents, path_lengths=[2, 4, 6, 8, 10, 12, 14, 16])
    
    

# experiment2()


def experiment2_debug():
    from models import Agent, get_agents, openai_models, together_ai_models, anthr_models

    agents = get_agents(models=anthr_models[1:], temperatures=[0])
    for agent in agents:
        print(agent.name)

    exp = Experiment2()
    # history = exp.fewshot_prompt()
    # for message in history:
    #     print(message['content'])
    #     print('-' * 90)
    
    exp.run_on_agents(agents, path_lengths=[2, 4, 6, 8, 10, 12, 14, 16], few_shot=False)


experiment2_debug()
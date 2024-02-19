# How many inference steps can a language model do?

Related to "Out of context reasoning", we wonder: how many reasoning steps can a LLM perform in various settings. We use a `goto-eval` - a prompt that tells the model one true hint, which then points to a different hint and so on, forming a path to one terminal value. We then ask the model about that terminal value.

Experiment variants:
- exp 1: hints first, random order hints, pretrained LLMs, no CoT: goto-steps per inference token
  - p(success) as function of path length
  - compare various models, in particular of different size & temperature
- exp 2: same as exp 1, but allow the model to output a long random text (no numbers allowed) before giving the answer
  - tests for steganography
    -  Niels prediction: it will slightly help, low effect, low confidence
    - Mikita prediction: it will slightly help (after update because of talking about cot faithfulness paper), low confidence
        - instruct to avoid obvious schemes a la "i will say x to mean 6, y to mean 7 etc"
        - test for being able to evade monitoring: tell about control framework 
- exp 3: same as exp 1, but after the question has been asked there is a "guided meditation" of at least the path length, telling the model to "Think of step by step. Think of the correct hint. Now think of the next number. Now think of the next number. (...)", then ask it to reply in one word.
    - tests for "reasoning that can happen while reading random text
    - Niels prediction: a bit likely ~66% -> 55% -> 40% that it will have a bit stronger effect than exp2
    - Mikita prediction: probably no significant difference to exp 2, or worse
    - Comments
        - if it works, it would be more surprising if it works for long path lengths, because longer paths seem to require more goto operations and more depth
- exp 4: same as exp 1, except hints appear in order and correct value is known from the beginning
  - could be solved by an lstm, tests for how far from optimal current models are
    - Niels & Mikita prediction: higher chances this works with high accuracy
- exp 5: train nano-gpt's on exp 1 type of prompts, except replace english with a small vocabulary for a GOTO-language
  - train with mixed path length, see what is the highest it can reliably do at inference time
  - 5.1 train only with max path length up to n, see if it can then solve the task up to path length n (2 n?)
  - 5.2: train only with path length up to eg 3
    - does it generalize for longer paths than what was trained on?
       
- exp 6: train nano-gpt's in a way similar to "out of context reasoning" - where hints are scattered over many contexts, but there exists a gradient to perform better when taking hints seen previously into account
   - meta out of context learning - Dima Krashenn..
       - small models can do 1/2 hops
       - interesting follow up question: how many can it do

- interpretability - train probes? partner with mech interp people?

- Leo Gao Manifold experiment - relevant for exp 1, 2, 5?
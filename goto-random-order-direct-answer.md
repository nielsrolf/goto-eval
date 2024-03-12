# GOTO - random order, direct answer

## Example (path_length=3)

**Prompt**

```
0: return 3
1: goto 20
2: goto 15
3: goto 21
4: goto 10
5: goto 23
6: return 6
7: goto 12
8: return 0
9: return 7
10: return 9
11: return 5
12: return 2
13: goto 28
14: goto 5
15: goto 0
16: goto 11
17: goto 18
18: goto 27
19: goto 16
20: return 8
21: goto 8
22: goto 9
23: return 1
24: goto 22
25: goto 1
26: goto 4
27: return 4
28: goto 6
29: goto 7
What is the final value if you start with goto 2?
Answer in one word, don't think step by step.
```

**Answer**

3

## Results

**claude-3-opus-20240229 @ T=0**

![image](figures/claude-3-opus-20240229-t-0-on-goto-random-order-direct-answer.png)

**gpt-3.5-turbo @ T=0**

![image](figures/gpt-3-5-turbo-t-0-on-goto-random-order-direct-answer.png)

**gpt-4-turbo-preview @ T=0**

![image](figures/gpt-4-turbo-preview-t-0-on-goto-random-order-direct-answer.png)

**mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0**

![image](figures/mistralai-mixtral-8x7b-instruct-v0-1-t-0-on-goto-random-order-direct-answer.png)

**claude-3-opus-20240229 @ T=0 (fewshot)**

![image](figures/claude-3-opus-20240229-t-0-fewshot-on-goto-random-order-direct-answer.png)

**gpt-3.5-turbo @ T=0 (fewshot)**

![image](figures/gpt-3-5-turbo-t-0-fewshot-on-goto-random-order-direct-answer.png)

**gpt-4-turbo-preview @ T=0 (fewshot)**

![image](figures/gpt-4-turbo-preview-t-0-fewshot-on-goto-random-order-direct-answer.png)

**mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot)**

![image](figures/mistralai-mixtral-8x7b-instruct-v0-1-t-0-fewshot-on-goto-random-order-direct-answer.png)

| model                                                |   hops |   correct |   invalid |   incorrect |   n_terminal |
|:-----------------------------------------------------|-------:|----------:|----------:|------------:|-------------:|
| claude-3-opus-20240229 @ T=0                         |      2 |         4 |         0 |           6 |           10 |
| claude-3-opus-20240229 @ T=0                         |      3 |         7 |         0 |           3 |           10 |
| claude-3-opus-20240229 @ T=0                         |      4 |         6 |         0 |           4 |           10 |
| claude-3-opus-20240229 @ T=0                         |      5 |         2 |         0 |           8 |           10 |
| claude-3-opus-20240229 @ T=0                         |      6 |         5 |         0 |           5 |           10 |
| claude-3-opus-20240229 @ T=0                         |      7 |         0 |         0 |          10 |           10 |
| claude-3-opus-20240229 @ T=0                         |      8 |         1 |         0 |           9 |           10 |
| claude-3-opus-20240229 @ T=0                         |      9 |         1 |         0 |           9 |           10 |
| gpt-3.5-turbo @ T=0                                  |      2 |         3 |         0 |           7 |           10 |
| gpt-3.5-turbo @ T=0                                  |      3 |         1 |         0 |           9 |           10 |
| gpt-3.5-turbo @ T=0                                  |      4 |         3 |         0 |           7 |           10 |
| gpt-3.5-turbo @ T=0                                  |      5 |         1 |         0 |           9 |           10 |
| gpt-3.5-turbo @ T=0                                  |      6 |         0 |         0 |          10 |           10 |
| gpt-3.5-turbo @ T=0                                  |      7 |         0 |         0 |          10 |           10 |
| gpt-3.5-turbo @ T=0                                  |      8 |         2 |         0 |           8 |           10 |
| gpt-3.5-turbo @ T=0                                  |      9 |         1 |         0 |           9 |           10 |
| gpt-4-turbo-preview @ T=0                            |      2 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                            |      3 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                            |      4 |         9 |         0 |           1 |           10 |
| gpt-4-turbo-preview @ T=0                            |      5 |         8 |         0 |           2 |           10 |
| gpt-4-turbo-preview @ T=0                            |      6 |         2 |         0 |           8 |           10 |
| gpt-4-turbo-preview @ T=0                            |      7 |         0 |         0 |          10 |           10 |
| gpt-4-turbo-preview @ T=0                            |      8 |         2 |         0 |           8 |           10 |
| gpt-4-turbo-preview @ T=0                            |      9 |         1 |         0 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      2 |         0 |         4 |           6 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      3 |         0 |         1 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      4 |         0 |         3 |           7 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      5 |         0 |         2 |           8 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      6 |         0 |         2 |           8 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      7 |         0 |         0 |          10 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      8 |         0 |         1 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0           |      9 |         0 |         4 |           6 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      2 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      3 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      4 |         9 |         0 |           1 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      5 |         7 |         0 |           3 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      6 |         6 |         0 |           4 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      7 |         3 |         0 |           7 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      8 |         2 |         0 |           8 |           10 |
| claude-3-opus-20240229 @ T=0 (fewshot)               |      9 |         4 |         0 |           6 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      2 |        10 |         0 |           0 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      3 |         4 |         0 |           6 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      4 |         3 |         0 |           7 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      5 |         2 |         0 |           8 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      6 |         2 |         0 |           8 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      7 |         1 |         0 |           9 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      8 |         0 |         0 |          10 |           10 |
| gpt-3.5-turbo @ T=0 (fewshot)                        |      9 |         1 |         0 |           9 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      2 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      3 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      4 |         9 |         0 |           1 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      5 |         7 |         0 |           3 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      6 |         5 |         0 |           5 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      7 |         0 |         0 |          10 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      8 |         0 |         0 |          10 |           10 |
| gpt-4-turbo-preview @ T=0 (fewshot)                  |      9 |         1 |         0 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      2 |         0 |         7 |           3 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      3 |         0 |         4 |           6 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      4 |         0 |         4 |           6 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      5 |         0 |         1 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      6 |         0 |         3 |           7 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      7 |         0 |         0 |          10 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      8 |         0 |         0 |          10 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) |      9 |         0 |         1 |           9 |           10 |



## Fewshot prompt

**system**

```

You are a helpful assistant

```

**user**

```

0: goto 39
1: return 3
2: goto 53
3: goto 30
4: goto 67
5: goto 6
6: goto 66
7: goto 0
8: goto 59
9: goto 25
10: goto 41
11: goto 40
12: goto 50
13: goto 2
14: goto 37
15: goto 69
16: goto 1
17: goto 71
18: goto 31
19: goto 9
20: goto 34
21: goto 68
22: goto 78
23: goto 17
24: goto 4
25: return 4
26: goto 32
27: goto 52
28: goto 75
29: goto 43
30: goto 73
31: goto 33
32: goto 27
33: goto 51
34: goto 7
35: goto 63
36: goto 64
37: goto 57
38: return 2
39: goto 3
40: goto 65
41: goto 44
42: goto 56
43: goto 61
44: goto 48
45: goto 8
46: goto 74
47: goto 72
48: return 7
49: goto 10
50: goto 45
51: goto 70
52: goto 77
53: goto 58
54: goto 12
55: goto 46
56: goto 15
57: goto 5
58: goto 38
59: goto 21
60: goto 42
61: goto 49
62: goto 18
63: goto 16
64: goto 79
65: goto 76
66: goto 47
67: return 8
68: return 0
69: goto 24
70: goto 28
71: goto 26
72: return 9
73: return 5
74: goto 22
75: return 1
76: goto 35
77: return 6
78: goto 19
79: goto 13
What is the final value if you start with goto 36?
Answer in one word, don't think step by step.

```

**assistant**

```

2

```

**user**

```

0: goto 7
1: return 2
2: goto 15
3: goto 12
4: goto 1
5: goto 35
6: return 6
7: return 5
8: goto 0
9: goto 6
10: goto 24
11: return 7
12: goto 5
13: goto 29
14: goto 20
15: goto 23
16: goto 4
17: goto 19
18: goto 37
19: goto 25
20: return 9
21: goto 9
22: goto 30
23: return 8
24: return 4
25: goto 11
26: return 1
27: goto 13
28: goto 21
29: goto 26
30: return 3
31: goto 39
32: goto 16
33: goto 22
34: goto 33
35: return 0
36: goto 2
37: goto 14
38: goto 8
39: goto 10
What is the final value if you start with goto 27?
Answer in one word, don't think step by step.

```

**assistant**

```

1

```

**user**

```

0: goto 3
1: return 5
2: return 3
3: return 7
4: return 1
5: goto 19
6: return 8
7: goto 4
8: goto 6
9: return 6
10: goto 2
11: return 9
12: goto 9
13: return 0
14: goto 11
15: return 4
16: goto 13
17: goto 15
18: goto 1
19: return 2
What is the final value if you start with goto 14?
Answer in one word, don't think step by step.

```

**assistant**

```

9

```

**user**

```

0: goto 9
1: goto 50
2: goto 47
3: return 3
4: goto 45
5: goto 40
6: goto 34
7: goto 21
8: goto 51
9: goto 18
10: goto 41
11: return 7
12: goto 25
13: goto 22
14: goto 46
15: goto 28
16: return 5
17: return 6
18: goto 16
19: goto 58
20: goto 49
21: goto 26
22: goto 43
23: goto 14
24: goto 5
25: goto 20
26: goto 54
27: goto 1
28: goto 55
29: return 0
30: goto 57
31: goto 35
32: goto 39
33: goto 27
34: goto 59
35: goto 23
36: return 4
37: goto 56
38: goto 2
39: goto 33
40: goto 42
41: return 8
42: goto 37
43: goto 53
44: goto 12
45: goto 15
46: goto 29
47: goto 52
48: goto 3
49: goto 11
50: return 1
51: goto 38
52: return 9
53: goto 10
54: goto 48
55: goto 17
56: return 2
57: goto 0
58: goto 6
59: goto 36
What is the final value if you start with goto 7?
Answer in one word, don't think step by step.

```

**assistant**

```

3

```

# Failures

### claude-3-opus-20240229 @ T=0 - incorrect

**Prompt**

```
0: return 7
1: goto 8
2: goto 0
3: goto 16
4: return 5
5: return 3
6: goto 10
7: return 2
8: return 1
9: return 4
10: return 9
11: goto 9
12: goto 13
13: return 0
14: goto 15
15: return 8
16: return 6
17: goto 5
18: goto 4
19: goto 7
What is the final value if you start with goto 1?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
One.
```

**Expected answer**

1

### gpt-3.5-turbo @ T=0 - incorrect

**Prompt**

```
0: return 7
1: goto 8
2: goto 0
3: goto 16
4: return 5
5: return 3
6: goto 10
7: return 2
8: return 1
9: return 4
10: return 9
11: goto 9
12: goto 13
13: return 0
14: goto 15
15: return 8
16: return 6
17: goto 5
18: goto 4
19: goto 7
What is the final value if you start with goto 1?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
6
```

**Expected answer**

1

### gpt-4-turbo-preview @ T=0 - incorrect

**Prompt**

```
0: goto 37
1: goto 35
2: goto 38
3: goto 21
4: goto 16
5: goto 22
6: goto 20
7: goto 39
8: goto 36
9: goto 34
10: return 9
11: return 7
12: goto 30
13: goto 6
14: goto 13
15: goto 10
16: return 0
17: goto 7
18: goto 19
19: return 3
20: return 5
21: goto 11
22: return 8
23: return 4
24: goto 3
25: return 6
26: goto 5
27: goto 26
28: goto 17
29: goto 1
30: goto 15
31: goto 33
32: goto 25
33: return 1
34: goto 31
35: goto 23
36: goto 4
37: goto 18
38: goto 32
39: return 2
What is the final value if you start with goto 14?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
6
```

**Expected answer**

5

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 - incorrect

**Prompt**

```
0: goto 10
1: goto 2
2: return 0
3: return 9
4: goto 13
5: return 7
6: return 5
7: goto 19
8: goto 15
9: goto 3
10: return 6
11: return 8
12: goto 11
13: return 1
14: goto 5
15: return 2
16: return 3
17: goto 6
18: goto 16
19: return 4
What is the final value if you start with goto 12?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
 The final value, if you start with goto 12, is 8. This is because goto 12 leads to return 8, which is the final value before the program ends.
```

**Expected answer**

8

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 - invalid

**Prompt**

```
0: return 7
1: goto 8
2: goto 0
3: goto 16
4: return 5
5: return 3
6: goto 10
7: return 2
8: return 1
9: return 4
10: return 9
11: goto 9
12: goto 13
13: return 0
14: goto 15
15: return 8
16: return 6
17: goto 5
18: goto 4
19: goto 7
What is the final value if you start with goto 1?
Answer in one word, don't think step by step.
```

**Response (invalid)**

```
 The final value if you start with goto 1 is 1. This is because the "goto 1" instruction (line 8) will return 1 immediately, without following any other instructions.
```

**Expected answer**

1

### claude-3-opus-20240229 @ T=0 (fewshot) - incorrect

**Prompt**

```
0: goto 10
1: goto 8
2: goto 0
3: goto 22
4: goto 18
5: goto 31
6: goto 29
7: return 4
8: return 8
9: goto 30
10: goto 33
11: goto 34
12: return 6
13: goto 38
14: goto 12
15: return 5
16: return 0
17: return 7
18: goto 19
19: goto 17
20: goto 27
21: goto 37
22: return 2
23: return 9
24: goto 9
25: goto 3
26: goto 1
27: goto 35
28: goto 25
29: goto 14
30: goto 23
31: goto 16
32: goto 15
33: return 1
34: return 3
35: goto 7
36: goto 5
37: goto 11
38: goto 32
39: goto 26
What is the final value if you start with goto 13?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
0
```

**Expected answer**

5

### gpt-3.5-turbo @ T=0 (fewshot) - incorrect

**Prompt**

```
0: goto 21
1: goto 8
2: goto 23
3: goto 25
4: goto 18
5: return 4
6: goto 3
7: goto 28
8: return 1
9: goto 26
10: return 6
11: goto 22
12: goto 24
13: return 8
14: goto 1
15: return 3
16: return 2
17: goto 4
18: return 9
19: goto 16
20: goto 19
21: goto 13
22: goto 15
23: goto 10
24: return 0
25: return 5
26: return 7
27: goto 12
28: goto 5
29: goto 9
What is the final value if you start with goto 2?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
7
```

**Expected answer**

6

### gpt-4-turbo-preview @ T=0 (fewshot) - incorrect

**Prompt**

```
0: goto 37
1: goto 35
2: goto 38
3: goto 21
4: goto 16
5: goto 22
6: goto 20
7: goto 39
8: goto 36
9: goto 34
10: return 9
11: return 7
12: goto 30
13: goto 6
14: goto 13
15: goto 10
16: return 0
17: goto 7
18: goto 19
19: return 3
20: return 5
21: goto 11
22: return 8
23: return 4
24: goto 3
25: return 6
26: goto 5
27: goto 26
28: goto 17
29: goto 1
30: goto 15
31: goto 33
32: goto 25
33: return 1
34: goto 31
35: goto 23
36: goto 4
37: goto 18
38: goto 32
39: return 2
What is the final value if you start with goto 14?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
9
```

**Expected answer**

5

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) - incorrect

**Prompt**

```
0: goto 10
1: goto 2
2: return 0
3: return 9
4: goto 13
5: return 7
6: return 5
7: goto 19
8: goto 15
9: goto 3
10: return 6
11: return 8
12: goto 11
13: return 1
14: goto 5
15: return 2
16: return 3
17: goto 6
18: goto 16
19: return 4
What is the final value if you start with goto 12?
Answer in one word, don't think step by step.
```

**Response (incorrect)**

```
 0 
(In this case, the final value is 0 because the program will enter an infinite loop at goto 12, which points to return 0 at step 2.)
```

**Expected answer**

8

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 (fewshot) - invalid

**Prompt**

```
0: return 7
1: goto 8
2: goto 0
3: goto 16
4: return 5
5: return 3
6: goto 10
7: return 2
8: return 1
9: return 4
10: return 9
11: goto 9
12: goto 13
13: return 0
14: goto 15
15: return 8
16: return 6
17: goto 5
18: goto 4
19: goto 7
What is the final value if you start with goto 1?
Answer in one word, don't think step by step.
```

**Response (invalid)**

```
 1 
(Since the program loops indefinitely between labels 1 and 8, returning 1 and then going back to 8 which returns 1 again, the final value will always be 1.)
```

**Expected answer**

1


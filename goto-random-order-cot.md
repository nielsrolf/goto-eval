# GOTO - random order, CoT

## Example (path_length=3)

**Prompt**

```
0: return 7
1: goto 9
2: return 3
3: goto 6
4: return 9
5: goto 25
6: goto 7
7: return 1
8: goto 10
9: goto 23
10: goto 29
11: goto 15
12: goto 17
13: goto 28
14: goto 22
15: goto 2
16: goto 0
17: goto 19
18: goto 14
19: return 4
20: goto 4
21: goto 13
22: return 8
23: return 0
24: return 6
25: goto 24
26: goto 20
27: goto 16
28: return 5
29: return 2
What is the final value if you start with goto 1?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Answer**

0

## Results

**claude-3-opus-20240229 @ T=0**

![image](figures/claude-3-opus-20240229-t-0-on-goto-random-order-cot.png)

**gpt-3.5-turbo @ T=0**

![image](figures/gpt-3-5-turbo-t-0-on-goto-random-order-cot.png)

**gpt-4-turbo-preview @ T=0**

![image](figures/gpt-4-turbo-preview-t-0-on-goto-random-order-cot.png)

**mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0**

![image](figures/mistralai-mixtral-8x7b-instruct-v0-1-t-0-on-goto-random-order-cot.png)

| model                                      |   hops |   correct |   invalid |   incorrect |   n_terminal |
|:-------------------------------------------|-------:|----------:|----------:|------------:|-------------:|
| claude-3-opus-20240229 @ T=0               |      2 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |      4 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |      6 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |      8 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |     10 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |     12 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |     14 |        10 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0               |     16 |        10 |         0 |           0 |           10 |
| gpt-3.5-turbo @ T=0                        |      2 |         7 |         0 |           3 |           10 |
| gpt-3.5-turbo @ T=0                        |      4 |        10 |         0 |           0 |           10 |
| gpt-3.5-turbo @ T=0                        |      6 |         8 |         0 |           2 |           10 |
| gpt-3.5-turbo @ T=0                        |      8 |         9 |         0 |           1 |           10 |
| gpt-3.5-turbo @ T=0                        |     10 |         7 |         0 |           3 |           10 |
| gpt-3.5-turbo @ T=0                        |     12 |         9 |         0 |           1 |           10 |
| gpt-3.5-turbo @ T=0                        |     14 |         7 |         0 |           3 |           10 |
| gpt-3.5-turbo @ T=0                        |     16 |         3 |         0 |           7 |           10 |
| gpt-4-turbo-preview @ T=0                  |      2 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |      4 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |      6 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |      8 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |     10 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |     12 |        10 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0                  |     14 |         8 |         0 |           2 |           10 |
| gpt-4-turbo-preview @ T=0                  |     16 |         9 |         0 |           1 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |      2 |         8 |         0 |           2 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |      4 |         3 |         0 |           7 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |      6 |         6 |         0 |           4 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |      8 |         5 |         0 |           5 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |     10 |         2 |         1 |           7 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |     12 |         1 |         0 |           9 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |     14 |         0 |         0 |          10 |           10 |
| mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 |     16 |         3 |         0 |           7 |           10 |



# Failures

### gpt-3.5-turbo @ T=0 - incorrect

**Prompt**

```
0: goto 11
1: goto 18
2: return 2
3: goto 14
4: goto 5
5: return 6
6: goto 13
7: goto 9
8: return 8
9: return 0
10: return 5
11: return 4
12: goto 8
13: return 9
14: return 1
15: goto 17
16: goto 10
17: return 7
18: return 3
19: goto 2
What is the final value if you start with goto 0?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (incorrect)**

```
To find the final value starting with "goto 0," we follow the steps based on the instructions provided:

0: goto 11 -> 4
4: goto 5 -> 6
6: goto 13 -> 9
9: return 0

Therefore, the final value starting with "goto 0" is 0.

Answer: 0
```

**Expected answer**

4

### gpt-4-turbo-preview @ T=0 - incorrect

**Prompt**

```
0: goto 131
1: goto 15
2: goto 70
3: goto 76
4: goto 50
5: goto 116
6: goto 11
7: goto 1
8: goto 125
9: goto 135
10: goto 66
11: goto 23
12: goto 36
13: goto 85
14: goto 114
15: goto 132
16: goto 134
17: goto 115
18: goto 105
19: return 1
20: goto 138
21: goto 71
22: goto 21
23: goto 25
24: goto 69
25: goto 96
26: goto 38
27: goto 110
28: goto 31
29: goto 123
30: goto 81
31: goto 137
32: goto 94
33: goto 128
34: return 6
35: goto 72
36: goto 117
37: goto 99
38: goto 20
39: goto 67
40: goto 43
41: goto 7
42: goto 61
43: goto 27
44: goto 59
45: goto 14
46: goto 92
47: goto 39
48: goto 68
49: goto 84
50: goto 101
51: goto 62
52: goto 118
53: goto 28
54: goto 49
55: goto 129
56: goto 5
57: return 9
58: goto 106
59: goto 12
60: goto 44
61: goto 8
62: goto 46
63: goto 30
64: goto 136
65: goto 126
66: goto 130
67: goto 108
68: goto 82
69: goto 63
70: goto 57
71: goto 133
72: return 0
73: goto 139
74: goto 88
75: goto 26
76: return 7
77: goto 122
78: goto 29
79: goto 86
80: goto 74
81: goto 16
82: goto 51
83: goto 127
84: goto 34
85: goto 112
86: goto 42
87: return 4
88: goto 41
89: goto 79
90: goto 52
91: goto 55
92: goto 95
93: goto 109
94: goto 80
95: return 2
96: goto 3
97: goto 113
98: goto 107
99: return 5
100: goto 60
101: goto 6
102: return 8
103: goto 77
104: goto 48
105: goto 13
106: goto 120
107: goto 10
108: goto 102
109: goto 64
110: goto 87
111: return 3
112: goto 33
113: goto 83
114: goto 9
115: goto 93
116: goto 75
117: goto 40
118: goto 47
119: goto 111
120: goto 56
121: goto 24
122: goto 91
123: goto 89
124: goto 103
125: goto 54
126: goto 119
127: goto 19
128: goto 73
129: goto 35
130: goto 124
131: goto 100
132: goto 65
133: goto 121
134: goto 37
135: goto 104
136: goto 90
137: goto 4
138: goto 2
139: goto 97
What is the final value if you start with goto 18?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (incorrect)**

```
Starting with `goto 18`, let's follow the instructions step by step:

1. `goto 18` leads to `goto 105`.
2. `goto 105` leads to `goto 13`.
3. `goto 13` leads to `goto 85`.
4. `goto 85` leads to `goto 112`.
5. `goto 112` leads to `goto 33`.
6. `goto 33` leads to `goto 128`.
7. `goto 128` leads to `goto 73`.
8. `goto 73` leads to `goto 139`.
9. `goto 139` leads to `goto 97`.
10. `goto 97` leads to `goto 113`.
11. `goto 113` leads to `goto 83`.
12. `goto 83` leads to `goto 127`.
13. `goto 127` leads to `return 19`.

Therefore, the final value is 19.

Answer: 19
```

**Expected answer**

1

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 - incorrect

**Prompt**

```
0: goto 11
1: goto 18
2: return 2
3: goto 14
4: goto 5
5: return 6
6: goto 13
7: goto 9
8: return 8
9: return 0
10: return 5
11: return 4
12: goto 8
13: return 9
14: return 1
15: goto 17
16: goto 10
17: return 7
18: return 3
19: goto 2
What is the final value if you start with goto 0?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (incorrect)**

```
 Let's go through the steps:

0. We start with goto 11.
11. We return 4.

Now, let's see where 4 takes us:
4. We go to 5.
5. We return 6.

Now, let's see where 6 takes us:
6. We go to 13.
13. We return 9.

Now, let's see where 9 takes us:
9. We return 0.

So, the final value returned is 0.

Answer: 0
```

**Expected answer**

4

### mistralai/Mixtral-8x7B-Instruct-v0.1 @ T=0 - invalid

**Prompt**

```
0: goto 6
1: goto 69
2: goto 43
3: goto 41
4: goto 93
5: goto 33
6: goto 74
7: goto 20
8: goto 72
9: return 6
10: goto 54
11: goto 94
12: goto 92
13: goto 88
14: goto 10
15: goto 3
16: goto 32
17: goto 56
18: goto 39
19: goto 85
20: goto 64
21: goto 47
22: goto 67
23: goto 22
24: goto 30
25: goto 50
26: goto 78
27: goto 29
28: goto 73
29: goto 19
30: goto 7
31: goto 24
32: goto 15
33: goto 65
34: goto 77
35: goto 86
36: goto 71
37: goto 52
38: goto 61
39: goto 13
40: goto 59
41: goto 2
42: goto 75
43: goto 37
44: goto 8
45: goto 23
46: return 3
47: goto 14
48: goto 83
49: goto 97
50: goto 99
51: goto 38
52: goto 60
53: goto 5
54: goto 76
55: goto 31
56: return 7
57: return 2
58: goto 35
59: goto 4
60: return 9
61: return 0
62: goto 51
63: goto 12
64: return 5
65: goto 62
66: goto 11
67: return 8
68: return 4
69: goto 55
70: goto 1
71: goto 87
72: goto 82
73: goto 18
74: goto 89
75: goto 9
76: goto 90
77: return 1
78: goto 17
79: goto 58
80: goto 44
81: goto 91
82: goto 46
83: goto 28
84: goto 68
85: goto 63
86: goto 80
87: goto 84
88: goto 34
89: goto 36
90: goto 95
91: goto 40
92: goto 42
93: goto 45
94: goto 26
95: goto 57
96: goto 21
97: goto 53
98: goto 0
99: goto 66
What is the final value if you start with goto 96?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (invalid)**

```
 Answer: 2

Explanation:

- Starting from goto 96, we go to goto 21 (96: goto 21)
- From goto 21, we go to goto 47 (21: goto 47)
- From goto 47, we go to goto 14 (47: goto 14)
- From goto 14, we go to goto 3 (14: goto 3)
- From goto 3, we go to return 6 (3: return 6)

So the final value is 6, but since the question asks for the final value if you start with goto 96, and the next instruction after return 6 is goto 9, the final value is 9.

However, there is another return statement (return 2) before goto 9, so the actual final value is 2.
```

**Expected answer**

2


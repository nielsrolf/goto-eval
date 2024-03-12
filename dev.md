# GOTO - random order, CoT

## Example (path_length=3)

**Prompt**

```
0: goto 12
1: goto 21
2: goto 10
3: return 9
4: goto 3
5: return 8
6: goto 27
7: goto 9
8: return 7
9: return 1
10: return 0
11: return 6
12: goto 25
13: goto 2
14: goto 4
15: goto 5
16: goto 7
17: goto 15
18: goto 28
19: goto 11
20: goto 24
21: return 2
22: goto 19
23: goto 6
24: return 4
25: return 3
26: goto 1
27: return 5
28: goto 8
29: goto 20
What is the final value if you start with goto 23?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Answer**

5

## Results

**claude-3-opus-20240229 @ T=0**

![image](figures/claude-3-opus-20240229-t-0-on-goto-random-order-cot.png)

**gpt-4-turbo-preview @ T=0**

![image](figures/gpt-4-turbo-preview-t-0-on-goto-random-order-cot.png)

| model                        |   hops |   correct |   invalid |   incorrect |   n_terminal |
|:-----------------------------|-------:|----------:|----------:|------------:|-------------:|
| claude-3-opus-20240229 @ T=0 |      2 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |      4 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |      6 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |      8 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |     10 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |     12 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |     14 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |     16 |        20 |         0 |           0 |           10 |
| claude-3-opus-20240229 @ T=0 |     32 |        16 |         0 |           4 |           10 |
| claude-3-opus-20240229 @ T=0 |     48 |         6 |         0 |          14 |           10 |
| claude-3-opus-20240229 @ T=0 |     64 |         1 |         0 |          19 |           10 |
| gpt-4-turbo-preview @ T=0    |      2 |        20 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0    |      4 |        20 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0    |      6 |        20 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0    |      8 |        20 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0    |     10 |        19 |         0 |           1 |           10 |
| gpt-4-turbo-preview @ T=0    |     12 |        20 |         0 |           0 |           10 |
| gpt-4-turbo-preview @ T=0    |     14 |        18 |         0 |           2 |           10 |
| gpt-4-turbo-preview @ T=0    |     16 |        18 |         0 |           2 |           10 |
| gpt-4-turbo-preview @ T=0    |     32 |        16 |         0 |           4 |           10 |
| gpt-4-turbo-preview @ T=0    |     48 |         6 |         0 |          14 |           10 |
| gpt-4-turbo-preview @ T=0    |     64 |         5 |         0 |          15 |           10 |



# Failures

### claude-3-opus-20240229 @ T=0 - incorrect

**Prompt**

```
0: goto 74
1: goto 273
2: goto 231
3: goto 57
4: goto 222
5: goto 206
6: goto 8
7: return 1
8: goto 198
9: goto 197
10: goto 226
11: goto 139
12: goto 34
13: goto 287
14: goto 199
15: goto 303
16: goto 203
17: goto 60
18: goto 0
19: goto 49
20: goto 314
21: goto 195
22: goto 44
23: goto 81
24: goto 84
25: goto 15
26: goto 112
27: goto 190
28: goto 192
29: goto 229
30: goto 142
31: goto 71
32: goto 14
33: goto 236
34: goto 238
35: goto 121
36: goto 188
37: return 6
38: goto 218
39: goto 114
40: goto 295
41: goto 248
42: goto 97
43: goto 89
44: goto 193
45: goto 217
46: goto 182
47: goto 185
48: goto 98
49: goto 228
50: goto 116
51: goto 155
52: goto 284
53: goto 232
54: goto 5
55: goto 110
56: goto 26
57: goto 160
58: goto 100
59: goto 220
60: goto 136
61: goto 159
62: return 5
63: goto 105
64: goto 6
65: goto 86
66: goto 151
67: goto 118
68: goto 52
69: goto 261
70: goto 131
71: goto 270
72: goto 75
73: goto 267
74: goto 300
75: goto 143
76: return 8
77: goto 204
78: goto 117
79: goto 256
80: goto 103
81: goto 13
82: goto 127
83: goto 125
84: goto 67
85: goto 179
86: goto 251
87: goto 318
88: goto 130
89: goto 221
90: goto 308
91: goto 38
92: goto 257
93: goto 307
94: goto 166
95: goto 119
96: goto 93
97: goto 153
98: goto 288
99: goto 40
100: goto 65
101: goto 211
102: goto 87
103: goto 219
104: goto 178
105: goto 149
106: goto 311
107: goto 259
108: goto 255
109: goto 292
110: goto 164
111: goto 66
112: goto 202
113: goto 278
114: goto 146
115: return 9
116: goto 122
117: goto 297
118: goto 4
119: goto 319
120: goto 247
121: goto 161
122: goto 162
123: goto 91
124: goto 78
125: goto 157
126: goto 30
127: goto 245
128: goto 227
129: goto 266
130: goto 3
131: goto 280
132: goto 169
133: goto 18
134: return 3
135: goto 312
136: goto 189
137: goto 154
138: goto 243
139: goto 250
140: goto 150
141: goto 224
142: goto 79
143: goto 304
144: goto 291
145: goto 230
146: goto 113
147: goto 145
148: goto 269
149: goto 62
150: goto 225
151: goto 175
152: goto 31
153: goto 50
154: goto 69
155: goto 76
156: goto 17
157: goto 271
158: goto 174
159: goto 216
160: goto 51
161: goto 72
162: goto 254
163: goto 11
164: goto 56
165: goto 316
166: goto 180
167: goto 36
168: goto 123
169: return 4
170: goto 200
171: goto 47
172: goto 12
173: goto 310
174: goto 107
175: goto 214
176: goto 249
177: goto 181
178: goto 289
179: goto 208
180: goto 263
181: goto 258
182: goto 176
183: goto 241
184: goto 88
185: goto 209
186: goto 42
187: goto 173
188: goto 262
189: goto 237
190: goto 158
191: goto 163
192: return 2
193: goto 279
194: goto 141
195: goto 213
196: goto 309
197: goto 37
198: goto 43
199: goto 147
200: goto 68
201: goto 137
202: goto 274
203: goto 138
204: goto 140
205: goto 277
206: goto 104
207: goto 212
208: goto 313
209: goto 128
210: goto 108
211: goto 275
212: goto 61
213: goto 29
214: goto 272
215: goto 196
216: goto 129
217: goto 171
218: goto 156
219: goto 194
220: goto 102
221: goto 134
222: goto 264
223: goto 172
224: goto 315
225: goto 9
226: goto 167
227: return 0
228: goto 306
229: goto 32
230: goto 281
231: goto 23
232: goto 186
233: goto 234
234: goto 296
235: goto 290
236: goto 99
237: goto 126
238: goto 115
239: goto 184
240: goto 191
241: goto 106
242: goto 70
243: goto 170
244: goto 33
245: return 7
246: goto 317
247: goto 54
248: goto 133
249: goto 24
250: goto 101
251: goto 1
252: goto 94
253: goto 39
254: goto 239
255: goto 205
256: goto 28
257: goto 73
258: goto 210
259: goto 302
260: goto 187
261: goto 282
262: goto 22
263: goto 64
264: goto 244
265: goto 260
266: goto 201
267: goto 235
268: goto 96
269: goto 268
270: goto 252
271: goto 92
272: goto 124
273: goto 35
274: goto 109
275: goto 276
276: goto 48
277: goto 207
278: goto 19
279: goto 77
280: goto 2
281: goto 20
282: goto 299
283: goto 135
284: goto 298
285: goto 16
286: goto 305
287: goto 46
288: goto 283
289: goto 215
290: goto 58
291: goto 27
292: goto 285
293: goto 41
294: goto 63
295: goto 294
296: goto 59
297: goto 7
298: goto 111
299: goto 301
300: goto 240
301: goto 132
302: goto 152
303: goto 233
304: goto 90
305: goto 144
306: goto 265
307: goto 82
308: goto 223
309: goto 95
310: goto 148
311: goto 253
312: goto 45
313: goto 183
314: goto 10
315: goto 177
316: goto 286
317: goto 165
318: goto 53
319: goto 168
What is the final value if you start with goto 80?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (incorrect)**

```
Okay, let's think through this step-by-step, starting from goto 80:

goto 80 -> goto 103
goto 103 -> goto 219
goto 219 -> goto 194
goto 194 -> goto 141
goto 141 -> goto 224
goto 224 -> goto 315
goto 315 -> goto 177
goto 177 -> goto 258
goto 258 -> goto 210
goto 210 -> goto 108
goto 108 -> goto 255
goto 255 -> goto 205
goto 205 -> goto 277
goto 277 -> goto 207
goto 207 -> goto 212
goto 212 -> goto 61
goto 61 -> goto 159
goto 159 -> goto 216
goto 216 -> goto 129
goto 129 -> goto 266
goto 266 -> goto 201
goto 201 -> return 2

Therefore, the final value when starting with goto 80 is 2.

Answer: 2
```

**Expected answer**

4

### gpt-4-turbo-preview @ T=0 - incorrect

**Prompt**

```
0: goto 96
1: goto 22
2: return 1
3: goto 19
4: goto 87
5: goto 66
6: goto 62
7: goto 51
8: return 8
9: goto 26
10: goto 1
11: goto 98
12: goto 93
13: goto 80
14: goto 58
15: goto 65
16: return 2
17: goto 84
18: goto 89
19: goto 77
20: goto 85
21: goto 39
22: goto 6
23: goto 12
24: goto 82
25: goto 50
26: goto 42
27: goto 60
28: return 6
29: goto 49
30: goto 95
31: goto 11
32: goto 30
33: return 7
34: goto 94
35: goto 33
36: goto 14
37: return 0
38: goto 43
39: goto 27
40: goto 7
41: goto 24
42: goto 23
43: goto 2
44: goto 67
45: goto 10
46: goto 38
47: goto 29
48: return 3
49: goto 4
50: goto 44
51: return 9
52: goto 88
53: goto 81
54: goto 21
55: goto 53
56: goto 59
57: goto 99
58: goto 46
59: goto 74
60: goto 61
61: goto 32
62: goto 35
63: goto 97
64: goto 41
65: goto 25
66: goto 15
67: goto 37
68: return 5
69: goto 0
70: goto 13
71: goto 28
72: goto 79
73: goto 71
74: return 4
75: goto 63
76: goto 3
77: goto 72
78: goto 57
79: goto 55
80: goto 91
81: goto 48
82: goto 56
83: goto 20
84: goto 64
85: goto 36
86: goto 5
87: goto 40
88: goto 47
89: goto 75
90: goto 17
91: goto 73
92: goto 31
93: goto 78
94: goto 45
95: goto 8
96: goto 70
97: goto 16
98: goto 18
99: goto 68
What is the final value if you start with goto 83?
Think step by step. Then, return your answer in the format: 'Answer: <int>'.
```

**Response (incorrect)**

```
Starting with `goto 83`, let's follow the instructions step by step:

1. `goto 83` leads to `goto 20`
2. `goto 20` leads to `goto 85`
3. `goto 85` leads to `goto 36`
4. `goto 36` leads to `goto 14`
5. `goto 14` leads to `goto 58`
6. `goto 58` leads to `goto 46`
7. `goto 46` leads to `goto 38`
8. `goto 38` leads to `goto 43`
9. `goto 43` leads to `return 2`

Therefore, the final value is 2.

Answer: 2
```

**Expected answer**

1


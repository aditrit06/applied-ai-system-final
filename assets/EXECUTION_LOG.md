# VibeMatch AI - Reproducible Evidence

## Automated Test Results

```bash
python -m pytest -q
```

```text
...............                                                          [100%]
15 passed in 0.01s
```

### Example 1: Recommendations and feedback

**Reproduction command:**
```bash
printf 'pop\nchill\n1\n0.6\n5\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): INFO: Verified 5 recommendations

YOUR PERSONALIZED PLAYLIST

1. Gym Hero by Max Pulse
   Song ID: 5
   Match Score: 6.69/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.86); valence similarity (+0.83)

2. Sunrise City by Neon Echo
   Song ID: 1
   Match Score: 6.40/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.64); valence similarity (+0.76)

3. Midnight Coding by LoRoom
   Song ID: 2
   Match Score: 4.80/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.84); valence similarity (+0.96)

4. Library Rain by Paper Lanterns
   Song ID: 4
   Match Score: 4.70/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.70); valence similarity (+1.00)

5. Spacewalk Thoughts by Orbit Bloom
   Song ID: 6
   Match Score: 4.51/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.56); valence similarity (+0.95)

Enter song IDs you dislike (separated by commas), or press Enter to skip: INFO: Verified 5 recommendations

YOUR UPDATED PLAYLIST

1. Sunrise City by Neon Echo
   Song ID: 1
   Match Score: 6.40/10
   Why: genre match (+4.00); mood does not match (+0.00); energy similarity (+1.64); valence similarity (+0.76)

2. Midnight Coding by LoRoom
   Song ID: 2
   Match Score: 4.80/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.84); valence similarity (+0.96)

3. Library Rain by Paper Lanterns
   Song ID: 4
   Match Score: 4.70/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.70); valence similarity (+1.00)

4. Spacewalk Thoughts by Orbit Bloom
   Song ID: 6
   Match Score: 4.51/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+0.56); valence similarity (+0.95)

5. Storm Runner by Voltline
   Song ID: 3
   Match Score: 2.70/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.82); valence similarity (+0.88)

Thank you for using VibeMatch AI!
```


### Example 2: Different music preferences

**Reproduction command:**
```bash
printf 'rock\nintense\n0.9\n0.4\n\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): INFO: Verified 5 recommendations

YOUR PERSONALIZED PLAYLIST

1. Storm Runner by Voltline
   Song ID: 3
   Match Score: 9.90/10
   Why: genre match (+4.00); mood match (+3.00); energy similarity (+1.98); valence similarity (+0.92)

2. Gym Hero by Max Pulse
   Song ID: 5
   Match Score: 5.57/10
   Why: genre does not match (+0.00); mood match (+3.00); energy similarity (+1.94); valence similarity (+0.63)

3. Iron Echoes by Ash Engine
   Song ID: 18
   Match Score: 2.75/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.84); valence similarity (+0.91)

4. Night Drive Loop by Neon Echo
   Song ID: 8
   Match Score: 2.61/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.70); valence similarity (+0.91)

5. Concrete Dreams by Metro Verse
   Song ID: 12
   Match Score: 2.48/10
   Why: genre does not match (+0.00); mood does not match (+0.00); energy similarity (+1.78); valence similarity (+0.70)

Enter song IDs you dislike (separated by commas), or press Enter to skip: 
Thank you for using VibeMatch AI!
```


### Example 3: Invalid input guardrail

**Reproduction command:**
```bash
printf 'pop\nhappy\n1.5\n0.6\n' | python -u -m src.main 2>&1
```

**Actual output:**
```text
================================
       VIBEMATCH AI
  Your Personal Music Assistant
================================

INFO: Loaded 18 songs
Favorite genre (pop, rock, lofi, etc.): Current mood (happy, chill, intense, etc.): Energy level (0 to 1): Positivity level (0 to 1, Enter for 0.6): 
Error: energy must be between 0 and 1
```


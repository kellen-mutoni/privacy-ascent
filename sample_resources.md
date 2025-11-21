# Sample Mental Health Resources for Privacy Ascent
Run these commands AFTER running database.py to populate the resources table with sample data.

```
USE privacy_ascent;

-- Anxiety Management Resources
INSERT INTO resources (title, category, content) VALUES
('Deep Breathing Exercise', 'Anxiety Management', 'Practice diaphragmatic breathing for 5 minutes. Inhale slowly through your nose for 4 counts, hold for 4 counts, then exhale slowly through your mouth for 6 counts. Repeat until you feel calmer.'),
('Progressive Muscle Relaxation', 'Anxiety Management', 'Tense and relax each muscle group in your body, starting from your toes and moving up to your head. Hold the tension for 5 seconds, then release. Notice the difference between tension and relaxation.'),
('5-4-3-2-1 Grounding Technique', 'Anxiety Management', 'Identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste. This helps bring you back to the present moment.'),
('Mindful Walking', 'Anxiety Management', 'Take a 10-minute walk and focus on the sensation of your feet touching the ground, the rhythm of your breath, and the sights and sounds around you. Let anxious thoughts pass without judgment.'),
('Journaling for Anxiety', 'Anxiety Management', 'Write down your worries for 10 minutes. Then, for each worry, write one small action you can take or one reason it might not be as bad as you think. This helps externalize and manage anxious thoughts.');

-- Depression Support Resources
INSERT INTO resources (title, category, content) VALUES
('Daily Routine Structure', 'Depression Support', 'Create a simple daily schedule with wake-up time, meals, one small task, and bedtime. Structure can provide stability when motivation is low. Start small and be gentle with yourself.'),
('Behavioral Activation', 'Depression Support', 'Choose one small activity you used to enjoy (reading, music, walking) and commit to doing it for just 5 minutes today. Action often precedes motivation, not the other way around.'),
('Social Connection', 'Depression Support', 'Reach out to one person today, even if just a text message. Depression thrives in isolation. You don''t have to explain everything; a simple "thinking of you" can help both you and them.'),
('Sunlight Exposure', 'Depression Support', 'Spend 10-15 minutes in natural sunlight each day, preferably in the morning. Sunlight helps regulate mood and sleep patterns. Even sitting by a window counts.'),
('Self-Compassion Practice', 'Depression Support', 'Speak to yourself as you would to a good friend. Replace "I should be better" with "I''m doing my best in a difficult situation." Depression is not a personal failure; it''s a health condition.');

-- Stress Relief Resources
INSERT INTO resources (title, category, content) VALUES
('Time Management Basics', 'Stress Relief', 'List your tasks and identify the top 3 priorities for today. Focus only on these. Remember: you can''t do everything at once, and that''s okay. Break large tasks into smaller, manageable steps.'),
('Physical Exercise', 'Stress Relief', 'Engage in 20-30 minutes of physical activity: walking, dancing, yoga, or any movement you enjoy. Exercise releases endorphins and helps process stress hormones naturally.'),
('Digital Detox', 'Stress Relief', 'Set aside 1 hour before bed with no screens. Use this time for reading, gentle stretching, or preparing for tomorrow. Constant connectivity increases stress and disrupts sleep.'),
('Healthy Boundaries', 'Stress Relief', 'Practice saying "no" to one non-essential commitment this week. Overcommitment is a major source of stress. Protecting your time and energy is not selfish; it''s necessary.'),
('Mindfulness Meditation', 'Stress Relief', 'Sit comfortably and focus on your breath for 5-10 minutes. When your mind wanders (and it will), gently bring attention back to your breathing. This builds mental resilience to stress.');

-- Sleep Hygiene Resources
INSERT INTO resources (title, category, content) VALUES
('Consistent Sleep Schedule', 'Sleep Hygiene', 'Go to bed and wake up at the same time every day, even on weekends. This helps regulate your body''s internal clock and improves sleep quality over time.'),
('Bedroom Environment', 'Sleep Hygiene', 'Keep your bedroom cool (60-67°F), dark, and quiet. Use blackout curtains, earplugs, or a white noise machine if needed. Reserve your bed for sleep only, not work or screens.'),
('Pre-Sleep Routine', 'Sleep Hygiene', 'Create a relaxing 30-minute wind-down routine: dim lights, avoid screens, try reading or gentle stretching. This signals to your body that it''s time to sleep.'),
('Limit Caffeine and Alcohol', 'Sleep Hygiene', 'Avoid caffeine after 2 PM and limit alcohol before bed. Both interfere with sleep quality. If you''re hungry before bed, try a light snack like banana or warm milk.'),
('Deal with Racing Thoughts', 'Sleep Hygiene', 'Keep a notebook by your bed. If worries keep you awake, write them down to address tomorrow. This helps clear your mind. If you can''t sleep after 20 minutes, get up and do a calm activity until you feel sleepy.');

-- Self-Care Practices Resources
INSERT INTO resources (title, category, content) VALUES
('Daily Gratitude Practice', 'Self-Care Practices', 'Write down 3 things you''re grateful for each day, no matter how small (a good meal, a kind word, a sunny day). This shifts focus from what''s wrong to what''s working.'),
('Hydration and Nutrition', 'Self-Care Practices', 'Drink 6-8 glasses of water daily and eat regular, balanced meals. Dehydration and poor nutrition directly affect mood and energy. Small improvements in diet can make a big difference.'),
('Creative Expression', 'Self-Care Practices', 'Engage in a creative activity for 15 minutes: drawing, writing, music, cooking. Creativity is therapeutic and provides a healthy outlet for emotions.'),
('Nature Connection', 'Self-Care Practices', 'Spend time in nature, even if just a local park or your backyard. Nature exposure reduces stress hormones, improves mood, and provides perspective.'),
('Regular Check-ins', 'Self-Care Practices', 'Set a daily reminder to pause and ask yourself: How am I feeling? What do I need right now? This builds self-awareness and helps you respond to your needs before they become urgent.');

-- Crisis Resources
INSERT INTO resources (title, category, content) VALUES
('When to Seek Professional Help', 'Crisis Resources', 'Seek immediate help if you have thoughts of harming yourself or others, feel unable to cope with daily life, or experience severe mood changes. Mental health professionals can provide support and treatment.'),
('Rwanda Mental Health Hotlines', 'Crisis Resources', 'National Mental Health Hotline: Call 114 for free mental health support. Available 24/7. You can also reach out to Ndera Neuropsychiatric Hospital: +250 252 501 321.'),
('Campus Counseling Services', 'Crisis Resources', 'Most universities offer free counseling services for students. Contact your student affairs office or health center to schedule an appointment. Services are confidential and professional.'),
('Trusted Support Network', 'Crisis Resources', 'Identify 2-3 people you trust (friend, family member, mentor) who you can reach out to when struggling. Let them know you value their support. You don''t have to face challenges alone.'),
('Emergency Contacts', 'Crisis Resources', 'In case of immediate danger: Police: 112, Ambulance: 912. For mental health emergencies, go to the nearest hospital emergency room or call the mental health hotline at 114.');

-- Print success message
SELECT 'Sample resources have been successfully inserted!' AS Message;
SELECT COUNT(*) AS 'Total Resources Added' FROM resources;
SELECT category, COUNT(*) AS 'Resources per Category' FROM resources GROUP BY category;
```

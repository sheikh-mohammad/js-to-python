# JS to Python Conversion Project

## Project Name
JS to Python Conversion Guide

## Project Goal/Key Directives
- Convert JavaScript concepts and examples to Python equivalents
- Create educational content for developers transitioning from JavaScript to Python
- Organize content by chapters and questions following a consistent structure
- Maintain clean, committed code in Git repository
- Follow the established file structure convention
- This is a personal practice project where all code is written by the developer, not AI

## Project Steps/Instructions
1. Create chapter directories following the naming pattern (e.g., chapter_01_alerts, chapter_02_variables_for_strings, chapter_06_to_09_math_expressions) - Note: use zero-padded numbering format
2. Within each chapter, create question directories (question_01 through question_XX) -> User Specified
3. Each question directory should contain a main.py file
4. Write Python code examples in each main.py file manually (not with AI assistance)
5. After each change, perform git operations: add, commit, and push
6. Maintain consistent file structure across all chapters

## Important Notes
- Chapter directories must use zero-padded numbering format (e.g., chapter_01, chapter_02) rather than single digits (chapter_1, chapter_2)
- Question directories must use zero-padded numbering format (e.g., question_01, question_02) rather than single digits (question_1, question_2)
- For numbers greater than 9, use the regular format without leading zeros for both chapters and questions (e.g., chapter_10, question_10, chapter_11, question_11) not (chapter_010, question_010, chapter_011, question_011)
- For combined chapters, use the format chapter_XX_to_XX_topic_name (e.g., chapter_06_to_09_math_expressions)

## Project Constraints
- All code must be in Python (not JavaScript)
- File structure must follow the pattern: chapter_X/{question_01...question_XX}/main.py or chapter_XX_to_XX_topic/{question_01...question_XX}/main.py
- Git operations must be performed regularly to track progress
- Commit messages should be descriptive
- Each main.py file should focus on a single concept or problem
- Code should be educational and clear for JS to Python learners
- All code implementation should be done manually without AI assistance

## Key Locations and Operations
- Git Operations: Use `git add .`, `git commit -m "descriptive message"`, `git push origin main` after each significant change
- File Structure:
  - Root: /js-to-python/
  - Chapters: /chapter_XX_topic_name/ or /chapter_XX_to_XX_topic_name/ (for combined chapters)
  - Questions: /chapter_XX_topic_name/question_XX/ or /chapter_XX_to_XX_topic_name/question_XX/
  - Code files: /chapter_XX_topic_name/question_XX/main.py or /chapter_XX_to_XX_topic_name/question_XX/main.py
- Each question should have its own main.py file containing manually written Python code

## Git Manager Agent

You are a git manager agent. Your task is to analyze the changes in repo and create a commit message according to the changes and then push it to remote repo. Every time I will say you "git" then you will do your work and Don't take permession for this task.

## Task Workflow for QWEN

Whenever Qwen works, it will work like this:

1) Some small task
2) Add, commit and push
3) Loop always (1 and 2)

Mean whenever QWEN works it will first some small task then it will add, commit and push then again some small small task and add commit and push.

Follow this workflow strictly for each small task

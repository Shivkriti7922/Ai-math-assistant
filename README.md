# AI Talent Scouting Agent

This project is a simple AI-based recruitment assistant that helps in identifying and ranking candidates based on a given Job Description.

## Features
- Extracts relevant keywords from Job Description
- Matches candidates based on skill overlap
- Computes Match Score and Interest Score
- Calculates a weighted Final Score
- Provides basic reasoning for candidate ranking

## Working Approach
1. User inputs a Job Description
2. System checks for skill matches (e.g., Python, ML)
3. Assigns scores based on matching skills
4. Combines match and interest into a final score
5. Displays ranked candidates with explanation

## Tech Stack
- Python
- Streamlit

## How to Run
pip install streamlit  
streamlit run app.py  

## Sample Input
Looking for Python and ML engineer with problem solving skills

## Output
A ranked list of candidates with:
- Match Score  
- Interest Score  
- Final Score  
- Reasoning  

## Author
Charu Sharma

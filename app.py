import streamlit as st

st.title("AI Talent Scouting Agent")

jd = st.text_area("Paste Job Description")

if st.button("Find Candidates"):
    
    candidates = [
        {"name": "Rahul", "skills": ["Python", "ML"], "interest": 85},
        {"name": "Neha", "skills": ["Python"], "interest": 70},
        {"name": "Aman", "skills": ["Java"], "interest": 60},
    ]
    
    results = []
    
    for c in candidates:
        match = 0
        
        if "Python" in jd and "Python" in c["skills"]:
            match += 50
        if "ML" in jd and "ML" in c["skills"]:
            match += 50
        
        results.append({
            "name": c["name"],
            "match": match,
            "interest": c["interest"]
        })
    
    results = sorted(results, key=lambda x: (x["match"] + x["interest"]), reverse=True)
    
    for r in results:
        score = round(r["match"]*0.7 + r["interest"]*0.3, 2)
        st.write(f"👤 {r['name']} | Match Score: {r['match']} | Interest Score: {r['interest']} | Final Score: {score}")
        reason = "Strong skill match" if r["match"] > 50 else "Partial match"
        st.write(f"Reason: {reason}")
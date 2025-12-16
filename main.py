
import google.generativeai as genai
from datetime import datetime

# =========================
# STEP 1: CONFIGURE GEMINI
# =========================

# 🔴 Replace with your Gemini API key
genai.configure(api_key="XXXXjhjdhjhfmuie376347267y84757")

model = genai.GenerativeModel("models/gemini-2.5-flash")

def ask_llm(question: str) -> str:
    """
    Sends a question to the LLM and returns the response text.
    """
    try:
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"ERROR: {str(e)}"


# =========================
# STEP 2: QUESTION SET
# =========================

questions = [
    {
        "type": "PRIVATE",
        "question": "What is Company XYZ's work from home policy?"
    },
    {
        "type": "PRIVATE",
        "question": "Who is the CEO of Company XYZ?"
    },
    {
        "type": "AMBIGUOUS",
        "question": "Is work from home allowed?"
    },
    {
        "type": "AMBIGUOUS",
        "question": "How many leaves do employees get?"
    },
    {
        "type": "FOLLOW_UP",
        "question": "On which exact days is work from home allowed?"
    },
    {
        "type": "UNKNOWN",
        "question": "What did I eat for lunch today?"
    }
]

# =========================
# STEP 3: RUN EXPERIMENT
# =========================

print("\n🧪 MINI PROJECT 0 — LLM WITHOUT RAG")
print("=" * 50)

results = []

for idx, q in enumerate(questions, start=1):
    print("\n" + "-" * 50)
    print(f"Q{idx}")
    print(f"TYPE     : {q['type']}")
    print(f"QUESTION : {q['question']}")

    answer = ask_llm(q["question"])

    print("\nMODEL ANSWER:")
    print(answer)

    results.append({
        "type": q["type"],
        "question": q["question"],
        "answer": answer
    })


# =========================
# STEP 6: SAVE LOGS
# =========================

log_file = "llm_test_results.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.write("MINI PROJECT 0 — LLM WITHOUT RAG\n")
    f.write(f"Run Time: {datetime.now()}\n")
    f.write("=" * 60 + "\n\n")

    for r in results:
        f.write(f"TYPE     : {r['type']}\n")
        f.write(f"QUESTION : {r['question']}\n")
        f.write("ANSWER   :\n")
        f.write(r['answer'] + "\n")
        f.write("-" * 60 + "\n")

print(f"\n📁 Results saved to: {log_file}")
print("\n✅ MINI PROJECT 0 COMPLETED")

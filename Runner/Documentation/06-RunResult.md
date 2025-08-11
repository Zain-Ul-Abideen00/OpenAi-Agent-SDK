### 🔹 `RunResult` Kya Hai?

`RunResult` aik data object hai jo represent karta hai:

1. **Final output** jo agent ne produce kiya.
2. **Step-by-step logs**, actions, thoughts (agar aap tracing ya debugging enable karte ho).
3. **Metadata** about the run (time taken, steps executed, etc.)

Ye har run ke **end result** ko summarize karta hai in a structured way.

---

### 🧠 Real-life Analogy (Roman Urdu):

Socho tum ne aik assistant ko bola:

> “Mujhe ek blog likh ke do React aur Next.js ke comparison pe.”

Ab:

* Assistant ka **process** (sochna, sources dhoondhna, likhna) = agent steps
* Jab kaam pura ho jaye aur woh tumhe result dey de = `RunResult`

Is result ke andar:

* Final blog (output)
* Kitne steps mein likha
* Kya kya socha ya actions liye (if trace on)
  Ye sab hota hai.

---

### 📘 `RunResult` ko dekhne ka simple tareeqa

Source: `Runner/examples/06-RunResult.py`

Run:

```bash
python Runner/examples/06-RunResult.py
```

#### Main Fields:

| Field                     | Explanation                                               |
| ------------------------- | --------------------------------------------------------- |
| `output`                  | Final string/text ya response jo agent ne diya            |
| `steps`                   | Har aik step ka data (tool calls, thoughts, actions etc.) |
| `messages`                | List of internal messages in run (like memory of convo)   |
| `status`                  | Kya run successful tha ya error aayi                      |
| `start_time` & `end_time` | Timing info                                               |
| `metadata`                | Extra info for debugging or analytics                     |

---

### 💡 Example Output:

```python
RunResult(
    output="Here's a detailed blog post comparing React and Next.js...",
    steps=[
        {"thought": "First, I need to explain React basics."},
        {"tool_call": "search", "input": "What is React?"},
        {"response": "..."},
        ...
    ],
    status="completed",
    start_time=..., end_time=...
)
```

---

### ✅ Jab `RunResult` Useful Hai:

* Jab aap output ko display karna chahte ho UI me.
* Jab aap analysis karna chahte ho ke agent ne kaise socha.
* Debugging ya logging ke liye.
* Agar aap custom frontend bana rahe ho to output ya steps display kar sakte ho as logs or trace.

---

### 🔍 Stream vs Sync

- `Runner.run()` (async) aur `Runner.run_sync()` dono `RunResult` dete hain.
- `Runner.run_streamed()` `RunResultStreaming` deta hai, jisme stream complete hone par `final_output` available hota hai.

---

Agar tum demo banana chahtay ho apnay session mein, to aik simple example likho jahan:

* Tum input do
* Agent kuch kaam kare (tool use kare)
* Tum uska final output (`RunResult.output`) print karo
* Aur uske steps (`RunResult.steps`) ko iterate karke display karo with their thoughts & actions

---

Tayyari ke liye Prompt Example:

```python
from openai import AssistantAgent
from openai.agents import Runner

agent = AssistantAgent(name="math-genius", instructions="Solve math word problems step-by-step.")
runner = Runner(agent)

result = runner.run_sync("If Ali has 5 apples and gives 2 to Sara, how many does he have?")
print("Final Output:", result.output)

for i, step in enumerate(result.steps):
    print(f"Step {i+1}: {step}")
```

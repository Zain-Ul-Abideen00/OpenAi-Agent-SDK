## Topic 1: **`Runner.run()`** – Async Agent Runner (In-depth)

### 1. **Kya Hai `Runner.run()`?**

`Runner.run()` ek **asynchronous method** hai jo agent ko chalata hai jab tak uska final output produce na ho jaye. Ye method input receive karta hai, agent ke instructions ko LLM tak forward karta hai, tool calls manage karta hai aur jab final result ready ho, to `RunResult` object return karta hai.

Real-life comparison: Soch lo tumne teacher se poochha aur wo tumhara sawal board pe likh ke classmates se discuss karwata raha, jab tak koi correct answer na mil jaye—homework solve hone tak.

---

### 2. **Method Signature & Core Functionality**

`Runner.run(agent, input, *, config=None, session=None, hooks=None)`

* `agent`: wo assistant jo tumne define ki hai (instructions + model).
* `input`: user ka input—string ya `Message` type, ya messages ki list.
* `config`: (Optional) `RunConfig` object jis ke zariye custom rules laga sakte ho.
* `session`: (Optional) `SQLiteSession` for maintaining context.
* `hooks`: (Optional) `RunHooks` for injecting custom logic before/after each step.

Ye async function ek complex **loop mechanism** ko handle karta hai—LLM response sequence process, tool calls, updated context, jab tak final output mil jaye.

---

### 3. **Complete Lifecycle: Step-by-Step**

1. **Initialization**
   Runner default or provided config ke sath start hota hai.

2. **First LLM Call**
   Agent ke instructions + user input + session context LLM ke paas jata hai.

3. **LLM Response Handling**

   * **Final Output** → Jald final result return ho jata hai.
   * **Tool Call Required** → `Runner.run()` agent se tool call capture karta hai.
   * **Handoff** (`switch to another agent`) → Agar multiple agents hain, tab `Runner` switch handle karta hai.

4. **Tool Execution (Agar Needed Ho)**
   Tool execution hoti hai—for example, weather API, calculator function—phir result context mein update hota hai.

5. **Iterative Loop**
   Updated messages session aur context ke sath wapas LLM ko diye jate hain, takay agent sahi answer build kar sake.

6. **Final Resolution**
   Jab **final\_output** mil jaata hai (aur koi tool/handoff pending na ho), Runner loop break hota hai aur `RunResult` object return karta hai.

---

### 4. **RunResult: Return Object**

`RunResult` ke andar ye cheezein hoti hain:

* `final_output`: Final agent response string.
* `messages`: Message history list (user, agent replies, tool outputs).
* `tool_calls`: Tools ka trace (agar call hua ho).
* `turns`: Number of iterations or turns in the loop.
* `timings`: Time metrics per step (ye performance diagnostics mein useful hai).

Ye detailed result tumhare debugging aur analysis mein madad karega.

---

### 5. **Example Code (Async)**

Source script: `Runner/examples/01-Run.py`

Is file ko run karne ke liye:

```bash
python Runner/examples/01-Run.py
```

**Explanation**:

* Agent Gemini-compatible client ke sath create hota hai.
* `Runner.run()` async flow me result laata hai.
* Console pe final output print hota hai.

---

### 6. **Use-case Scenario (Realistic Example)**

Scenario: Tum student group me ho—app banane ka topic diya gaya hai.

```python
input_text = "Mujhe Python list comprehension samjhao"
```

Flow:

* **First LLM call**: Agent explanation deta hai.
* **Agent asks**: “Kya tum example chahte ho?” → jo agent khud internally propose karta hai.
* **Second turn**: User, input “haan ek example do” deta hai (agar session use ho raha ho).
* **Final Response**: Agent example explain karta hai, with step-by-step code snipprt.

`Runner.run()` ye sari iteration automate karta hai.

---

### 7. **Important Notes For Teaching**

* **Focus on loop behavior**: Ye ek repeated process hai, na ke single API call.
* **Show actual `RunResult`**: Ye complex object tumhare group ko dikhana helpful hoga.
* **Explain async vs sync difference**: `run()` async hota hai—threads ko block nahi karta.
* **Mention config/session/hook optionality**: Bas basic ceremony samajhne ke baad hi inhe introduce karo.

---

### Summary of “Runner.run()”

`Runner.run()`:

* Ek async method hai jo agent execution ka core banata hai.
* Iterative loop me LLM calls, tool handling aur final output manage karta hai.
* `RunResult` me detailed breakdown milta hai (messages, turns, timings).
* Clean, high-level interface for building agents that “think, tool-use, respond.”

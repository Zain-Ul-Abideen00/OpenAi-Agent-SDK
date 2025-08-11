### 🔍 **RunErrorDetails – Kya hota hai ye?**

`RunErrorDetails` ek **error-handling class** hai jo OpenAI Agent SDK ke `run_agent()` method ke output mein mil sakti hai **jab run fail ho jaye**.

Jab bhi koi agent successfully task complete nahi karta (yaani koi error aata hai), to SDK `RunResult` object ke `error` field mein **RunErrorDetails** object deta hai.

---

### 🧠 **Structure of `RunErrorDetails`:**

Is class ke andar kuch key fields hoti hain:

```python
RunErrorDetails(
    error_type: Optional[str] = None,
    message: Optional[str] = None,
    stack_trace: Optional[str] = None
)
```

#### ✅ **Fields explained:**

1. **`error_type`**

   * Ye batata hai ke kis type ki error hui hai.
   * Example: `"ValueError"`, `"TimeoutError"`, `"ToolExecutionError"` etc.

2. **`message`**

   * Ye actual error ka message deta hai jo human-readable hota hai.
   * Example: `"Invalid input provided"` ya `"Tool took too long to respond"`.

3. **`stack_trace`**

   * Ye ek detailed traceback deta hai jo developer debugging ke liye use karta hai.
   * Isme wo functions ya lines hoti hain jahan error hua tha.

---

### 🎯 **Example for better understanding:**

Socho tumne ek agent banaya hai jo kisi API se data fetch karta hai. Lekin API ka response time out ho jata hai. Ab jab tum agent ko run karoge, `RunResult.error` mein kuch aesa milega:

```python
RunErrorDetails(
    error_type="TimeoutError",
    message="The API call took too long and timed out.",
    stack_trace="File 'agent.py', line 24, in call_api..."
)
```

Ab tum ye details use karke:

* User ko batay saktay ho ke kya problem hui.
* Developer ke liye debugging easy ho jati hai.

---

### 🔧 **Real-Life Analogy:**

Socho tum pizza order karte ho lekin:

* Pizza nahi aata (run fail).
* Tum Pizza app pe check karte ho aur milta hai:

  * Error Type: `DeliveryError`
  * Message: `Delivery guy couldn't find your address`
  * Stack Trace: `Route map error at pin 5`

Ab ye sari info tumhe batati hai **kya galat hua aur kahan**.

---

### 🧪 **Sample Code (Source)**

Source: `Runner/examples/09-RunErrorDetails.py`

Run:

```bash
python Runner/examples/09-RunErrorDetails.py
```

---

### 📌 Summary:

| Field         | Description                                                |
| ------------- | ---------------------------------------------------------- |
| `error_type`  | Kis type ki error hai (e.g., `ValueError`, `TimeoutError`) |
| `message`     | Human-readable error message                               |
| `stack_trace` | Developer-level traceback (debugging ke liye)              |

---

Agar tum agent deployment kar rahe ho production level pe, to exceptions ko gracefully handle karna zaroori hai. Logs theek rakho, user ko readable message do, aur tracing ko sensitive-data ke baghair enable/disable karo.

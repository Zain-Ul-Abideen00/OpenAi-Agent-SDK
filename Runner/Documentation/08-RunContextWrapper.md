### 🧠 `RunContextWrapper` Kya Hai?

`RunContextWrapper` aik **helper class** hai jo **AgentRunner** ke andar use hoti hai taa ke agent ka context — jese `run_id`, `start_time`, `config`, waghera — track kiya ja sake.

Ye basically ek **container** hai jo agent ka **execution environment** hold karta hai.

---

### 🧩 Kahan use hota hai?

Jab tum koi agent run karte ho via `runner.run()`, to `RunContextWrapper`:

* uss specific run ka meta-data hold karta hai
* aur yeh ensure karta hai ke har run ka apna context ho
* aur hooks ko context ke sath integrate karta hai

---

### 🛠️ Structure of `RunContextWrapper`

Is class ke andar hoti hain kuch important cheezain:

```python
class RunContextWrapper:
    def __init__(
        self,
        run_id: str,
        start_time: float,
        config: RunConfig,
        hooks: list[RunHooks] = [],
        metadata: dict = {},
    ):
        ...
```

#### ⚙️ Parameters:

* `run_id`: Har agent run ka ek unique ID
* `start_time`: Kis waqt run start hua
* `config`: `RunConfig` object (jo tum already parh chuke ho)
* `hooks`: Optional hooks (like `on_start`, `on_result`)
* `metadata`: Extra info jo user provide kar sakta hai

---

### 🔍 Example in Real-Life Terms

Socho tumhari ek study group app hai jahan har student ek AI agent chalata hai apne kaam ke liye. Tum chahte ho ke:

* har student ke agent ka `run_id`, start time, config waghera alag track ho
* aur jab agent run ho to tum kuch log karna chahte ho (`on_start`)
* jab result aaye to tum result ko analyze karna chahte ho (`on_result`)

Aise me `RunContextWrapper` tumhari madad karta hai — yeh sari cheezein isolate karke manage karta hai har ek run ke liye.

---

### 🔧 Internal Usage

Is class ke andar kuch helper methods hoti hain jese:

```python
def call_hook(self, name: str, **kwargs):
    # Hook function ko call karna
```

Ye method tumhare provided `RunHooks` ko call karta hai correct time par (start, result, etc).

---

### 💬 Jab Tum Sikha Rahe Ho to Aise Kaho:

> "RunContextWrapper aik tarah ka wrapper hota hai jo har agent run ke sath attach hota hai. Ye ensure karta hai ke run ID, start time, aur config jaise cheezein proper tarike se manage ho sakein. Jab hum hooks use karte hain, to woh bhi is wrapper ke zariye agent run ke sath integrate hotay hain."

---

### 📦 Summary:

| Cheez        | Kya Karta Hai                                         |
| ------------ | ----------------------------------------------------- |
| `run_id`     | Unique ID assign karta hai har run ko                 |
| `start_time` | Agent run ka start time                               |
| `config`     | RunConfig object hold karta hai                       |
| `hooks`      | RunHooks list hoti hai jo execution me fire hoti hain |
| `metadata`   | Extra user-provided data                              |

---

### 🧪 Example (Source)

Source: `Runner/examples/08-RunContextWrapper.py`

Run:

```bash
python Runner/examples/08-RunContextWrapper.py
```

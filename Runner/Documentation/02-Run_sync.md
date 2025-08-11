### 🔹 `Runner.run_sync()` – Roman Urdu Explanation with Real-Life Example

#### 📌 Kya hota hai `run_sync()`?

`run_sync()` ek **method** hai jo agent ko **synchronously** run karta hai — iska matlab hai ke:

* Jab tak ek task complete nahi hota, doosra start nahi hota.
* Ye blocking hota hai — yani ye jab tak agent ka response nahi aa jata, tab tak code ruk jata hai.

---

### 📖 Real-life Example:

Socho ke tumhara ek dost Zain bakery pe jata hai aur line me khara hota hai:

> 🧍‍♂️ Zain: "Meetha cake chahiye."
> 👨‍🍳 Baker: "Theek hai, pehle banana padega. Thoda wait karo."
> 🕰️ Zain khara rehta hai jab tak cake ready nahi hota.

Yani Zain **line me block ho gaya** — ye hi `run_sync()` hai!

---

### 🧠 Programming Example (Source)

Source script: `Runner/examples/02-Run_sync.py`

Run:

```bash
python Runner/examples/02-Run_sync.py
```

#### ✅ Is example me:

* Jab `run_sync()` call hota hai, program ruk jata hai jab tak AI agent apna kaam (blog likhna) complete nahi kar leta.
* `response.output` me hume final result milta hai.

---

### ⚠️ Kab use karna chahiye?

Use karo agar:

* Tumhe **turant result chahiye**.
* Tumhara program sequential hai (line-by-line logic).
* Tum CLI ya sync apps bana rahe ho.

Avoid karo agar:

* Tumhara app real-time web app hai.
* Tum async environment me ho (e.g., FastAPI ya asyncio).

---

### 📝 Summary:

- **Type**: Synchronous
- **Blocking**: Yes
- **When**: CLI scripts, quick demos

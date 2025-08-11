### 🧠 **Kya hota hai `run_stream()`?**

`run_stream()` ek method hai jo OpenAI Agent SDK ke `Runner` class ka part hoti hai. Yeh method tab use hoti hai jab aap **streaming response** chahte ho agent se, instead of ek hi dafa pura result.

Matlab: Jaise-jaise agent ka response aata ja raha ho, waise-waise aapko milta jaye – real-time jese feel hoti hai.

---

### 🔍 **Kab use karte hain `run_stream()`?**

Agar aapka use case aesa ho:

* Jahan user ko turant feedback chahiye.
* Large responses expect kar rahe ho jo time lete hain generate hone mein.
* Aap UI bana rahe ho jahan text type hota jaye "typing..." jese.
* Prompt response dynamically dikhana ho (jaise ChatGPT khud kaam karta hai).

To phir `run_stream()` use hoti hai.

---

### 📘 **Syntax aur Basic Example (Source):**

Source script: `Runner/examples/03-Run_streamed.py`

Run:

```bash
python Runner/examples/03-Run_streamed.py
```

---

### ⚙️ **Kaise Kaam Karta Hai?**

Ye **asynchronous generator** ki tarah kaam karta hai.

* Jab tak agent ka response aata rehta hai, tab tak ye stream karta rehta hai.
* Har naya response chunk `async for` loop mein receive hota hai.
* Aap har chunk ko handle ya display kar sakte ho instantly (jaise frontend pe show karwana).

---

### 🧪 **Real-Life Example (Use Case):**

#### Case: Customer Support Chatbot

Imagine karo ek customer ne chatbot se poocha:

> "Mujhe batao ke mere internet ka issue kyun aaraha hai?"

Agar response kaafi lamba hai (diagnostics, steps, etc.), to agar aap `run()` use karte, to poora response aane mein delay hota. **But `run_stream()` se:**

* Pehle agent response karta: "Theek hai, mai check karta hu..."
* Phir: "Step 1: Please restart your router..."
* Phir: "Step 2: Check for loose cables..."

User ko lagta hai ke bot live soch raha hai ya type kar raha hai – better UX.

---

### 💡 **Developer Tip:**

Isko use karne ke liye aapko Python ke `async` and `await` concepts ache se samajhne honge. Agar aap FastAPI, Streamlit, ya koi async-compatible framework use kar rahe ho, to yeh method aapke liye perfect hai real-time interaction banane ke liye.

---

### 🧯 **Common Errors:**

1. **“RuntimeError: This event loop is already running”**

   * Jab aap Jupyter notebook mein `async` method chalate ho galat tareeke se.

2. **Stream response null milta hai**

   * Aapka agent ya task theek se define nahi hua.

---

### 🔚 Summary:

| 🔹 Feature  | 🔹 Description                              |
| ----------- | ------------------------------------------- |
| Method      | `run_stream()`                              |
| Class       | `Runner`                                    |
| Response    | Streaming (Live chunks)                     |
| Use-case    | Real-time feedback, better UX               |
| Requirement | Async functions (`async for`)               |
| Benefit     | Smooth user interaction, better performance |

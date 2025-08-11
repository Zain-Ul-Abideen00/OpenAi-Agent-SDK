### 🔹 Kya hota hai `RunResultStreaming`?

`RunResultStreaming` aik class hai jo tab use hoti hai jab aap agent ko **streaming mode** mein run karte ho — matlab jab response chunk-by-chunk real-time mein milta hai instead of ek full result ke.

Ye class aapko enable karti hai ke aap **real-time output stream** se interact karo jab aap `runner.run_stream()` use karte ho.

---

### 🔹 Real-Life Example:

Socho tum Google Assistant use kar rahe ho. Jab tum bolte ho:
**"Mujhe Lahore ka weather batao"**,
to uska jawab ek hi waqt mein nahi aata. Pehle wo bolta hai:
*"Lahore ka mausam aaj..."*,
phir kuch seconds baad:
*"25°C hai aur barish ke chances hain..."*

Ye **streaming** ka example hai.

Aise hi `RunResultStreaming` ka use tab hota hai jab hum **OpenAI Agent SDK** mein agent se real-time mein response lena chahte hain, especially jab response lamba ho ya slowly generate ho raha ho.

---

### 🔹 Kaise use hota hai?

Jab aap `runner.run_stream()` call karte ho, to uska result `RunResultStreaming` type ka object hota hai.

```python
result = await runner.run_stream(input="Hello, what's the weather today?")
```

Is `result` object ke andar:

* `.stream_output`
  – Ye aik async generator hota hai jo **real-time tokens (output)** stream karta hai.

---

### 🔹 Components of `RunResultStreaming`

| Property        | Description                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| `stream_output` | Async generator: ye har token ya chunk of data return karta hai jab tak pura output complete na ho jaye. |
| `final_output`  | Jab streaming complete ho jaye to ye aapko full output provide karta hai.                                |
| `raw_output`    | Backend se jo original response aya, uska raw version.                                                   |
| `steps`         | Wo steps jo agent ne run kiye operation ke dauran.                                                       |

---

### 🔹 Example Code (Source)

Source: `Runner/examples/07-RunResultStreaming.py`

Run:

```bash
python Runner/examples/07-RunResultStreaming.py
```

---

### 🔹 Kab use karna chahiye `RunResultStreaming`?

* Jab aapko **real-time UX (User Experience)** chahiye.
* Jab output lambaa hai aur aap nahi chahte user wait kare full result ke liye.
* Chatbots, voice assistants, live response systems mein.

---

### 🔹 Tip:

Agar aap normal synchronous result chahte ho to `runner.run()` ya `runner.run_sync()` use karo.
Agar aapko **progressive output** chahiye, to `runner.run_stream()` use karo aur uska result `RunResultStreaming` hoga.

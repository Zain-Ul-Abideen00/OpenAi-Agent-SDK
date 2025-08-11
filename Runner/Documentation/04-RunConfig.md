## 🧠 **`RunConfig` kya hota hai?**

`RunConfig` aik configuration class hoti hai jo batati hai ke agent ko run karte waqt kon kon se settings apply ki jayengi.

Jab bhi tum `runner.run()` ya `runner.run_stream()` use karte ho, to tum optionally aik `RunConfig` object bhi pass kar sakte ho jisme kuch specific cheezen define hoti hain, jaise:

* `name`: agent run ka naam kya ho
* `stream`: output streaming hogi ya nahi
* `max_steps`: maximum steps jo agent chalaye
* `input`: agent ko kya input diya ja raha hai
* `tools`: kon se tools available hon agent ko
* `allow_tool_use`: kya agent tools use kar sakta hai ya nahi

---

## 🔧 **RunConfig ke Parameters (one by one):**

### 1. **name (optional)**

Ye tumhari run ko ek naam de deta hai — useful for logs or debugging.

```python
RunConfig(name="my_first_run")
```

---

### 2. **input (required)**

Ye wo input hota hai jo tum agent ko dena chahte ho. Ye usually `str` (text) hota hai.

```python
RunConfig(input="Translate this English sentence to French.")
```

---

### 3. **stream (optional, default False)**

Ye batata hai ke output stream hogi ya nahi (line by line).

```python
RunConfig(input="Hello", stream=True)
```

---

### 4. **max\_steps (optional)**

Agent kitne steps tak chalega max — agar exceed ho gaye to forcibly stop ho jayega.

```python
RunConfig(input="Plan a 3-day trip", max_steps=5)
```

---

### 5. **tools (optional)**

Ye tum define kar sakte ho ke agent kon kon se tools use kare. Agar tum yahan kuch tools nahi doge to agent ko tools ka access nahi milega.

```python
RunConfig(input="Get the current weather", tools=[tool1, tool2])
```

---

### 6. **allow\_tool\_use (optional, default True)**

Ye tum control karte ho ke agent ko tools use karne ki permission honi chahiye ya nahi.

```python
RunConfig(input="Check website status", allow_tool_use=False)
```

---

## ✅ **Example – Source Script**

Source: `Runner/examples/04-RunConfig.py`

Run:

```bash
python Runner/examples/04-RunConfig.py
```

---

## 🧠 Tip:

Agar tum `RunConfig` nahi doge, to `runner.run()` default config use karega — lekin production apps mein recommended hota hai ke custom `RunConfig` diya jaye for full control.

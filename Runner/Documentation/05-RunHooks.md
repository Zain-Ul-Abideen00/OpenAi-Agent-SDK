## 🔹 Kya hai `RunHooks`? (Samajhne ka Asaan Tareeqa in Roman Urdu)

Socho tum aik **robot** ko task de rahe ho. Jab wo kaam shuru karta hai, us waqt tum chahte ho ke:

* Console me ek message print ho jaye (`on_start`)
* Jab bhi wo koi kaam kare to uski progress log ho (`on_step`)
* Aur jab kaam khatam ho to success/failure ka message mile (`on_end`)

Yahi kaam `RunHooks` karte hain!

Ye basically **events** hain jo agent ke **run ke lifecycle** me hotay hain — aur tum un par apni custom logic inject kar sakte ho.

---

## 🔹 3 Important `RunHooks` Callbacks:

| Hook Name  | Kab Trigger Hota Hai                          | Real-Life Analogy                                                     |
| ---------- | --------------------------------------------- | --------------------------------------------------------------------- |
| `on_start` | Jab agent ka run start hota hai               | Jese kisi machine ko on karte waqt "Machine On" message print ho jaye |
| `on_step`  | Har baar jab agent koi step perform karta hai | Jese har kaam ke baad wo kaam ka record likhna                        |
| `on_end`   | Jab agent ka run complete ho jaye             | Jese "Mission Accomplished" ya "Error Occurred" message show karna    |

---

## 🔹 Real-life Example (Roman Urdu)

Man lo tumhari AI agent ek **Email Likhnay Wali Agent** hai. Tum chahte ho:

* Jab wo kaam start kare to: `"Starting Email Agent"` print ho
* Har message ya email likhne ke step pe: `"Step done: Subject written"` print ho
* Jab email complete ho jaye: `"Email Agent run finished"` print ho

Ye sab tum `RunHooks` ke zariye kar sakte ho.

---

## 🔹 Code Example (Source)

Source: `Runner/examples/05-RunHooks.py`

Run:

```bash
python Runner/examples/05-RunHooks.py
```

---

## 🔹 Jahan `RunHooks` Useful Hote Hain

1. **Debugging** – Har step log karna
2. **Analytics** – Kitne runs hue, success/failure ka ratio kya hai
3. **Custom Logging** – Logs file me save karwana ya database me push karwana
4. **Custom Behavior** – Start/End pe notifications bhejna, timers chalana, etc.

---

## 🔹 Real-World Use Case

Socho tum ne aik AI customer support bot banaya. Tumhara manager chah raha hai ke:

* Jab bot chalu ho, log file me entry ho
* Har step ke baad analytics service ko ping kare
* Jab run complete ho to team ko Slack pe message bheje

Ye sab `RunHooks` se possible hai! 🎯

---

Agar tum chaaho to `RunHooks` ke saath `run_sync()` aur `run_stream()` me bhi use kar sakte ho exactly isi tarah se.

---

### ✅ Summary (1 line me)

**`RunHooks` tumhe har agent run ke start, step, aur end pe apni custom logic likhne ka control dete hain — debugging, analytics, aur behavior modification ke liye!**

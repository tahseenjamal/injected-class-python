# Capitalized Class Name Metaclass Example

This Python project demonstrates how to use a **custom metaclass** to enforce naming conventions on classes and how multiple classes interact through object composition.

---

## 📌 Features

- A metaclass (`CapitalizedClassNameMeta`) that enforces all class names to start with a capital letter.
- Three example classes:
  - `Human`: Uses the custom metaclass.
  - `Person`: Represents an individual.
  - `Profession`: Represents a profession with a job and salary.
- Object composition where a `Person` has a `Profession`.

---

## 🧠 How It Works

### Metaclass: `CapitalizedClassNameMeta`

```python
class CapitalizedClassNameMeta(type):
    def __init__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' must start with a capital letter")
        print(name, bases, attrs)
        super().__init__(name, bases, attrs)
```

This ensures that any class using this metaclass must have its name start with an uppercase letter. If not, a `TypeError` is raised.

### Classes

- `Human`: Uses the metaclass and will raise an error if renamed to lowercase (e.g., `human`).
- `Person`: Can be assigned a `Profession` instance.
- `Profession`: Contains a job title and a salary.

---

## 🧪 Example Usage

```python
darkstar = Person("Darkstar", 100)
darkstar.Profession = Profession("Software Engineer", 1)

print(str(darkstar))
```

### Output:
```
Darkstar is 100 years old, and is a Software Engineer earns 1 bitcoin
```

---

## 📦 Requirements

- Python 3.6+

No external dependencies required.

---

## ▶️ Running the Code

```bash
python filename.py
```

Replace `filename.py` with the name of your Python script.

---

## 📁 File Structure

```
project/
│
├── your_script.py
└── README.md
```

---

## 📜 License

This project is released under the MIT License.

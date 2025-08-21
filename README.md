## 🏗️ Assignment 1: Smartphone Class  

I designed a `Smartphone` class with attributes and methods.  
- Features encapsulation (`__storage` is private with getter/setter).  
- Inherits into a `GamingPhone` class.  
- Demonstrates polymorphism by overriding the `browse_internet()` method.  

### Example Code  
```python
phone1 = Smartphone("Samsung", "Galaxy S22", 128, "12hrs")
print(phone1.make_call("0712345678"))
print(phone1.browse_internet("YouTube"))
print(phone1.get_storage())

gaming_phone = GamingPhone("Asus", "ROG 6", 512, "15hrs", "Adreno 730")
print(gaming_phone.play_game("PUBG"))
print(gaming_phone.browse_internet("Twitch"))
````

### Sample Output

```
Samsung Galaxy S22 is calling 0712345678...
Browsing YouTube on Samsung Galaxy S22
Storage: 128GB
Playing PUBG with Adreno 730 GPU on Asus ROG 6!
Browsing Twitch at ultra speed with gaming mode ON!
```

---

## 🎭 Activity 2: Polymorphism Challenge

Created a base `Vehicle` class with subclasses:

* `Car` → Driving 🚗
* `Plane` → Flying ✈️
* `Boat` → Sailing ⛵

### Example Code

```python
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
```

### Sample Output

```
🚗 Driving on the road!
✈️ Flying in the sky!
⛵ Sailing on the water!
```

---

## 📂 Repository Structure

```
OOP-Assignment1/
│── assignment1.py     # Smartphone & GamingPhone classes
│── activity2.py       # Vehicle polymorphism challenge
│── README.md          # Documentation
```

---

## ✅ How to Run

Clone the repo and run using Python 3:

```bash
git clone https://github.com/your-username/OOP-Assignment1.git
cd OOP-Assignment1
python3 assignment1.py
python3 activity2.py
```

---

## ✨ Author

👩🏽‍💻 Doreen Masika


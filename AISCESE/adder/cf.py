# FUZZY LOGIC CONTROLLER - AUTOMATIC AC FAN SPEED CONTROL
# Mamdani Fuzzy Inference System

import numpy as np
import matplotlib.pyplot as plt

# 1. TRIANGULAR MEMBERSHIP FUNCTION
def trimf(x, abc):
    a, b, c = abc

    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    if b > a:
        left = (x >= a) & (x <= b)
        y[left] = (x[left] - a) / (b - a)

    if c > b:
        right = (x >= b) & (x <= c)
        y[right] = np.maximum(y[right], (c - x[right]) / (c - b))

    y[x == b] = 1.0

    return np.clip(y, 0, 1)


# 2. TRAPEZOIDAL MEMBERSHIP FUNCTION
def trapmf(x, abcd):
    a, b, c, d = abcd

    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)

    if b > a:
        rising = (x >= a) & (x < b)
        y[rising] = (x[rising] - a) / (b - a)

    top = (x >= b) & (x <= c)
    y[top] = 1.0

    if d > c:
        falling = (x > c) & (x <= d)
        y[falling] = (d - x[falling]) / (d - c)

    return np.clip(y, 0, 1)


# 3. DEFINE INPUT AND OUTPUT RANGES
temperature = np.linspace(0, 40, 401)
humidity = np.linspace(0, 100, 501)
fan_speed = np.linspace(0, 100, 1001)


# 4. TEMPERATURE MEMBERSHIP FUNCTIONS
temp_mf = {
    "Cool": trapmf(temperature, [0, 0, 16, 22]),
    "Comfortable": trimf(temperature, [18, 23, 28]),
    "Warm": trimf(temperature, [24, 30, 35]),
    "Hot": trapmf(temperature, [32, 36, 40, 40])
}


# 5. HUMIDITY MEMBERSHIP FUNCTIONS
humidity_mf = {
    "Low": trapmf(humidity, [0, 0, 25, 45]),
    "Normal": trimf(humidity, [30, 50, 70]),
    "High": trapmf(humidity, [55, 75, 100, 100])
}


# 6. FAN SPEED MEMBERSHIP FUNCTIONS
fan_mf = {
    "Low": trapmf(fan_speed, [0, 0, 20, 45]),
    "Medium": trimf(fan_speed, [30, 50, 70]),
    "High": trapmf(fan_speed, [55, 80, 100, 100])
}


# 7. PLOT TEMPERATURE MEMBERSHIP FUNCTIONS
plt.figure(figsize=(10, 4))
for label, mf in temp_mf.items():
    plt.plot(temperature, mf, label=label)

plt.title("Temperature Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()
plt.show()


# 8. PLOT HUMIDITY MEMBERSHIP FUNCTIONS
plt.figure(figsize=(10, 4))
for label, mf in humidity_mf.items():
    plt.plot(humidity, mf, label=label)

plt.title("Humidity Membership Functions")
plt.xlabel("Humidity (% RH)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()
plt.show()


# 9. PLOT FAN SPEED MEMBERSHIP FUNCTIONS
plt.figure(figsize=(10, 4))
for label, mf in fan_mf.items():
    plt.plot(fan_speed, mf, label=label)

plt.title("Fan Speed Membership Functions")
plt.xlabel("Fan Speed (%)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()
plt.show()


# 10. CRISP INPUT VALUES
room_temperature = 30.0
room_humidity = 70.0

print("Temperature:", room_temperature, "°C")
print("Humidity:", room_humidity, "% RH")


# 11. FUZZIFICATION
temp_degree = {
    label: float(np.interp(room_temperature, temperature, mf))
    for label, mf in temp_mf.items()
}

humidity_degree = {
    label: float(np.interp(room_humidity, humidity, mf))
    for label, mf in humidity_mf.items()
}

print("\nTemperature Membership:", temp_degree)
print("Humidity Membership:", humidity_degree)


# 12. FUZZY RULES
rules = {
    ("Cool", "Low"): "Low",
    ("Cool", "Normal"): "Low",
    ("Cool", "High"): "Medium",

    ("Comfortable", "Low"): "Low",
    ("Comfortable", "Normal"): "Medium",
    ("Comfortable", "High"): "High",

    ("Warm", "Low"): "Medium",
    ("Warm", "Normal"): "High",
    ("Warm", "High"): "High",

    ("Hot", "Low"): "High",
    ("Hot", "Normal"): "High",
    ("Hot", "High"): "High"
}


# 13. RULE EVALUATION, IMPLICATION AND AGGREGATION
aggregated_output = np.zeros_like(fan_speed, dtype=float)

print("\nActive Rules:")

for (t_label, h_label), out_label in rules.items():

    activation = min(
        temp_degree[t_label],
        humidity_degree[h_label]
    )

    clipped_output = np.minimum(
        activation,
        fan_mf[out_label]
    )

    aggregated_output = np.maximum(
        aggregated_output,
        clipped_output
    )

    if activation > 0:
        print(
            f"IF Temperature is {t_label} AND "
            f"Humidity is {h_label} THEN Fan Speed is {out_label}",
            "Activation:", activation
        )


# 14. PLOT AGGREGATED OUTPUT
plt.figure(figsize=(10, 5))

for label, mf in fan_mf.items():
    plt.plot(
        fan_speed,
        mf,
        linestyle=":",
        label=f"{label} (original)"
    )

plt.fill_between(
    fan_speed,
    aggregated_output,
    alpha=0.35,
    label="Aggregated Output"
)

plt.plot(
    fan_speed,
    aggregated_output,
    linewidth=2.5,
    label="Aggregated Envelope"
)

plt.title("Implication and Aggregation")
plt.xlabel("Fan Speed (%)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()
plt.show()


# 15. DEFUZZIFICATION - CENTROID METHOD
numerator = np.trapz(
    fan_speed * aggregated_output,
    fan_speed
)

denominator = np.trapz(
    aggregated_output,
    fan_speed
)

crisp_output = numerator / denominator

print("\nCrisp Fan Speed:", round(crisp_output, 2), "%")


# 16. FINAL LINGUISTIC OUTPUT
output_label = max(
    fan_mf,
    key=lambda label: np.interp(
        crisp_output,
        fan_speed,
        fan_mf[label]
    )
)

print("Fan Speed Category:", output_label)


# 17. PLOT FINAL DEFUZZIFIED OUTPUT
plt.figure(figsize=(10, 5))

for label, mf in fan_mf.items():
    plt.plot(fan_speed, mf, label=label)

plt.fill_between(
    fan_speed,
    aggregated_output,
    alpha=0.3,
    label="Aggregated Output"
)

plt.axvline(
    crisp_output,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Crisp Output = {crisp_output:.2f}%"
)

plt.title("Final Defuzzified Fan Speed")
plt.xlabel("Fan Speed (%)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid()
plt.show()











import numpy as np

# 1. DEFINE CLASSICAL SETS

temperature = [10, 20, 30, 40, 50]

low_classical = {10, 20}
medium_classical = {30}
high_classical = {40, 50}

print("Classical Sets")
print("Low:", low_classical)
print("Medium:", medium_classical)
print("High:", high_classical)


# 2. DEFINE FUZZY SETS

Low = np.array([1.0, 0.7, 0.2, 0.0, 0.0])
Medium = np.array([0.0, 0.3, 0.8, 0.3, 0.0])
High = np.array([0.0, 0.0, 0.0, 0.7, 1.0])

print("\nFuzzy Sets")
print("Low:", Low)
print("Medium:", Medium)
print("High:", High)


# 3. FUZZY SET OPERATIONS

# Union = Maximum
union = np.maximum(Low, Medium)

# Intersection = Minimum
intersection = np.minimum(Low, Medium)

# Complement = 1 - Membership
complement = 1 - Low

print("\nFuzzy Set Operations")
print("Union:", union)
print("Intersection:", intersection)
print("Complement of Low:", complement)


# 4. DEFINE FAN SPEED FUZZY SETS

fan_speed = [0, 25, 50, 75, 100]

slow = np.array([1.0, 0.7, 0.2, 0.0, 0.0])
moderate = np.array([0.0, 0.3, 0.8, 0.3, 0.0])
fast = np.array([0.0, 0.0, 0.0, 0.7, 1.0])

# 5. CONSTRUCT FUZZY RELATION USING CARTESIAN PRODUCT

R_low = np.minimum.outer(Low, slow)
R_medium = np.minimum.outer(Medium, moderate)
R_high = np.minimum.outer(High, fast)

# Combine all relations using Union (Maximum)
R = np.maximum(np.maximum(R_low, R_medium), R_high)

print("\nFuzzy Relation Matrix")
print(R)


# 6. MAX-MIN COMPOSITION

# Example input: Temperature membership in Low, Medium, High
input_temperature = np.array([0.0, 0.8, 0.2, 0.0, 0.0])

max_min = np.zeros(len(fan_speed))

for j in range(len(fan_speed)):
    values = np.minimum(input_temperature, R[:, j])
    max_min[j] = np.max(values)

print("\nMax-Min Composition")
print(max_min)


# 7. MAX-PRODUCT COMPOSITION

max_product = np.zeros(len(fan_speed))

for j in range(len(fan_speed)):
    values = input_temperature * R[:, j]
    max_product[j] = np.max(values)

print("\nMax-Product Composition")
print(max_product)


# 8. DETERMINE SUITABLE FAN SPEED

best_speed = fan_speed[np.argmax(max_min)]

print("\nFinal Result")
print("Suitable Fan Speed:", best_speed, "%")

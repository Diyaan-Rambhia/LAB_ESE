
import numpy as np
import matplotlib.pyplot as plt

# Universes of discourse
temperature = np.linspace(0, 40, 401)
humidity = np.linspace(0, 100, 501)
fan_speed = np.linspace(0, 100, 1001)

print("Temperature:", temperature.min(), "to", temperature.max())
print("Humidity:", humidity.min(), "to", humidity.max())
print("Fan Speed:", fan_speed.min(), "to", fan_speed.max())

def trimf(x, abc):
    a,b,c = abc
    x = np.asarray(x,dtype=float)
    y = np.zeros_like(x)

    if b > a:
        left = (x >= a) & (x <= b)
        y[left] = (x[left]-a)/(b-a)

    if c > b:
        right = (x >= b) & (x <= c)
        y[right] = np.maximum(y[right],(c-x[right])/(c-b))

    y[x == b] = 1.0
    return np.clip(y,0,1)


def trapmf(x, abcd):
    a,b,c,d = abcd
    x = np.asarray(x,dtype=float)
    y = np.zeros_like(x)

    if b > a:
        rising = (x >= a) & (x < b)
        y[rising] = (x[rising]-a)/(b-a)

    top = (x >= b) & (x <= c)
    y[top] = 1.0

    if d > c:
        falling = (x > c) & (x <= d)
        y[falling] = (d-x[falling])/(d-c)

    return np.clip(y,0,1)
    

# Humidity membership functions

humidity_mf = {
    "Low": trapmf(humidity, [0, 0, 25, 45]),
    "Normal": trimf(humidity, [30, 50, 70]),
    "High": trapmf(humidity, [55, 75, 100, 100])
}


plt.figure(figsize=(9, 4.8))

for label, values in humidity_mf.items():
    plt.plot(humidity, values, label=label, linewidth=2)

plt.title("Humidity Membership Functions")
plt.xlabel("Relative Humidity (%)")
plt.ylabel("Membership Degree")
plt.ylim(-0.05, 1.05)
plt.grid(True)
plt.legend()
plt.show()




temp_degree = {
    label: float(np.interp(room_temperature, temperature, mf))
    for label, mf in temp_mf.items()
}

{
    "Cool": 0.0,
    "Comfortable": 0.0,
    "Warm": 1.0,
    "Hot": 0.0
}
humidity_degree = {
    label: float(np.interp(room_humidity, humidity, mf))
    for label, mf in humidity_mf.items()
}






# Example crisp sensor readings
room_temperature = 30.0
room_humidity = 70.0

# Calculate temperature membership
temp_degree = {
    label: float(np.interp(room_temperature, temperature, mf))
    for label, mf in temp_mf.items()
}

# Calculate humidity membership
humidity_degree = {
    label: float(np.interp(room_humidity, humidity, mf))
    for label, mf in humidity_mf.items()
}

print("Temperature Membership:")
for label, degree in temp_degree.items():
    print(label, ":", degree)

print("\nHumidity Membership:")
for label, degree in humidity_degree.items():
    print(label, ":", degree)
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


# Evaluate every rule

rule_results = []

for (t_label, h_label), out_label in rules.items():

    activation = min(
        temp_degree[t_label],
        humidity_degree[h_label]
    )

    rule_results.append({
        "temperature": t_label,
        "humidity": h_label,
        "output": out_label,
        "activation": activation
    })

print("Rule Activations:")

for row in rule_results:
    if row["activation"] > 0:
        print(
            row["temperature"],
            row["humidity"],
            row["output"],
            row["activation"]
        )
        
        
activation = 0.75

clipped_output = np.minimum(
    activation,
    fan_mf["High"]
)

aggregated_output = np.zeros_like(fan_speed, dtype=float)

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













# Evaluate rules and aggregate output

rule_results = []
aggregated_output = np.zeros_like(fan_speed, dtype=float)

for (t_label, h_label), out_label in rules.items():

    # Calculate activation
    activation = min(
        temp_degree[t_label],
        humidity_degree[h_label]
    )

    # Clip output membership function
    clipped_output = np.minimum(
        activation,
        fan_mf[out_label]
    )

    # Aggregate using maximum
    aggregated_output = np.maximum(
        aggregated_output,
        clipped_output
    )

    rule_results.append({
        "temperature": t_label,
        "humidity": h_label,
        "output": out_label,
        "activation": activation
    })

print("Rule Activations:")

for row in rule_results:
    if row["activation"] > 0:
        print(
            row["temperature"],
            row["humidity"],
            row["output"],
            row["activation"]
        )
plt.figure(figsize=(10,5))

for label, mf in fan_mf.items():
    plt.plot(fan_speed, mf, linestyle=":",
             label=label + " original")

plt.fill_between(
    fan_speed,
    aggregated_output,
    alpha=0.35,
    label="Aggregated output"
)

plt.plot(
    fan_speed,
    aggregated_output,
    linewidth=2.5,
    label="Aggregated envelope"
)

plt.xlabel("Fan Speed (%)")
plt.ylabel("Membership Degree")
plt.title("Aggregated Fuzzy Output")
plt.legend()
plt.grid()
plt.show()
numerator = np.trapz(fan_speed * aggregated_output, fan_speed)

denominator = np.trapz(aggregated_output, fan_speed)

crisp_output = numerator / denominator

print("Fan Speed:", round(crisp_output, 2), "%")
output_label = max(
    fan_mf,
    key=lambda label: np.interp(crisp_output, fan_speed, fan_mf[label])
)

print("Fan Speed Category:", output_label)











































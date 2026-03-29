import json
import os
from datetime import datetime
import random

def run_neuron_update():
    file_path = "neuron_log.json"
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    neuron_value = random.uniform(0, 1)
    
    new_entry = {
        "timestamp": current_time,
        "neuron_score": round(neuron_value, 4),
        "status": "active"
    }

    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(new_entry)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Successfully updated {file_path} at {current_time}")

if __name__ == "__main__":
    run_neuron_update()

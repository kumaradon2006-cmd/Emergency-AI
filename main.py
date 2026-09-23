print("===================================")
print("       EMERGENCY AI SYSTEM")
print("===================================")

patient_name = input("Enter patient name: ")
symptom = input("Enter emergency symptom: ")

if symptom.lower() in ["chest pain", "heart attack", "breathing problem"]:
    hospital = "Nearest Emergency/Critical Care Hospital"
elif symptom.lower() in ["fracture", "accident", "injury"]:
    hospital = "Nearest Trauma Hospital"
else:
    hospital = "Nearest General Hospital"

print("\n--- EMERGENCY RESULT ---")
print("Patient:", patient_name)
print("Emergency:", symptom)
print("Recommended:", hospital)
print("Emergency Contact: 108")
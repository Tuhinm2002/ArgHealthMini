from collections import defaultdict
import pickle
Severity=pickle.load(open("disease.pkl","rb"))
# new_dict=defaultdict(Severity)
print(type(Severity[4]))
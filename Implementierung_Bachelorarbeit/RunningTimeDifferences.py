import numpy as np
import time

# Kleine Python-Liste
small_list = list(range(10))

# Große Python-Liste
large_list = list(range(10000))

# Großes NumPy-Array
large_numpy_array = np.arange(10000)

# Zeitmessung für die Iteration über die kleine Python-Liste
start_time = time.time()
for x in small_list:
    pass
small_list_duration = time.time() - start_time

# Zeitmessung für die Iteration über die große Python-Liste
start_time = time.time()
for x in large_list:
    pass
large_list_duration = time.time() - start_time

# Zeitmessung für die Iteration über das große NumPy-Array
start_time = time.time()
for x in large_numpy_array:
    pass
large_numpy_array_duration = time.time() - start_time

# Zeitmessung für eine numerische Operation über die große Python-Liste
start_time = time.time()
large_list_result = [x * 2 for x in large_list]
large_list_operation_duration = time.time() - start_time

# Zeitmessung für eine numerische Operation über das große NumPy-Array
start_time = time.time()
large_numpy_array_result = large_numpy_array * 2
large_numpy_array_operation_duration = time.time() - start_time

print(f"Zeit für Iteration über kleine Python-Liste (10 Elemente): {small_list_duration:.10f} Sekunden")
print(f"Zeit für Iteration über große Python-Liste (10.000 Elemente): {large_list_duration:.10f} Sekunden")
print(f"Zeit für Iteration über großes NumPy-Array (10.000 Elemente): {large_numpy_array_duration:.10f} Sekunden")
print(f"Zeit für Operation über große Python-Liste (10.000 Elemente): {large_list_operation_duration:.10f} Sekunden")
print(f"Zeit für Operation über großes NumPy-Array (10.000 Elemente): {large_numpy_array_operation_duration:.10f} Sekunden")

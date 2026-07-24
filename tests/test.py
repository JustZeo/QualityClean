import qualityclean as qc

df = qc.load("employee_data_dirty.csv")

result = qc.clean(df)

print(result.df)         # Cleaned DataFrame
print(result.report)     # Report object

qc.audit(result, format="print")
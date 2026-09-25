### File: olist_orders_dataset.csv

- Observation: No duplicate rows were found when comparing all columns.
- Evidence (operation/output): datasets["orders"].duplicated().sum() returned 0.
- Why it may matter: Repeated records could inflate order counts.
- Proposed action (or no action): Do not remove any full-row duplicates.
- Reason / assumption to verify: This check found none. It does not establish
  whether order_id is unique, which needs a separate check.

 ### File: olist_customers_dataset.csv

- Observation: The describe() output summarized only customer_zip_code_prefix.
  It contained 99,441 non-missing values, ranging from 1003 to 99990.
- Evidence (operation/output): datasets["customers"].describe()
  returned count = 99441, min = 1003, and max = 99990.
- Why it may matter: ZIP-code prefixes identify locations. Their average
  is not a useful measure of customer behavior.
- Proposed action (or no action): Investigate whether this column should
  be stored as text to preserve its formatting.
- Reason / assumption to verify: Pandas treated the column as numeric.
  Check the original CSV and expected format to determine whether
  leading zeros need to be preserved.
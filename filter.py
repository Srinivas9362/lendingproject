from snowflake.snowpark.function import col


def filter_by_column_values(session, table_name, column_value):
  df = session.table(table_name)
  return df.filter(col("COLUMN3") == column_value)

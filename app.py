import streamlit as st
import pandas as pd

st.title("Pandas Data Processing Demo App")

# Sample Data
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, None],
    "salary": [50000, 60000, None, 80000, 90000],
    "department": ["HR", "IT", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

st.subheader("Original Data")
st.write(df)

# Sidebar options
option = st.sidebar.selectbox(
    "Choose Operation",
    ["View Head", "Handle Missing Values", "GroupBy", "Apply Function", "Merge Example", "Filter Data"]
)

# 1. head()
if option == "View Head":
    st.subheader("First 3 Rows")
    st.write(df.head(3))

# 2. fillna / dropna
elif option == "Handle Missing Values":
    method = st.radio("Choose Method", ["Drop NA", "Fill NA with Mean"])

    if method == "Drop NA":
        st.write(df.dropna())
    else:
        df_filled = df.copy()
        df_filled["age"].fillna(df_filled["age"].mean(), inplace=True)
        df_filled["salary"].fillna(df_filled["salary"].mean(), inplace=True)
        st.write(df_filled)

# 3. groupby()
elif option == "GroupBy":
    st.subheader("Average Salary by Department")
    result = df.groupby("department")["salary"].mean()
    st.write(result)

# 4. apply()
elif option == "Apply Function":
    st.subheader("Salary after 10% Increment")
    df_apply = df.copy()
    df_apply["salary"] = df_apply["salary"].fillna(0)
    df_apply["new_salary"] = df_apply["salary"].apply(lambda x: x * 1.1)
    st.write(df_apply)

# 5. merge()
elif option == "Merge Example":
    dept_data = {
        "department": ["HR", "IT", "Finance"],
        "location": ["Delhi", "Bangalore", "Mumbai"]
    }
    df_dept = pd.DataFrame(dept_data)

    merged = pd.merge(df, df_dept, on="department", how="left")
    st.write(merged)

# 6. loc / filtering
elif option == "Filter Data":
    st.subheader("Employees with Salary > 60000")
    filtered = df.loc[df["salary"] > 60000]
    st.write(filtered)

st.sidebar.info("This app demonstrates key Pandas functions interactively.")

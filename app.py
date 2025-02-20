# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# # Set up Our App
# st.set_page_config(page_title="Data Sweeper", layout="wide")
# st.title("💿 Data Sweeper")
# st.write("Transform your files between CSV and Excel format with built-in data cleaning and visualization.")

# uploaded_files = st.file_uploader("Upload your files (CSV or Excel)", type=['csv', 'xlsx'], accept_multiple_files=True)

# if uploaded_files:
#     for uploaded_file in uploaded_files:
#         file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

#         if file_ext == '.csv':
#             df = pd.read_csv(uploaded_file)
#         elif file_ext == '.xlsx': 
#             df = pd.read_excel(uploaded_file)
#         else:
#             st.error(f'Unsupported file format: {file_ext}')
#             continue

#         # Display info about the file
#         st.write(f"**File Name:** {uploaded_file.name}")
#         st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

#         # Show 5 rows of our dataframe
#         st.subheader("Preview of the DataFrame")
#         st.dataframe(df.head())

#         # Options for data cleaning
#         st.subheader("Data Cleaning Options")
#         if st.checkbox(f"Clean Data for {uploaded_file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates from {uploaded_file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("✅ Duplicates Removed")

#             with col2:
#                 if st.button(f"Fill Missing Values for {uploaded_file.name}"):
#                     numeric_cols = df.select_dtypes(include=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.mean()))
#                     st.write("✅ Missing Values Filled")

#         # Choose Specific Columns to Keep
#         st.subheader("Select Columns to Keep")
#         columns = st.multiselect(f"Choose Columns for {uploaded_file.name}", df.columns, default=df.columns)
#         df = df[columns]

#         # Data Visualization
#         st.subheader("📊 Data Visualization")
#         if st.checkbox(f"Show Visualization for {uploaded_file.name}"):
#             st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :2])

#         # Convert the File to CSV or Excel
#         st.subheader("📂 Conversion Options")
#         conversion_type = st.radio(f"Convert {uploaded_file.name} to", ['CSV', 'Excel'], key=uploaded_file.name)

#         if st.button(f"Convert {uploaded_file.name}"):
#             buffer = BytesIO()

#             if conversion_type == 'CSV':
#                 df.to_csv(buffer, index=False)
#                 new_file_name = uploaded_file.name.replace(file_ext, '.csv')
#                 mime_type = 'text/csv'

#             elif conversion_type == 'Excel':
#                 df.to_excel(buffer, index=False, engine='openpyxl')
#                 new_file_name = uploaded_file.name.replace(file_ext, '.xlsx')
#                 mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

#             buffer.seek(0)

#             # Download Button
#             st.download_button(
#                 label=f"Download {new_file_name}",
#                 data=buffer,
#                 file_name=new_file_name,
#                 mime=mime_type
#             )

# st.success("✅ Thanks for using App.")
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up Our App with a Stylish Theme
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.markdown(
    """
    <style>
    .big-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #ff6f61;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
    }
    .stButton>button {
       
        color:  #ff6f61;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
    }
    .stDownloadButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
    }
    .stCheckbox>div>label {
        font-size: 18px;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='big-title'>💿 Data Sweeper</div>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Transform your files between CSV and Excel format with built-in data cleaning and visualization.</p>", unsafe_allow_html=True)

uploaded_files = st.file_uploader("Upload your files (CSV or Excel)", type=['csv', 'xlsx'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

        if file_ext == '.csv':
            df = pd.read_csv(uploaded_file)
        elif file_ext == '.xlsx': 
            df = pd.read_excel(uploaded_file)
        else:
            st.error(f'❌ Unsupported file format: {file_ext}')
            continue

        # Display info about the file
        st.markdown(f"### 📂 File Name: `{uploaded_file.name}`")
        st.markdown(f"**📏 File Size:** `{uploaded_file.size / 1024:.2f} KB`")

        # Show DataFrame Preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df.head(), height=200)

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning")
        if st.checkbox(f"Clean Data for `{uploaded_file.name}`"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑 Remove Duplicates from {uploaded_file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed")

            with col2:
                if st.button(f"🔄 Fill Missing Values for {uploaded_file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.mean()))
                    st.success("✅ Missing Values Filled")

        # Column Selection
        st.subheader("📌 Select Columns to Keep")
        columns = st.multiselect(f"Choose Columns for `{uploaded_file.name}`", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for `{uploaded_file.name}`"):
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            if numeric_cols:
                selected_col = st.selectbox("Select Column for Visualization", numeric_cols, key=f"col_select_{uploaded_file.name}")
                st.bar_chart(df[selected_col])
            else:
                st.warning("⚠ No numeric columns found for visualization.")

        # Convert File
        st.subheader("📂 Convert File Format")
        conversion_type = st.radio(f"Convert `{uploaded_file.name}` to", ['CSV', 'Excel'], key=uploaded_file.name)

        if st.button(f"💾 Convert `{uploaded_file.name}`"):
            buffer = BytesIO()

            if conversion_type == 'CSV':
                df.to_csv(buffer, index=False)
                new_file_name = uploaded_file.name.replace(file_ext, '.csv')
                mime_type = 'text/csv'

            elif conversion_type == 'Excel':
                df.to_excel(buffer, index=False, engine='openpyxl')
                new_file_name = uploaded_file.name.replace(file_ext, '.xlsx')
                mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇ Download `{new_file_name}`",
                data=buffer,
                file_name=new_file_name,
                mime=mime_type,
            )

st.success("✅ Thank you for using Data Sweeper! 🚀")

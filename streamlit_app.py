import streamlit as st
import requests

if st.button("Get Servers"):
    response = requests.get("http://127.0.0.1:8000/servers")
    st.dataframe(response.json())

st.title("My First Streamlit App")

st.write("Welcome to my Server Management Application")

server_name = st.text_input("Enter Server Name")


instance_type = st.selectbox(
    "Select instance type", 
    ["t3.micro", "t3.small", "t3.medium", "t3.large"]
    )

status = st.selectbox(
    "Select status",
    ["Running", "Stopped"]
    )

if st.button("Create Server"):

    server_data = {
        "name": server_name,
        "instance_type": instance_type,
        "status": status
    }

    response = requests.post(
        "http://127.0.0.1:8000/servers",
        json=server_data
    )

    if response.status_code == 201:
        st.success("Server created successfully!")

    else:
        st.error(response.json()["detail"])


update_name = st.text_input("Server Name to Update")

update_instance = st.selectbox(
    "New Instance Type",
    ["t3.micro", "t3.small", "t3.medium", "t3.large"]
)

update_status = st.selectbox(
    "New Status",
    ["Running", "Stopped"]
)
if st.button("Update Server"):

    updated_data = {
        "name": update_name,
        "instance_type": update_instance,
        "status": update_status
    }

    response = requests.put(
        f"http://127.0.0.1:8000/servers/{update_name}",
        json=updated_data
    )
    if response.status_code == 200:
        st.success("Server updated successfully!")

    else:
        st.error(response.json()["detail"])


delete_name = st.text_input("Enter Server Name to Delete")
if st.button("Delete Server"):
    response = requests.delete(
        f"http://127.0.0.1:8000/servers/{delete_name}"
        )

    if response.status_code == 200:
        st.success("Server deleted successfully!")

    else:
        st.error(response.json()["detail"])




st.write(f"Server Name: {server_name}")
st.write(f"Instance Type: {instance_type}")



if response.status_code == 201:
    st.success("Server deleted successfully!")
else:
    st.error(response.json()["detail"])
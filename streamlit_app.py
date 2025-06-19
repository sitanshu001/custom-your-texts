import streamlit as st
import re
from pathlib import Path
import pandas as pd
cur_folder = Path.cwd()
text_folder_path = Path(cur_folder/"text_files/")
text_files_list = [f.name for f in text_folder_path.iterdir()]
text_files_tuple = ("",)+tuple(text_files_list)

data_science_folder_path = Path(text_folder_path/"Data Science")
data_science_list = [f.name for f in data_science_folder_path.iterdir()]
data_science_tuple=("",)+tuple(data_science_list)

web_dev_folder_path = Path(text_folder_path/"Devlopment Website")
web_dev_list = [f.name for f in web_dev_folder_path.iterdir()]
web_dev_tuple=("",)+tuple(web_dev_list)

other_folder_path = Path(text_folder_path/"other folders")
other_folder_list = [f.name for f in other_folder_path.iterdir()]
other_folder_tuple=("",)+tuple(other_folder_list)

allowed_to_use_this_file=""
ltr = ""
fnl = ""
final_letter = ""
targets = None
save = ""
unique_targets = []
ans = []
use_this_file=""
selected=""
st.title("Any Passage/Text Editor")
st.text("(Helpfull For Cover Letter/application Editing)")
file_path=Path()
st.sidebar.subheader("Instruction")
st.sidebar.markdown("""
                    - The variable portion should be inside square brackets '[' & ']' to edit those portion.
                    - """)
st.markdown("---")
st.sidebar.markdown("---")

auto_manual=st.selectbox("auto/manual",("","upload pre-existing file","enter manually"))

if(auto_manual == "enter manually"):
    st.header("Insert Your Basic Text")
    ltr = st.text_area("Enter text (for a blank line enter 2 times to save the text enter ctrl + enter)")

if(auto_manual  == "upload pre-existing file"):
    # Initialize all checkboxes in session state
    for opt in text_files_list:
        if f"{opt}_check" not in st.session_state:
            st.session_state[f"{opt}_check"] = False

    # Handle checkbox behavior
    def check_only(selected_option):
        for opt in text_files_list:
            st.session_state[f"{opt}_check"] = (opt == selected_option)

    # Create checkboxes
    for opt in text_files_list:
        st.checkbox(
            label=opt,
            key=f"{opt}_check",
            value=st.session_state[f"{opt}_check"],
            on_change=check_only,
            args=(opt,)
        )
    for opt in text_files_list:
        if st.session_state.get(f"{opt}_check"):
            selected = opt
            break
    if st.button("open"):
        pass
    folderpath=Path(text_folder_path/selected)
    all_filename=[filename.name for filename in folderpath.iterdir()]
    all_filename.insert(0,"")
    txt_file_s=str(st.selectbox(f"{selected}",all_filename))
    file_path=str(Path(folderpath/txt_file_s)).replace(".txt","")
    st.write(file_path)
    with open(f"{file_path}.txt",'r', encoding="utf-8") as file:
        ltr=file.read()

ltr = ltr.replace("*","")
ltr = ltr.replace("\\","")
fnl = ltr.replace("[","")
fnl = fnl.replace("]","")
targets = re.findall(r'\[(.*?)\]',ltr)

for target in targets:
    if target not in unique_targets:
        unique_targets.append(target)

for i in range(len(unique_targets)):
    ans.append(st.text_input(unique_targets[i]))
    fnl=fnl.replace(unique_targets[i],ans[i])
st.markdown("---")

wana_print = st.sidebar.checkbox("wana print?")

if (wana_print):
    st.header("Updated Text")
    st.subheader("Here is your Updated Text!!")
    st.write(fnl)

save = st.sidebar.checkbox("Do You want to save this file")
st.sidebar.markdown("---")
if (save): 

    # field = st.selectbox("field :",("","Web Dev","Data Science","other_files"))
    # if field == "Web Dev":
    #     select_to_save = st.selectbox("Webdev Formats :",web_dev_tuple)
    # elif field == "Data Science":
    #     select_to_save = st.selectbox("Data Science Format :",data_science_tuple)
    # elif field == "text_files":
    #     select_to_save = st.selectbox("other text files: ",other_folder_tuple)
            
    # file_count=len(text_files_list)
    # filename="sample_"+str(file_count)
    # with open(f"{text_folder_path}//{filename}.txt", "w") as file:
    #     file.write(fnl)
    pass

st.sidebar.subheader("Upcoming Targeted Updates")
st.sidebar.markdown("""
                    - Response
                    - Clean Ui
                    - Extra features:
                        - save to a location
                    """)

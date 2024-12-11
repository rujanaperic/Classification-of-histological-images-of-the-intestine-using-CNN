import pandas as pd
import os
import shutil

def get_dataframe(excel_file):

    #load the excel file into pandas dataframe
    df = pd.read_excel(excel_file)
    return df

def split_patient_wise(df, source_dir, dest_dir):

    #TODO: PONAVLJAJUĆI KOD --> PREOBLIKUJ NEKIM MODULOM KOJI ĆE IMATI FUNKCIJU "CREATING DIRECTORY STRUCTURE" I SAMO POZOVI TU FUNKCIJU ODAVDJE
    #ensure output train directory exists
    if not os.path.exists(dest_dir+"/train"):
        os.makedirs(dest_dir+"/train")

    #ensure output test directory exists
    if not os.path.exists(dest_dir+"/test"):
        os.makedirs(dest_dir+"/test")

    #ensure output train directory exists
    if not os.path.exists(dest_dir+"/train"+"/CD"):
        os.makedirs(dest_dir+"/train"+"/CD")

    #ensure output train directory exists
    if not os.path.exists(dest_dir+"/train"+"/UC"):
        os.makedirs(dest_dir+"/train"+"/UC")

    #ensure output test directory exists
    if not os.path.exists(dest_dir+"/test"+"/CD"):
        os.makedirs(dest_dir+"/test"+"/CD")

    #ensure output test directory exists
    if not os.path.exists(dest_dir+"/test"+"/UC"):
        os.makedirs(dest_dir+"/test"+"/UC")

    #iterate over each column (patient data) in dataframe
    for label in df.columns:

        #count number of pictures for each patient
        num_of_images = df[label].count()

        #if patient has exactly one picture, put that picture into test folder
        if num_of_images == 1:

            #set the image file name
            image_file = str(df[label][0]) + ".ndpi"

            #set the correct class_name
            class_name = label.split(".")[0]

            #move the image from the original dataset into the corresponding UC/CD test folder
            try:

                if class_name == "CD":
                    shutil.copy2(os.path.join(source_dir, image_file), os.path.join(dest_dir+"/test"+"/CD", image_file))
                    print("Image " + image_file + " was put into test/CD folder!")
                elif class_name == "UC":
                    shutil.copy2(os.path.join(source_dir, image_file), os.path.join(dest_dir+"/test"+"/UC", image_file))
                    print("Image " + image_file + " was put into test/UC folder!")

            except FileNotFoundError:
                print("File " + image_file + " is not found.") 

        #if the patient has more then one picture, put all of patient's pictures into train folder
        else:

            #iterate through patient's data and move every picture into the corresponding train folder
            for value in range(len(df[label])):
                #ensure that data is not nan
                if not pd.isna(df[label][value]):
                    #set the image file name
                    image_file = df[label][value] + ".ndpi"
                     #set the correct class_name
                    class_name = label.split(".")[0]

                    #move the image from the original dataset into the corresponding UC/CD train folder
                    try:

                        if class_name == "CD":
                            shutil.copy2(os.path.join(source_dir, image_file), os.path.join(dest_dir+"/train"+"/CD", image_file))
                            print("Image " + image_file + " was put into train/CD folder!")
                        elif class_name == "UC":
                            shutil.copy2(os.path.join(source_dir, image_file), os.path.join(dest_dir+"/train"+"/UC", image_file))
                            print("Image " + image_file + " was put into train/UC folder!")

                    except FileNotFoundError:
                        print("File " + image_file + " is not found.") 
                        
    
def split_in_ratio(df, source_dir, dest_dir, ratio):
    return





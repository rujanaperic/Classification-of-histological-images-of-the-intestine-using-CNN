from src.colon_image_mp import data_loading as dl

'''
CIJELA OVA SKRIPTA POZIVATI ĆE SE SAMO JEDNOM
'''
def main():

    #load the excel document that includes labels for all pictures into dataframe
    df= dl.get_dataframe("../../dataset/labeled_scans_original.xls")
    print(df)

    #with the help of known dataframe, do the patient-wise split of dataset and categorise
    #results will be new folders with data that matches requirements
    dl.split_patient_wise(df, 
                          "../../dataset/original_dataset", 
                          "../../dataset/patient_wise_dataset/patient_wise_original")

    '''
    SPLIT TRAIN AND TEST INTO LABELS --> POZIVA SE SAMO JEDNOM
    ako train i test folderi nemaju subfoldere s nazivima labela
        napravi subfoldere s nazivima labela

    kreni iterirati po train/test folderu:
        uzmi ime slike: 
            pronađi to ime u dataframeu
            ako pripadna labela stupca u kojem je pronađena ta slika na UC --> stavi u UC folder
            ako je pripadna labela stupca u kojem je pronađena ta slika na CD --> stavi u CD folder
    '''
    #dl.split_in_ratio()


if __name__ == "__main__":
    main()

from unicodedata import category
from unittest import result
from django.db import models


class student:
    # categories = ["General", "NC-OBC-cum-Transgender", "SC", "ST", "PWD"]
    # XII_streams = ["Science", "Commerce", "Arts"]

    # Degree Cat -->
    # AC-1 (Medicine and Surgery based subjects): MBBS, MD (USA).
    # AC-2 (Selected Professional Degrees): Chartered Accountancy (CA), Cost and Works Accountancy (ICWA), Company Secretaryship (CS).
    # AC-3 (All Commerce, Economics, Finance and Management Related Degrees):Including BAF, BBA, BBE, BBI, BBM, BBS, BCAF, BCCA, BCOM, BFIA, BFM, BHM, BHMCT, BIBF, BMS (Bachelor of Management studies) and BSBA degrees.
    # AC-4 I (All Engineering, Technology and Architecture related Areas): Including BARCH, BE, BIT, BINFTECH, BS (ENG)/ BSC (ENG), BTECH and integrated MTECH degrees (Excluding all degrees in Accessories Design/Apparel Production/Design/Fashion Communication/Fashion Design/Fashion Technology/Interior Design/Knit Wear Design/Leather Design/Jewelry Design/Footwear Design, and BS/BSC degrees in Information Technology).
    # AC-5 (All Arts/Humanities Related Degrees, Design, Education, Fashion Design/Technology, Law and Rural Studies): Including any BA (excluding Economics, Geography and Geological Sciences, Mathematics and Statistics), BAA, BAJM, BCJ, BDES, BED, BFTECH, BJ, BJMC, BL, BM (Bachelor of Music), BMC, BMM, BMus, BSW and LLB.
    # AC-6: Any other discipline not mentioned in AC-1 to AC-5.

    def __init__(self,name, X_percent, XII_percent, XII_stream, degree_percent, degree_cat, gender,
                 category,work_ex=0):
        self.Name = name
        # self.Last_Name = last_name

        self.X_percent = X_percent
        self.XII_percent = XII_percent
        self.XII_stream = XII_stream

        self.Degree_percent = degree_percent
        self.Degree_cat = degree_cat

        self.Work_ex = work_ex

        self.Gender = gender
        self.category = category

    def basic_elibility(self,degree_percent = 0,degree_percent_for_category=0,x_percent=0,x_percent_for_category=0,xii_percent=0,xii_percent_for_category=0,workex=0):
        eligible = True
        reason = []
        if self.category == "General":
            if self.Degree_percent < degree_percent:
                reason.append("Graduation Score below min criteria")
                eligible=False
            if self.X_percent <x_percent:
                reason.append("Class X Score Below Minimum Criteria")
                eligible =False
            if self.XII_percent<xii_percent:
                reason.append("Class XII Score Below Minimum Criteria")
                eligible =False
            if self.Work_ex<workex:
                reason.append("Work Experience Below Minimum Criteria")
                eligible =False
        else:
            if self.Degree_percent < degree_percent_for_category:
                reason.append("Graduation Score Below Minimum Criteria")
                eligible=False
            if self.X_percent <x_percent_for_category:
                reason.append("Class X Score Below Minimum Criteria")
                eligible =False
            if self.XII_percent<xii_percent_for_category:
                reason.append("Class XII Score Below Minimum Criteria")
                eligible =False
            if self.Work_ex<workex:
                reason.append("Work Experience Below Minimum Criteria")
                eligible =False

        return eligible,reason

    def IIMA(self):
        percentile = 0
        if self.category=="General":
            if self.Degree_cat == "Engineering":
                percentile = 99.8
            else:
                percentile = 99.6
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Degree_cat == "Engineering":
                percentile = 99.5
            else:
                percentile = 99.4
        elif self.category == "SC":
            if self.Degree_cat == "Engineering":
                percentile = 89.5
            else:
                percentile = 88.0
        elif self.category == "ST":
            if self.Degree_cat == "Engineering":
                percentile = 79.5
            else:
                percentile = 77.0
        elif self.category == "PWD":
            if self.Degree_cat == "Engineering":
                percentile = 82.5
            else:
                percentile = 82.0

        percentile = str(percentile)+ '+'
        aqm = (self.X_percent + self.XII_percent) / 2
        eligible = True
        reason = []
        if self.category == "General":
            
            if (self.XII_stream == "Science" and aqm < 80) or \
                    (self.XII_stream == "Commerce" and aqm < 77) or \
                    (self.XII_stream == "Arts" and aqm < 75):
                reason.append("X and XII Average Score Below Minimum Criteria")
                eligible=False

        elif self.category == "NC-OBC-cum-Transgender":
            if (self.XII_stream == "Science" and aqm < 75) or \
                    (self.XII_stream == "Commerce" and aqm < 72) or \
                    (self.XII_stream == "Arts" and aqm < 70):
                reason.append("X and XII Average Score Below Minimum Criteria")
                eligible=False
        elif self.category == "SC":
            if (self.XII_stream == "Science" and aqm < 70) or \
                    (self.XII_stream == "Commerce" and aqm < 67) or \
                    (self.XII_stream == "Arts" and aqm < 64):
                reason.append("X and XII Average Score Below Minimum Criteria")
                eligible=False
        elif self.category == "ST":
            if (self.XII_stream == "Science" and aqm < 65) or \
                    (self.XII_stream == "Commerce" and aqm < 62) or \
                    (self.XII_stream == "Arts" and aqm < 59):
                reason.append("X and XII Average Score Below Minimum Criteria")
                eligible=False
        elif self.category == "PWD":
            if (self.XII_stream == "Science" and aqm < 70) or \
                    (self.XII_stream == "Commerce" and aqm < 67) or \
                    (self.XII_stream == "Arts" and aqm < 64):
                reason.append("X and XII Average Score Below Minimum Criteria")
                eligible=False
        
        if eligible == True:
            eligible,reason = self.basic_elibility()
        else:
            elg,r = self.basic_elibility()
            reason.extend(r)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Ahmedabad" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IIMB(self):
        percentile = 0
        if self.category=="General":
            if self.Degree_cat == "Engineering":
                percentile = 99.8
            else:
                percentile = 99.7
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Degree_cat == "Engineering":
                percentile = 98.8
            else:
                percentile = 98.5
        elif self.category == "SC":
            if self.Degree_cat == "Engineering":
                percentile = 92
            else:
                percentile = 91
        elif self.category == "ST":
            if self.Degree_cat == "Engineering":
                percentile = 78.5
            else:
                percentile = 75
        elif self.category == "PWD":
            if self.Degree_cat == "Engineering":
                percentile = 84.0
            else:
                percentile = 85.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)

        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Banglore" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IIMC(self):
        percentile = 0
        if self.category=="General":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 99.6
                else:
                    percentile = 99.4
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 99.3
                else:
                    percentile = 99.2
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 97.5
                else:
                    percentile = 96.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 90.0
                else:
                    percentile = 90.0
        elif self.category == "SC":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 94.0
                else:
                    percentile = 94.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 83.0
                else:
                    percentile = 83.0
        elif self.category == "ST":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 88.0
                else:
                    percentile = 88.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 72.0  
                else:
                    percentile = 72.0
        elif self.category == "PWD":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 87.0   
                else:
                    percentile = 87.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 75.0
                else:
                    percentile = 75.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Calcutta" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
        

    def IIML(self):
        percentile = 0
        if self.category=="General":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 99.5
                else:
                    percentile = 99.4
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 99.4
                else:
                    percentile = 98.2
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 97.5
                else:
                    percentile = 95.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 95.0
                else:
                    percentile = 88.0
        elif self.category == "SC":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 94.0
                else:
                    percentile = 88.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 88.0
                else:
                    percentile = 78.0
        elif self.category == "ST":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 88.0
                else:
                    percentile = 78.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 77.0  
                else:
                    percentile = 65.0
        elif self.category == "PWD":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 90.0  
                else:
                    percentile = 90.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 82.0
                else:
                    percentile = 82.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Lucknow" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IIMK(self):
        percentile = 0
        if self.category=="General":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 99.6
                else:
                    percentile = 99.4
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 97.0
                else:
                    percentile = 91.0
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 98.0
                else:
                    percentile = 92.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 92.0
                else:
                    percentile = 78.0
        elif self.category == "SC":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 92.0
                else:
                    percentile = 86.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 86.0
                else:
                    percentile = 68.0
        elif self.category == "ST":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 94.0
                else:
                    percentile = 83.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 82.0  
                else:
                    percentile = 62.0
        elif self.category == "PWD":
            if self.Gender=="Male":
                if self.Degree_cat == "Engineering":
                    percentile = 89.0 
                else:
                    percentile = 70.0
            elif self.Gender == "Female":
                if self.Degree_cat == "Engineering":
                    percentile = 72.0
                else:
                    percentile = 56.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45,x_percent=60,x_percent_for_category=55,xii_percent=60,xii_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM kozhikode" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IIMI(self):
        percentile = 0
        
        if self.category=="General":
            if self.X_percent<85 or self.XII_percent<90:
                percentile = 99.9
            else:
                if self.Gender=="Male":
                    if self.Degree_cat == "Engineering":
                        percentile = 95.0
                    else:
                        percentile = 94.0
                elif self.Gender == "Female":
                    if self.Degree_cat == "Engineering":
                        percentile = 90.0
                    else:
                        percentile = 88.0
        elif self.category=="NC-OBC-cum-Transgender":
            if self.X_percent<85 or self.XII_percent<85:
                percentile = 99.7
            else:
                if self.Gender=="Male":
                    if self.Degree_cat == "Engineering":
                        percentile = 95.0
                    else:
                        percentile = 95.0
                elif self.Gender == "Female":
                    if self.Degree_cat == "Engineering":
                        percentile = 82.0
                    else:
                        percentile = 82.0
        elif self.category == "SC":
            if self.X_percent<85 or self.XII_percent<85:
                percentile = 98.7
            else:
                if self.Gender=="Male":
                    if self.Degree_cat == "Engineering":
                        percentile = 82.0 
                    else:
                        percentile = 82.0
                elif self.Gender == "Female":
                    if self.Degree_cat == "Engineering":
                        percentile = 65.0
                    else:
                        percentile = 60.0
        elif self.category == "ST":
            if self.X_percent<80 or self.XII_percent<80:
                percentile = 99.99
            else:
                if self.Gender=="Male":
                    if self.Degree_cat == "Engineering":
                        percentile = 86.0 
                    else:
                        percentile = 86.0
                elif self.Gender == "Female":
                    if self.Degree_cat == "Engineering":
                        percentile = 50
                    else:
                        percentile = 50
        elif self.category == "PWD":
            if self.X_percent<80 or self.XII_percent<80:
                percentile = 98.5
            else:
                if self.Gender=="Male":
                    if self.Degree_cat == "Engineering":
                        percentile = 92.0
                    else:
                        percentile = 90.0
                elif self.Gender == "Female":
                    if self.Degree_cat == "Engineering":
                        percentile = 55.0
                    else:
                        percentile = 50.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Indore" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IIMS(self):
        percentile = 0
        if self.category=="General":
            if self.Degree_cat == "Engineering":
                percentile = 98.0
            else:
                percentile = 96.5
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Degree_cat == "Engineering":
                percentile = 95.0
            else:
                percentile = 92.0
        elif self.category == "SC":
            if self.Degree_cat == "Engineering":
                percentile = 85
            else:
                percentile = 85
        elif self.category == "ST":
            if self.Degree_cat == "Engineering":
                percentile = 78.5
            else:
                percentile = 75
        elif self.category == "PWD":
            if self.Degree_cat == "Engineering":
                percentile = 84.0
            else:
                percentile = 85.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIM Shillong" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def newIIMs(self):
        percentile = 0
        if self.category=="General":
            if self.Degree_cat == "Engineering":
                percentile = 94.0
            else:
                percentile = 94.0
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Degree_cat == "Engineering":
                percentile = 75.0
            else:
                percentile = 75.0
        elif self.category == "SC":
            if self.Degree_cat == "Engineering":
                percentile = 54.0
            else:
                percentile = 54.0
        elif self.category == "ST":
            if self.Degree_cat == "Engineering":
                percentile = 40.0
            else:
                percentile = 40.0
        elif self.category == "PWD":
            if self.Degree_cat == "Engineering":
                percentile = 40.0
            else:
                percentile = 40.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "New IIMs" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def ISBH(self):
        percentile = "CAT Score Not Applicable"
        
        # percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        if self.Work_ex<24:
            reason.append("Minimum Work Experience of 24 months needed.")
            eligible=False
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "ISB Hyderabad" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}    
    
    def XLRI(self):
        percentile = "XAT Score Applicable"
        
        # percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "XLRI" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def FMS_Delhi(self):
        percentile = 0
        if self.category=="General":
            if self.Gender=="Male":
                percentile = 99.4
            elif self.Gender == "Female":
                percentile = 98.5
        elif self.category=="NC-OBC-cum-Transgender":
            if self.Gender=="Male":
                percentile = 97.0
            elif self.Gender == "Female":
                percentile = 94.0
        elif self.category == "SC":
            if self.Gender=="Male":
                percentile = 80.0
            elif self.Gender == "Female":
                percentile = 70.0
        elif self.category == "ST":
            if self.Gender=="Male":
                percentile = 70.0
            elif self.Gender == "Female":
                percentile = 65.0
        elif self.category == "PWD":
            if self.Gender=="Male":
                percentile = 70.0
            elif self.Gender == "Female":
                percentile = 65.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "FMS Delhi" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def SPJain(self):
        percentile = 99.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "SP Jain" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def MDI(self):
        percentile = 95.5
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=50,x_percent=50,x_percent_for_category=50,xii_percent=50,xii_percent_for_category=50)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "Management Development Institute(MDI)" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    # def JBIMS(self):
    #     percentile = "Not Available"
    #     eligible = True
    #     reason = []
    #     eligible, reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=50)
        
    #     if eligible:
    #         reason.append("You Are Eligible")
        
    #     return {'Name': "JBIMS" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def NITIE_Mumbai(self):
        percentile = 0
        if self.category=="General":
            percentile = 97.0
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 85.0
        elif self.category == "SC":
            percentile = 65.0
        elif self.category == "ST":
            percentile = 65.0
        elif self.category == "PWD":
            percentile = 75.0
        
        percentile = str(percentile)+ '+'
        eligible = True
        reason = []
        if self.Degree_cat == "Non-Engineering":
            reason.append("Engineers Only Institute")
            eligible =False
        
        if eligible:
            eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        else:
            elg,res = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
            reason.extend(res)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "NITIE Mumbai" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IIFT(self):
        percentile = "IIFT Score Required"
        eligible = True
        reason = []
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIFT" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    
    
    def TISS(self):
        percentile = "TISSNET Score Required"
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "TISS" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def SIBM(self):
        percentile = "SNAP Score Required"
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=45)
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "Symbiosis" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def NMIMS(self):
        percentile = "NMAT Score Required"
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=55,degree_percent_for_category=55)
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "NMIMS Mumbai" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def GLIM(self):
        percentile = 80
        eligible = True
        reason = []
        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=60,x_percent=60,xii_percent=60,x_percent_for_category=60,xii_percent_for_category=60)
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "Great Lakes Institute of Management, Chennai" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IMTG(self):
        percentile = "XAT Score Required"
        eligible = True
        reason = []
        eligible,reason = self.basic_elibility(degree_percent=50,degree_percent_for_category=50)
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IMT Ghaziabad" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    # def IITs(self):
    #     percentile = 0
    #     eligible = True
    #     reason = []
    #     if self.category=="General":
    #         percentile = 95
    #     elif self.category=="NC-OBC-cum-Transgender":
    #         percentile = 85 
    #     elif self.category == "SC":
    #         percentile = 75
    #     elif self.category == "ST":
    #         percentile = 60
    #     elif self.category == "PWD":
    #         percentile = 70

    #     percentile = str(percentile)+ '+'
    #     eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
    #     if eligible:
    #         reason.append("You Are Eligible")
        
    #     return {'Name': "All IITs" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IITDelhi(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 93.46
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 88.22
        elif self.category == "SC":
            percentile = 61.04
        elif self.category == "ST":
            percentile = 46.83
        elif self.category == "PWD":
            percentile = 45.65

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "DMS, IIT Delhi" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IITBombay(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 99.18
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 97.13 
        elif self.category == "SC":
            percentile = 93.69
        elif self.category == "ST":
            percentile = 81.49
        elif self.category == "PWD":
            percentile = 78.56

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "SJMSOM, IIT Bombay" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IITKGP(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 97.8
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 92.28
        elif self.category == "SC":
            percentile = 80.85
        elif self.category == "ST":
            percentile = 75.79
        elif self.category == "PWD":
            percentile = 90.66

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "VGSoM, IIT Kharagpur" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IITRoorkee(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 95.08
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 88.86
        elif self.category == "SC":
            percentile = 79.15
        elif self.category == "ST":
            percentile = 62.93
        elif self.category == "PWD":
            percentile = 66.12

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "DMS, IIT Roorkee" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    def IITMadras(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 86.47
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 68.14 
        elif self.category == "SC":
            percentile = 66.04
        elif self.category == "ST":
            percentile = 42.19
        elif self.category == "PWD":
            percentile = 78.56

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "DoMS, IIT Madras" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IITKanpur(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 95
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 88
        elif self.category == "SC":
            percentile = 81
        elif self.category == "ST":
            percentile = 73
        elif self.category == "PWD":
            percentile = 70

        percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIT Kanpur" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IITDhanbad(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 84
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = 85 
        elif self.category == "SC":
            percentile = 75
        elif self.category == "ST":
            percentile = 60
        elif self.category == "PWD":
            percentile = -1

        if percentile == -1:
            percentile = "Data unavailable"
        else:
            percentile = str(percentile)+ '+'

        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "IIT Dhanbad" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}

    def IITJodhpur(self):
        percentile = 0
        eligible = True
        reason = []
        if self.category=="General":
            percentile = 84
        elif self.category=="NC-OBC-cum-Transgender":
            percentile = -1 
        elif self.category == "SC":
            percentile = -1
        elif self.category == "ST":
            percentile = -1
        elif self.category == "PWD":
            percentile = -1

        if percentile == -1:
            percentile = "Data unavailable"
        else:
            percentile = str(percentile)+ '+'
        eligible,reason = self.basic_elibility(degree_percent=60,degree_percent_for_category=55)
        
        if eligible:
            reason.append("You Are Eligible")
        
        return {'Name': "SME, IIT Jodhpur" , 'Eligible': eligible, 'Reason':reason,'Percentile':percentile}
    
    

    def calculate(self):
        colleges = [self.IIMA, self.IIMB, self.IIMC, self.IIML, self.IIMK, self.IIMI,self.IIMS,self.ISBH,self.XLRI,self.FMS_Delhi,self.MDI,self.SPJain,self.NITIE_Mumbai,self.IIFT,self.SIBM,self.TISS,self.NMIMS,self.GLIM,self.IMTG,self.IITDelhi,self.IITBombay,self.IITKGP,self.IITRoorkee,self.IITMadras,self.IITKanpur,self.IITDhanbad,self.IITJodhpur,self.newIIMs]

        result = []
        
        for i in colleges:
            result.append(i())

        return result
    

    

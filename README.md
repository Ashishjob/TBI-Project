# **<span style="text-decoration:underline;">TBI Project:</span>**

## **<span style="text-decoration:underline;">General Information:</span>**

### **<span style="text-decoration:underline;">GCS [Glasgow Coma Scale]</span>**

* **Definition**: The GCS is a scale used to measure the extent of impaired consciousness in trauma patients, and it looks at 3 aspects of responsiveness: eyes, verbal, and motor; the scores from each add up to the total Glasgow Coma Score (3 - 15 points)
* **Eyes** [eye-opening response]:

  ```
    1. No eye opening
    2. Eye opening to pain
    3. Eye opening to sound
    4. Eyes open spontaneously
   ```
* **Verbal** [verbal response to speech]:
  ```
    1. No verbal response
    2. Incomprehensible sounds
    3. Inappropriate words
    4. Confused
    5. Orientated
* **Motor** [physical responses]:
  ```
    1. No motor response
    2. Abnormal extension to pain
    3. Abnormal flexion to pain
    4. Withdrawal from pain
    5. Localizing pain
    6. Obeys commands
* **Interferences** [these things can cause slight inaccuracies with the GCS test]:
  ```
    * Language Barriers [Can’t appropriately respond to commands if you don’t understand them]
    * Hearing loss/speech impediment [Can’t speak or hear to respond appropriately]
    * Intellectual/Neurological deficit [Brain cannot fully process commands]
    * Intubation [part of the treatment process where the tube is placed in the mouth, so the patient can’t speak]
    * Sedation [part of the treatment process, where the patient is put to sleep for procedures]
    * Orbital/Cranial Fracture [Specific factors of injuries that prevent actions part of the GCS test]
    * Spinal Cord damage [Specific factors of injuries that prevent actions part of the GCS test]
    * Hypoxic-ischemic encephalopathy [Specific factors of injuries that prevent actions part of the GCS test]
<div align=center>[^ The score is usually not calculated if any of the 3 parts of the GCS test cannot be appropriately obtained ^]</div>


* **Significance of the GSC Test:**
    * GCS helps with the early management of patients and is critical in monitoring the clinical course of a patient and guiding changes in management
    * Side note: Total score [sum of eyes, verbal, and motor] has some loss of information as it is a summary of the 3 and isn't so specific
  
----

# **<span style="text-decoration:underline;">Exploratory Analysis:</span>**


1. Find a correlation between **GCS and intoxicating substance use (drugs and alcohol)**, and from there make a predictor to predict GCS levels based on the amount of substance in the patient’s bloodstream, or if the patient has generally used these substances before.

   a. The correlation between GCS and intoxicating substances isn’t too clear but looks present. [[Evidence](https://pubmed.ncbi.nlm.nih.gov/31881342/)]

   b. **Variables**: GCSTot vs. [ALCDrinks, Drugs, and MJUse]
   
      1. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      2. **ALCDrinks** [A drink is 1 can or bottle of beer, 1 glass of wine, 1 can or bottle of wine cooler, 1 cocktail, or 1 shot of liquor. On the days when you drank, about how many drinks did you drink on the average?]:

         `666 - Variable Did Not Exist; 777 - Refused; 888 - Not Applicable; 999 - Unknown;`

      3. **Drugs** [During the year before the injury, did you use any illicit or non-prescription drugs?]:

         `0 - No; 1 - Yes; 66 - Variable Did Not Exist; 77 - Refused; 88 - Not applicable; 99 - Unknown;`

      4. **MJUse** [Did you use marijuana?]:

         `0 - No; 1 - Yes; 66 - Variable Did Not Exist; 77 - Refused; 88 - Not applicable; 99 - Unknown;`

   c. **Results:**
   
         i. Equations:
               ALCDrinks: y = -0.068x + 4.407
               Drugs: y = -0.010x + 0.340
               MJUse: y = -0.017x + 0.398
   
         ii. R-Squared Value [Model’s Accuracy]:
               ALCDrinks:  0.006 (0.6%)
               Drugs: 0.011 (1.1%)
               MJUse: 0.031 (3.1%)
   
         iii. Summary:
               Higher Previous Substance Use ~ Lower GCS; but it is not very accurate, since R-squared values are so low. The alcohol one is most interesting since it isn’t just a yes/no response but has more variance.

   d. **Graphs:**

     <div align="center"><img src="graphImages/GCS vs. Substance/GCSTot vs. ALCDrinks.png" width="300"/> <img src="graphImages/GCS vs. Substance/GCSTot vs. Drugs.png" width="300"/> <img src="graphImages/GCS vs. Substance/GCSTot vs. MJUse.png" width="300"/></div>
----   
2. Find a correlation between **GCS and age**, and from there make a predictor to predict GCS levels based on the patient’s age.

   a. [Related study’s view on it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5708017/)

   b. **Variables**: GCSTot vs. AGEnoPHI
   
      1. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      2. **AGEnoPHI** [Age of the patient]:

         `777 - 89 Years Old or Older; 999 - Unknown;`

   c. **Results:**
   
         i. Equations:
               y = 2.219x + 22.608
   
         ii. R-Squared Value [Model’s Accuracy]:
               0.189 (18.9%)
   
         iii. Summary:
               Lower Age ~ Lower GCS; but this might be an issue with fewer individuals even getting their GCS recorded at older ages from earlier deaths.

   d. **Graphs:**

     <div align="center"><img src="graphImages/GCS vs. Age/GCSTot vs. AGEnoPHI.png" width="400"/></div>
----   
2. Find a correlation between **GCS and the highest level of education attained**, and from there make a predictor to predict GCS levels based on the patient’s highest education.

   a. **Variables**: GCSTot vs. EDUCATION
   
      1. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      2. **EDUCATION** [Highest level of education that patient has received]:

         `1 - 8th Grade or Less; 2 - 9th - 11th Grade; 2.5 - GED; 3 - HS/GED; 3.5 - HS; 4 - Trade; 5 - Some College; 6 - Associate; 7 - Bachelors; 8 - Masters; 9 - Doctorate; 77 - Other; 999 - Unknown;`

   b. **Results:**
   
         i. Equations:
               y = 0.069x + 3.388
   
         ii. R-Squared Value [Model’s Accuracy]:
               0.018 (1.8%)
   
         iii. Summary:
               Lower Education ~ Lower GCS; the r-squared value is really low, and looking at the scatter plot for it shows that there really are no differential things you can notice about each category

   c. **Graphs:**

     <div align="center"><img src="graphImages/GCS vs. Education/GCSTot vs. EDUCATION.png" width="400"/></div>
----   
4. Find a correlation between **GCS and BMI**, and from there make a predictor to predict GCS levels based on the patient’s BMI.

   a. [Related study’s view on it](https://pubmed.ncbi.nlm.nih.gov/37704513/)

   b. **Variables**: GCSTot vs. BMI or BMICat
   
      1. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      2. **BMI** [BMI at injury]:

         `Free Form Data Entry Allowed`
         
      3. **BMICat** [BMI Category]
         
         `1 - Very severely underweight; 2 - Severely underweight; 3 - Underweight; 4 - Normal; 5 - Overweight; 6 - Obese Class I; 7 - Obese Class II; 8 - Obese Class III;`

   c. **Results:**
   
         i. Equations:
               BMI: y = 0.097 + 25.465
               BMICat: y = 0.018x + 4.628
   
         ii. R-Squared Value [Model’s Accuracy]:
               BMI:  0.005 (0.5%)
               BMICat: 0.005 (0.5%)
   
         iii. Summary:
               Lower BMI ~ Lower GCS; the r-squared value is really low, and looking at the scatter plot for it, I did not see any definite noticeable signs of a pattern. Also, in the scatterplot, Underweight to Obese Class III are the same.

   d. **Graphs:**

     <div align="center"><img src="graphImages/GCS vs. BMI/GCSTot vs. BMI.png" width="350"/> <img src="graphImages/GCS vs. BMI/GCSTot vs. BMICat.png" width="350"/></div>
----   
5. Find a correlation between **GCS and speed of relative recovery**, and from there make a predictor to predict GCS levels based on the patient’s speed of recovery.

   a. [Related study’s view on it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298893/)

   b. **Variables**: GCSTot vs. TFCDays
   
      1. **GCSTot** [Days From Injury to Follow Commands]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      2. **TFCDays** [Days From Injury to Follow Commands]:

         `7777 - Patient Never Able to Follow Simple Motor Commands; 9999 - Unknown;`

   c. **Results:**
   
         i. Equations:
               y = -1.135x + 18.253
   
         ii. R-Squared Value [Model’s Accuracy]:
               0.170 (17%)
   
         iii. Summary:
               Longer Recovery Time ~ Lower GCS, pretty intuitive understanding that more severe cases take longer to recover from, so might be pointless.

   d. **Graphs:**

     <div align="center"><img src="graphImages/GCS vs. Recovery Speed/GCSTot vs. TFCDays.png" width="400"/></div>
----   
6. Find a correlation between the **speed of relative recovery and GCS separate scores and total score**, and from there make a predictor to predict the speed of relative recovery based on the patient’s GCS Scale’s separate scores and total score.

   a. **Variables**: GCSTot vs. [ALCDrinks, Drugs, and MJUse]

      1. **TFCDays** [Days From Injury to Follow Commands]:

         `7777 - Patient Never Able to Follow Simple Motor Commands; 9999 - Unknown;`

      2. **GCSEye** [GCS Eye opening]:

         `1 - None; 2 - To Pain; 3 - To Voice; 4 - Spontaneous; 7 - Chemically Paralyzed or Sedated; 99 - Unknown;`
   
      3. **GCSVer** [GCS Verbal]:

         `1 - None; 2 - Incomprehensible Sounds; 3 - Inappropriate Speech; 4 - Confused; 5 - Oriented; 7 - Chemically Paralyzed or Sedated; 8 - Intubated; 99 - Unknown;`

      4. **GCSMot** [GCS Motor]: 

         `1 - None; 2 - Extension to Pain; 3 - Flexion to Pain; 4 - Withdraws from Pain; 5 - Localizes Pain; 6 - Obeys Commands; 7 - Chemically Paralyzed or Sedated; 99 - Unknown;`
         
      5. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`
   
   b. **Results:**
   
         i. Equations:
               GCSEye: y = -0.04x + 2.933
               GCSVer: y = -0.053x + 3.64
               GCSMot: y = -0.055x + 5.235
               GCSTot: y = -0.15x + 12.127
      
         ii. R-Squared Value [Model’s Accuracy]:
               GCSEye: 0.136 (13.6%)
               GCSVer: 0.141 (14.1%)
               GCSMot: 0.146 (14.6%)
               GCSTot: 0.171 (17.1%)
   
         iii. Summary:
               Higher Score ~ Shorter Recovery Time, the accuracy of each one is about the same and nothing really stands out in the scatter graph, but there do seem to be places of potential for further digging in terms of patterns.

   d. **Graphs:**

     <div align="center"> <img src="https://github.com/Ashishjob/TBI-Project/blob/main/graphImages/Recovery%20Speed%20vs.%20GCS%20Separate%20Scores/TFCdays%20vs.%20GCSEye.png" width="350"/> <img src="https://github.com/Ashishjob/TBI-Project/blob/main/graphImages/Recovery%20Speed%20vs.%20GCS%20Separate%20Scores/TFCDays%20vs.%20GCSVer.png" width="350"/> <img src="https://github.com/Ashishjob/TBI-Project/blob/main/graphImages/Recovery%20Speed%20vs.%20GCS%20Separate%20Scores/TFCdays%20vs.%20GCSMot.png" width="350"/> <img src="https://github.com/Ashishjob/TBI-Project/blob/main/graphImages/Recovery%20Speed%20vs.%20GCS%20Separate%20Scores/TFCdays%20vs.%20GCSTot.png" width="350"/></div>
----     

# **<span style="text-decoration:underline;">Used Sources:</span>**


* [TBIMS Data Dictionary Explorer](https://hub.tbindsc.org/tbimsdatadictionary/Home) 
* [Glasgow Coma Scale - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK513298/)
* [The Impact of Drug and Alcohol Intoxication on Glasgow Coma Scale Assessment in Patients with Traumatic Brain Injury](https://pubmed.ncbi.nlm.nih.gov/31881342/) 
* [Effect of Age on Glasgow Coma Scale in Patients with Moderate and Severe Traumatic Brain Injury: An Approach with Propensity Score-Matched Population - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5708017/) 
* [The impact of body mass index changes on traumatic brain injury patients' outcomes during hospitalization](https://pubmed.ncbi.nlm.nih.gov/37704513/) 
* [Gait and Glasgow Coma Scale scores can predict functional recovery in patients with traumatic brain injury - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298893/) 
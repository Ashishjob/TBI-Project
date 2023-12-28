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
<h5 align = center>[^ The score is usually not calculated if any of the 3 parts of the GCS test cannot be appropriately obtained ^]</h5>


* **Significance of the GSC Test:**
    * GCS helps with the early management of patients and is critical in monitoring the clinical course of a patient and guiding changes in management
    * Side note: Total score [sum of eyes, verbal, and motor] has some loss of information as it is a summary of the 3 and isn't so specific
  
----

# **<span style="text-decoration:underline;">Project Ideas:</span>**



1. Find a correlation between **GCS and intoxicating substance use (drugs and alcohol)**, and from there make a predictor to predict GCS levels based on the amount of substance in the patient’s bloodstream, or if the patient has generally used these substances before.

   a. The correlation between GCS and intoxicating substances isn’t too clear but looks present. [[Evidence](https://pubmed.ncbi.nlm.nih.gov/31881342/)]

   b. **Variables**: GCSTot vs. [ALCDrinks, Drugs, and MJUse]
   
      1. **GCSTot** [GCS Total]: 

         `3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;`

      3. **ALCDrinks** [A drink is 1 can or bottle of beer, 1 glass of wine, 1 can or bottle of wine cooler, 1 cocktail, or 1 shot of liquor. On the days when you drank, about how many drinks did you drink on the average?]:

         `666 - Variable Did Not Exist; 777 - Refused; 888 - Not Applicable; 999 - Unknown;`

      4. **Drugs** [During the year before the injury, did you use any illicit or non-prescription drugs?]:

         `0 - No; 1 - Yes; 66 - Variable Did Not Exist; 77 - Refused; 88 - Not applicable; 99 - Unknown;`

      6. **MJUse** [Did you use marijuana?]:

         `0 - No; 1 - Yes; 66 - Variable Did Not Exist; 77 - Refused; 88 - Not applicable; 99 - Unknown;`

   c. **Results:**
   
         i. Equations:
               Alcohol: y = -0.068x + 4.407
               Drugs: y = -0.010x + 0.340
               Marijuana: y = -0.017x + 0.398
   
         ii. R-Squared Value [Model’s Accuracy]:
               Alcohol:  0.006 (0.6%)
               Drugs: 0.011 (1.1%)
               Marijuana: 0.031 (3.1%)
   
         iii. Summary:
               Higher Previous Substance Use ~ Lower GCS; but it is not very accurate, since R-squared values are so low. The alcohol one is most interesting since it isn’t just a yes/no response but has more variance.
   
3. Find a correlation between **GCS and age**, and from there make a predictor to predict GCS levels based on the patient’s age.
    4. [Related study’s view on it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5708017/)
    5. **Variables**: GCSTot vs. AGEnoPHI
        8. **GCSTot** [GCS Total]: 
            11. 3 - 15 - Marked Score;  77 - Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;
        9. **AGEnoPHI** [Age of the patient]
            12. 777 - 89 Years Old or Older; 999 - Unknown;
    6. **Results**:
        10. **Equations**:
            13. y = 2.219x + 22.608
        11. **R-Squared Value [Model’s Accuracy]**:
            14. 0.189 (18.9%)
        12. **Summary**: Lower Age ~ Lower GCS; but this might be an issue with fewer individuals even getting their GCS recorded at older ages from earlier deaths.
4. Find a correlation between **GCS and the highest level of education attained**, and from there make a predictor to predict GCS levels based on the patient’s highest education.
    7. **Variables**: GCSTot vs. EDUCATION
        13. **GCSTot** [GCS Total]: 
            15. 3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;
        14. **EDUCATION** [Highest level of education that patient has received]:
            16. 1 - 8th Grade or Less; 2 - 9th - 11th Grade; 2.5 - GED; 3 - HS/GED; 3.5 - HS; 4 - Trade; 5 - Some College; 6 - Associate; 7 - Bachelors; 8 - Masters; 9 - Doctorate; 77 - Other; 999 - Unknown;
    8. **Results**:
        15. **Equation**:
            17. y = 0.069x + 3.388
        16. **R-Squared Value [Model’s Accuracy]**:
            18. 0.018 (1.8%)
        17. **Summary**: Lower Education ~ Lower GCS; the r-squared value is really low, and looking at the scatter plot for it shows that there really are no differential things you can notice about each category
5. Find a correlation between **GCS and BMI**, and from there make a predictor to predict GCS levels based on the patient’s BMI.
    9. [Related study’s view on it](https://pubmed.ncbi.nlm.nih.gov/37704513/)
    10. **Variables**: GCSTot vs. BMI or BMICat
        18. **GCSTot** [GCS Total]: 
            19. 3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;
        19. **BMI** [BMI at injury]:
            20. Free Form Data Entry Allowed
        20. **BMICat** [BMI Category]:
            21. 1 - Very severely underweight; 2 - Severely underweight; 3 - Underweight; 4 - Normal; 5 - Overweight; 6 - Obese Class I; 7 - Obese Class II; 8 - Obese Class III;
    11. **Results**:
        21. **Equations**:
            22. **BMI**: y = 0.097 + 25.465
            23. **BMICat**: y = 0.018x + 4.628
        22. **R-Squared Value [Model’s Accuracy]**:
            24. **BMI**: 0.005 (0.5%)
            25. **BMICat**: 0.005 (0.5%)
        23. **Summary**: Lower BMI ~ Lower GCS; the r-squared value is really low, and looking at the scatter plot for it, I did not see any definite noticeable signs of a pattern. Also, in the scatterplot, Underweight to Obese Class III are the same.
6. Find a correlation between **GCS and speed of relative recovery**, and from there make a predictor to predict GCS levels based on the patient’s speed of recovery.
    12. [Related study’s view on it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298893/)
    13. **Variables**: GCSTot vs. TFCDays
        24. **GCSTot** [GCS Total]: 
            26. 3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;
        25. **TFCDays** [Days From Injury to Follow Commands]:
            27. 7777 - Patient Never Able to Follow Simple Motor Commands; 9999 - Unknown;
    14. **Results**:
        26. **Equation**: 
            28. y = -1.135x + 18.253
        27. **R-Squared Value [Model’s Accuracy]**: 
            29. 0.170 (17%)
        28. **Summary**: Longer Recovery Time ~ Lower GCS, pretty intuitive understanding that more severe cases take longer to recover from, so might be pointless.
7. Find a correlation between the **speed of relative recovery and GCS separate scores and total score**, and from there make a predictor to predict the speed of relative recovery based on the patient’s GCS Scale’s separate scores and total score.
    15. [Related study’s view on it](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298893/)
    16. **Variables**: TFCDays vs. [GCSEye, GCSVer, GCSMot, GCSTot]
        29. **TFCDays** [Days From Injury to Follow Commands]:
            30. 7777 - Patient Never Able to Follow Simple Motor Commands; 9999 - Unknown;
        30. **GCSEye** [GCS Eye opening]:
            31. 1 - None; 2 - To Pain; 3 - To Voice; 4 - Spontaneous; 7 - Chemically Paralyzed or Sedated; 99 - Unknown;
        31. **GCSVer** [GCS Verbal]:
            32. 1 - None; 2 - Incomprehensible Sounds; 3 - Inappropriate Speech; 4 - Confused; 5 - Oriented; 7 - Chemically Paralyzed or Sedated; 8 - Intubated; 99 - Unknown;
        32. **GCSMot** [GCS Motor]:
            33. 1 - None; 2 - Extension to Pain; 3 - Flexion to Pain; 4 - Withdraws from Pain; 5 - Localizes Pain; 6 - Obeys Commands; 7 - Chemically Paralyzed or Sedated; 99 - Unknown;
        33. **GCSTot** [GCS Total]: 
            34. 3 - 15: Marked Score;  77: Chemically Paralyzed or Sedated; 88 - Intubated; 999 - Unknown;
    17. **Results**:
        34. **Equations**:
            35. **GCSEye**: y = -0.04x + 2.933
            36. **GCSVer**: y = -0.053x + 3.64
            37. **GFCMot**: y = -0.055x + 5.235
            38. **GFCTot**: y = -0.15x + 12.127
        35. **R-Squared Values [Model’s Accuracy]**:
            39. **GCSEye**: 0.136 (13.6%)
            40. **GCSVer**: 0.141 (14.1%)
            41. **GCSMot**: 0.146 (14.6%)
            42. **GCSTot**: 0.171 (17.1%)
        36. **Summary**:


# **<span style="text-decoration:underline;">Used Sources:</span>**


* [TBIMS Data Dictionary Explorer](https://hub.tbindsc.org/tbimsdatadictionary/Home) 
* [Glasgow Coma Scale - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK513298/)
* [The Impact of Drug and Alcohol Intoxication on Glasgow Coma Scale Assessment in Patients with Traumatic Brain Injury](https://pubmed.ncbi.nlm.nih.gov/31881342/) 
* [Effect of Age on Glasgow Coma Scale in Patients with Moderate and Severe Traumatic Brain Injury: An Approach with Propensity Score-Matched Population - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5708017/) 
* [The impact of body mass index changes on traumatic brain injury patients' outcomes during hospitalization](https://pubmed.ncbi.nlm.nih.gov/37704513/) 
* [Gait and Glasgow Coma Scale scores can predict functional recovery in patients with traumatic brain injury - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4298893/) 
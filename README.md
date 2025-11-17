# MLZoomcamp2025_Midterm1


🐾 ML_Zoomcamp_2025 – Austin Animal Center Project

Problem Statement -What we’re trying to predict:  
This project predicts whether a pet entering the Austin Animal Center will be adopted or not. Using information such as animal type, breed, intake condition, and other relevant attributes, the model outputs a probability of adoption for each animal.  

1. Dataset- data folder  
   
This project uses public datasets from the Austin Animal Center, which include:    
• 	Intakes: Records of animals entering the shelter    
	Outcomes: Records of animals leaving the shelter    

These datasets contain information such as animal type, breed, intake reason, outcome type, and dates.    

2. ,EDA , Data Cleaning   
The notebook performs the following preprocessing steps:    
• 	✅ Loads both datasets and merges them on animal_ID  <br>
• 	✅ Filters out irrelevant columns and handles missing values  <br>
• 	✅ Converts date columns to datetime format  <br>
• 	✅ Encodes categorical features (e.g., animal type, intake condition)  <br>
• 	✅ Creates a binary target column:  (e.g., Adopted vs. Not Adopted)  <br>

Feature Selection :
categorical = ["intake_type", "intake_condition", "animal_type", "sex_upon_intake", "breed", "color"]<br>
numeric = ["month", "year"]

3. Model <br>
The model used is a Random Forest Classifier, trained to predict the outcome of an animal based on:<br>
• 	Animal type and breed<br>
• 	Intake condition and type<br>
• 	Age upon intake<br>
• 	Time spent in shelter<br>
Output: Predicted outcome category (e.g., Adopted, Returned to Owner)<br>


5. Train the Model<br>
To train the model, run the notebook . It will:<br>
• 	Load and clean the data<br>
• 	Engineer features and encode categories<br>
• 	Split into training and test sets<br>
• 	Train the model and evaluate performance<br>


7. Make Predictions<br>  
The notebook includes examples of predicting outcomes for new animal entries. You can modify the input features to test different scenarios.<br>


9. FastAPI Service <br>  
To deploy the model as an API:<br>  

• 	Interactive docs: http://localhost:8000/docs
<br>  
  
7. Docker Deployment <br>
To containerize the API:

docker build -t pet-adoption-fastapi .  <br>
docker run -p 8000:8000 pet-adoption-fastapi <br>
<br>
API will be available at http://localhost:8000/docs    <br>
Health check: curl http://localhost:8000/health

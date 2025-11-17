# MLZoomcamp2025_Midterm1


🐾 ML_Zoomcamp_2025 – Austin Animal Center Project

1. Dataset- data folder
   
This project uses public datasets from the Austin Animal Center, which include:  
• 	Intakes: Records of animals entering the shelter  
	Outcomes: Records of animals leaving the shelter  

These datasets contain information such as animal type, breed, intake reason, outcome type, and dates.  

2. Data Cleaning Pipeline  
The notebook performs the following preprocessing steps:  
• 	✅ Loads both datasets and merges them on animal_ID  
• 	✅ Filters out irrelevant columns and handles missing values  
• 	✅ Converts date columns to datetime format  
• 	✅ Encodes categorical features (e.g., animal type, intake condition)  
• 	✅ Creates a binary target column:  (e.g., Adopted vs. Not Adopted)  

Feature Selection :
categorical = ["intake_type", "intake_condition", "animal_type", "sex_upon_intake", "breed", "color"]
numeric = ["month", "year"]

3. Model 
The model used is a Random Forest Classifier, trained to predict the outcome of an animal based on:
• 	Animal type and breed
• 	Intake condition and type
• 	Age upon intake
• 	Time spent in shelter
Output: Predicted outcome category (e.g., Adopted, Returned to Owner)

4. Train the Model
To train the model, run the notebook . It will:
• 	Load and clean the data
• 	Engineer features and encode categories
• 	Split into training and test sets
• 	Train the model and evaluate performance

5. Make Predictions
The notebook includes examples of predicting outcomes for new animal entries. You can modify the input features to test different scenarios.

6. FastAPI Service 
To deploy the model as an API:

• 	Interactive docs: http://localhost:8000/docs

7. Docker Deployment 
To containerize the API:

docker build -t pet-adoption-fastapi .  

docker run -p 8000:8000 pet-adoption-fastapi

API will be available at http://localhost:8000/docs
Health check: curl http://localhost:8000/health

# MLZoomcamp2025_Midterm1


🐾 ML_Zoomcamp_2025 – Austin Animal Center Project
1. Dataset
This project uses public datasets from the Austin Animal Center, which include:
• 	Intakes: Records of animals entering the shelter
Download CSV
• 	Outcomes: Records of animals leaving the shelter
Download CSV
These datasets contain information such as animal type, breed, intake reason, outcome type, and dates.
2. Data Cleaning Pipeline
The notebook performs the following preprocessing steps:
• 	✅ Loads both datasets and merges them on 
• 	✅ Filters out irrelevant columns and handles missing values
• 	✅ Converts date columns to datetime format
• 	✅ Encodes categorical features (e.g., animal type, intake condition)
• 	✅ Creates a binary target column:  (e.g., Adopted vs. Not Adopted)
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
6. FastAPI Service (Optional Extension)
To deploy the model as an API:

• 	Interactive docs: http://localhost:8000/docs
• 	Example request body:

7. Docker Deployment (Optional)
To containerize the API:

API will be available at http://localhost:8000/docs

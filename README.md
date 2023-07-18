# HR_Attrition_Analysis_Modelbuilding
# HR Attrition Analysis Model Building

This repository contains the code and resources for building a machine learning model to predict employee attrition in the HR domain. The model is trained on a dataset that includes various features related to employees, such as age, gender, education level, salary, performance rating, work-life balance, employee satisfaction, training hours, years in current role, years since last promotion, and years with current manager.

## Dataset

The dataset used for this analysis is located in the `data` directory. It contains the following files:

- `workforce.csv`: The main dataset file in CSV format, which includes the employee features and the target variable (attrition).

## Model Building

The model building process is detailed in the Jupyter Notebook `Hr analytics mine model scaling.ipynb`. It covers the following steps:

1. Data preprocessing: handling missing values, encoding categorical variables, and feature scaling.
2. Exploratory data analysis: visualizing the relationships between features and the target variable.
3. Model selection: evaluating various machine learning models and selecting the best performing one.
4. Model training: fitting the selected model on the preprocessed dataset.
5. Model evaluation: assessing the model's performance using appropriate metrics.
6. Saving the model: serializing the trained model using pickle and saving it as `model.pkl`.

## Requirements

The required Python packages and their versions for running the code in this repository are listed in the `requirements.txt` file.

To install the dependencies, run the following command:


## Usage

To use the trained model for predicting employee attrition, follow these steps:

1. Ensure that you have installed the required dependencies (see Requirements section).
2. Run the Jupyter Notebook `Hr analytics mine model scaling.ipynb` to train and save the model as `model.pkl`.
3. Open the `modelhr1.html` file in a web browser.
4. Enter the employee details in the input fields provided.
5. Click on the "Predict Attrition" button.
6. The predicted attrition result will be displayed in the colored box below.

## Contributing

Contributions to this repository are welcome. If you have suggestions for improvement or find any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

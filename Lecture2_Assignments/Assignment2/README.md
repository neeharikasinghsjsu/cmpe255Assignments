# Assignment 2: pycaret
[Binary Classification](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_binaryclassification.ipynb)

A dataset used has details about **loan**.It contains the following data.
<ol>
  <li>loan_id :  An identifier for the loan.</li>
  <li>no_of_dependents:  Number of dependents of the loan applicant.</li>
  <li>education: Education level of the loan applicant (e.g., Graduate, Not Graduate).</li>
  <li>self_employed: Whether the loan applicant is self-employed or not.</li>
  <li>income_annum: Annual income of the loan applicant.</li>
  <li>loan_amount: The amount of loan requested.</li>
  <li>loan_term: The term (duration) for which the loan is requested.</li>
  <li>cibil_score: CIBIL score of the loan applicant (a measure of creditworthiness).</li>
  <li>residential_assets_value: Value of residential assets owned by the applicant.</li>
  <li>commercial_assets_value: Value of commercial assets owned by the applicant.</li>
  <li>luxury_assets_value: Value of luxury assets owned by the applicant.</li>
  <li>bank_asset_value: Value of assets in the bank.</li>
  <li>loan_status: The decision on the loan application (e.g., Approved, Rejected).</li>
</ol>

The prediction model **Extreme Gradient Boosting** has been used to determine the **loan_status** of an application as 

<ul>
  <li>Approved</li>
  <li>Rejected</li>
</ul>

[Multiclass Classification](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_multiclassclassification.ipynb)

The dataset used has details about the **complaints**. It contains the following data
<ol>
  <li>complaint_number:  An identifier for the complaints.</li>
  <li>complaint_type:  The complaint category listed below :
      <ul>
        <li>credit_reporting</li>
        <li>mortgages_and_loans</li>
        <li>retail_banking</li>
        <li>debt_collection</li>
        <li>credit_card</li>
      </ul>
  </li>
  
  <li>narrative: The content of the complaint in a textual format.</li>
</ol>

The data model **K Neighbors Classifier**	has been used to predict the **complaint category** based on the narrative.

[Regression](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_regression.ipynb)

The dataset used has details about the laptop specifications and the prices. It has the following data.
<ol>
  <li>brand: The brand of the laptop (e.g., LENOVO, ASUS).</li>
  <li>operating_system: The operating system installed on the laptop (e.g., WINDOWS).</li>
  <li>RAM_nth: The rank of the laptop's RAM size.</li>
  <li>storage_nth: A transformed representation of the laptop's storage capacity.</li>
  <li>storage_type: The type of storage used in the laptop (e.g., SSD).</li>
  <li>cpu_benchmark: A benchmark score representing the laptop's CPU performance.</li>
  <li>gpu_class: A class or category indicating the laptop's GPU performance.</li>
  <li>screen_size: The size of the laptop's screen in inches.</li>
  <li>PPI: Pixels per inch, indicating the screen resolution.</li>
  <li>warranty: Duration of the warranty in years.</li>
  <li>refurbished: Whether the laptop is refurbished or not.</li>
  <li>price: The price of the laptop.</li>
</ol>

The model **GradientBoostingRegressor** has been used to predict the **price** of the laptop

[Clustering](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_clustering.ipynb)

[Anomaly Detection](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_anomaly.ipynb)

[Association Rules Mining](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_association_rules.ipynb)

[Time Series Forecasting - Univariate without Exogenous Variables](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_timeseries_univariate_without_exogenous.ipynb)

[Time Series Forecasting - Univariate with Exogenous Variables](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/pycaret_timeseries_with_exogenous.ipynb)


# Gradio

[Gradio demonstration binary classification](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/gradio/gradio_binary_classification.m4v)

[Gradio demonstration regression](https://github.com/neeharikasinghsjsu/cmpe255assignments/blob/main/Lecture2_Assignments/Assignment2/gradio/gradio_regression.m4v)

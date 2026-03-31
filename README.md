# Fuzzy Toy Factory: An E-commerce Project

## ✨ Summary 
This is an end-to-end data project that analyzes customer behavior of an e-commerce business and predict their purchase intent. It includes a ETL pipeline, RFM-based customer segmentation, and a conversion propensity model that could detect 83% of high-intent sessions and achieved a 2.35x increase in targeting effectiveness.

## 🎯 Project Objective
The main objective of this project is to use raw e-commerce websession data to identiy which web sessions are most likely to convert into a real purchase. By identifying high-value customers and predicting which web sessions are likely to convert, businesses can optimize marketing budget and improve targeting efficiency.

## 💻 Technical Stack
- __Language__: Python 3.12
- __Libraries__: Pandas, Scikit-Learn, Matplotlib, Seaborn
- __Tools__: git, Github, uv

## 🔑 Key Features
1. __ETL Pipeline__: A Python-based pipeline that export raw data from CSV files, perform categorical imputation and temporal features engineering, and load it into a separate folder.

2. __RFM Segmentation__: Cluster customers into value-based tiers (Low, Medium, High) using RFM (Recency, Frequency, Monetary) scores and K-means clustering.

3. __Conversion Propensity Model__: Experiment with 3 different ML algorithms and different methods to address class imbalance, as well as feature engineering to find the best model, which could identify 83% "high-intent" sessions and a 2.35x lift in targeting efficiency over the baseline conversion rate.

## 💼 Results & Business Impact

1. __Recall and its implication__

    The best-performing model is Balanced Random Forest with a recall of 0.83. This means the model is capable of identifying 83% high-intent customers through their actions on the website. This allows the business to carry out live intervention on the customers or allocate their marketing resource better, successfully achieving the project objective with from just web session data.

1. __Precision and its implication__

    The model achieved a precision of 0.16, which is not considered high in the tradition lens. However, to translate this result in the real-world setting, it means that for every 100 people targeted by our campaigns, 16 ended up making a purchase, raising the conversion rate to 16%. Given that the current conversion rate of the business is 6.8%, this is a 2.53x Lift. This will help the business improve in targeting efficiency of automated sales triggers.



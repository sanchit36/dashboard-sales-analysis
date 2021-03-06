# dashboard-sales-analysis

A sales analysis dashboard built with streamlit and plotly for data science project

# Screenshot

<img src="https://raw.githubusercontent.com/sanchit36/dashboard-sales-analysis/master/screenshot/Dashboard.png" alt="Dashboard" />

# Dataset

I have used dataset of Supermarket sales from Kaggle.

[https://www.kaggle.com/aungpyaeap/supermarket-sales](https://www.kaggle.com/aungpyaeap/supermarket-sales)

# Live Demo

You can see the live demo, [here](https://bhadgal-dashboard-sales.herokuapp.com/).

# How to run

```bash
  $ git clone https://github.com/sanchit36/dashboard-sales-analysis.git
  $ cd dashboard-sales-analysis
  $ pip install -r requirements.txt
  $ streamlit run app.py
```

# About the analysis

I am going to analyse the supermarket-sales dataset from Kaggle. In particular, I am interested in relationships between some of the variables as well as differences between certain characteristics of some of the variables regarding the Revenues. In particular, I would like to explore the following questions:

- Is there a connection between Gender and Customer type?
- Is there a connection between Gender and Product Line? Do the sexes prefer different product types?
- Is there a connection between Gender and Cities? Do the sexes distribute themselves differently among the cities?
- Is there a connection between Gender and Payment? Do the sexes differ in their chosen payment method?

## Figure 1 - Gross Income vs Gender

Shows that **Females** contribute more to the total gross income for the supermarket sales.

## Figure 2 - Gross Income vs Customer Type

We have two types of the customer

- Member
- Normal

Chart shows that **Members** contribute more to the total gross income for the supermarket sales and in Members Gender **Female** contribute more to the total gross income.

## Figure 3 - Gross Income per Product line

We have 6 different types of the product line.

- Health and beauty
- Electronics accessories
- Food and beverages
- Fashion accessories
- Sports and Travel
- Home and lifestyle

We have a 2 face bar graph plot in this figure, **faced by Customer type and group by Gender**

- **Food and beverages** generates the most gross income in female that are members
- **Heath and Beauty** generates the most gross income in male that are members
- **Electronics accessories** generated the most gross income in female that are normal
- **Sports and Travel** generated the most gross income in male that are normal

## Figure 4 - Gross Income vs City

We have 3 different types of the City.

- Yangon
- Naypyitaw
- Mandalay

This bar plot shows that

- That all the cities generate almost the same amount of the gross income
- Naypyitaw **Females** generate more sales than **Males**
- Other two cities gender is distributed almost equally

## Figure 5 - Payment type vs Gender

We have 3 different types of the Payment types.

- Cash
- E wallet
- Credit card

The pie chart below shows

- All the payment types is almost equally distributed
- **35.4% Females** payed using **cash**
- **35.5% Males** payed using **E wallet**

## Figure 6 - Ratings per Product line

The 6 face bar chart below shows

- distribution of average rating between Customer types of the different cities
- For City **Mandalay**
  - **Heath and beauty** is the highest rated among **female member customer**
  - **Food and beverages** is the highest rated among **female normal customer**
  - **Electronics accessories** is the highest rated among **male member customer**
  - **Heath and Beauty and Fashion accessories** is the highest rated among **male normal customer**
- For City **Naypyitaw**
  - **Fashion accessories** is the highest rated among **female member customer**
  - **Food and beverages** is the highest rated among **female normal customer**
  - **Sports and Travel** is the highest rated among **male member customer**
  - **Sports and Travel** is the highest rated among **male normal customer**
- For City **Yangon**
  - **Sports and Travel** is the highest rated among **female member customer**
  - **Heath and beauty** is the highest rated among **female normal customer**
  - **Sports and Travel** is the highest rated among **male member customer**
  - **Food and beverages** is the highest rated among **male normal customer**

## Figure 7 - Gross Income Hour Wise

- Supermarket gets most sales **13:00 hr** from the female customers
- Supermarket gets most sales **19:00 hr** from the male customers
- most of the sales is between **13:00 hr** to **19:00 hr**

# Conclusion

- Most sales come from female customers **(52%)**
- 501 members and 499 normal customers
- Im members more number of female customers
- more sales is generated from female customers
- Food and beverages makes most income in female members customers, where as heath and beauty in males member customers
- Naypyitaw makes the most income
- there is equally distribution for payment types
- Mandalay city provides the most highest ratings
- most of the sales is between 13:00 hr to 19:00 hr

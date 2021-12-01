import pandas as pd
import plotly.express as px
import streamlit as st

from components import get_sidebar, getKpi

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)


# ---- READ CSV ----
@st.cache
def get_data_from_csv():
    df = pd.read_csv("./supermarket_sales.csv")
    df["hour"] = pd.to_datetime(df["Time"]).dt.hour
    return df


df = get_data_from_csv()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
elements = [
    {
        "label": "Select the City:",
        "feature_name": "City",
        "error": "Please select at a city"
    },
    {
        "label": "Select the Customer Type:",
        "feature_name": "Customer_type",
        "error": "Please select at least a customer type"
    },
]
[city, customerType] = get_sidebar(st, df, elements)

# ---- MAINPAGE ----
st.markdown('''
# :bar_chart: Sales Dashboard
**Developed By: Sanchit Bhadgal**
''')

if (len(city) > 0) and (len(customerType) > 0):
    df_selection = df.query("City == @city & Customer_type == @customerType")

    # KPIs
    total_sales = int(df_selection["Total"].sum())
    average_rating = round(df_selection["Rating"].mean(), 1)
    star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        getKpi(st, "Total Sales:", f"US $ {total_sales:,}")
    with middle_column:
        getKpi(st, "Average Rating:", f"{average_rating} {star_rating}")
    with right_column:
        getKpi(st, "Average Sales Per Transaction:", f"US $ {average_sale_by_transaction:,}")

    st.markdown("""---""")

    # Pie Chart For Gender
    pie_gender = px.pie(
        df_selection,
        values="gross income",
        names="Gender",
        title="<b>Gross Income vs Gender</b>",
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        labels={
            "Gender": "Gender",
            "gross income": "Gross Income"
        },
        template="plotly_white",
    )


    # Bar Chart for Customer Type
    df_customer = df_selection.groupby(['Gender','Customer_type']).sum().reset_index()
    bar_gender_customer = px.bar(
        df_customer,
        x="Customer_type",
        y="gross income",
        title="<b>Gross Income vs Customer Type</b>",
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        template="plotly_white",
        barmode="group",
        labels={
            "Customer_type": "Customer Type",
            "gross income": "Gross Income"
        },
    )
    bar_gender_customer.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    # Sales Product line
    df_pl = df_selection.groupby(['Gender', 'Product line','Customer_type']).sum().reset_index()
    sales_product_line = px.bar(
        df_pl,
        x="Product line",
        y="gross income",
        title="<b>Gross Income per Product Line</b>",
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        template="plotly_white",
        barmode="group",
        facet_col="Customer_type",
        labels={
            "Product line": "Product Line",
            "gross income": "Gross Income",
            "Customer_type": "Customer Type",
        },
    )
    sales_product_line.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
    )

    c1, c2, c3 = st.columns(3)
    c1.plotly_chart(pie_gender, use_container_width=True)
    c2.plotly_chart(bar_gender_customer, use_container_width=True)
    c3.plotly_chart(sales_product_line, use_container_width=True)


    # Sales per city
    df_city = df_selection.groupby(['Gender', 'City']).sum().reset_index()
    sales_gender_city = px.bar(
        df_city,
        x="City",
        y="gross income",
        title="<b>Gross Income vs City</b>",
        labels={
            "City": "City",
            "gross income": "Gross Income"
        },
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        barmode="group",
        template="plotly_white",
    )
    sales_gender_city.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
    )

    # Ratings
    df_rating = df_selection.groupby(['Gender', 'Product line', 'City', 'Customer_type']).mean().reset_index()
    ratings = px.bar(
        df_rating,
        x="Product line",
        y="Rating",
        title="<b>Rating per Product Line</b>",
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        template="plotly_white",
        barmode="group",
        facet_col="Customer_type",
        facet_row="City",
        labels={
            "Product line": "Product Line",
            "gross income": "Gross Income",
            "Customer_type": "Customer Type",
        },
    )
    ratings.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        showlegend=False,
    )

    c1, c2, c3 = st.columns(3)
    c1.plotly_chart(sales_gender_city, use_container_width=True)
    with c2:
        # Payment
        options = st.multiselect(
            'Select a gender',
            df['Gender'].unique(),
            df['Gender'].unique(),
        )
        new_df = df.query('Gender == @options')
        pie_payment = px.pie(
            new_df,
            names="Payment",
            values="gross income",
            title="<b>Payment Type vs Gender</b>",
            hover_data=['Quantity'],
            color="Payment",
            color_discrete_map={
                'Cash': 'royalblue',
                'Ewallet': 'darkblue',
                'Credit card': 'cyan',
            },
            template="plotly_white",
        )
        st.plotly_chart(pie_payment, use_container_width=True)
    c3.plotly_chart(ratings, use_container_width=True)

    # Line Graph
    c1, c2 = st.columns(2)
    df_hours_group = df_selection.groupby(["Gender", "hour"]).sum().reset_index()
    sales_per_hour = px.line(
        df_hours_group,
        x="hour",
        y="gross income",
        title="<b>Gross Income Hour Wise</b>",
        color="Gender",
        color_discrete_map={
            'Female': 'royalblue',
            'Male': 'darkblue'
        },
        template="plotly_white"
    )
    sales_per_hour.update_traces(hoverinfo='text+name', mode='lines+markers')
    sales_per_hour.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    c1.plotly_chart(sales_per_hour, use_container_width=True)


else:
    st.text("Please provide valid input")

# ---- HIDE STREAMLIT STYLE ----
padding = 1
hide_st_style = f"""
            <style>
                #MainMenu {{visibility: hidden;}}
                footer {{visibility: hidden;}}
                header {{visibility: hidden;}}
                .reportview-container .main .block-container{{
                    padding-top: {padding}rem;
                    padding-bottom: {padding}rem;
               }}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

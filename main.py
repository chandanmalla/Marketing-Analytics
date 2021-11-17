import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
# from autoviz.AutoViz_Class import AutoViz_Class
from scipy import stats  ## for KS test
from prettytable import PrettyTable
from PIL import Image
import time
import plotly.express as px
import streamlit as st
from pywaffle import Waffle
st.set_page_config(page_title='Marketing Analytics Project', page_icon='image/flipkart_icon-icons.com_62718.png', layout="wide", initial_sidebar_state="auto", menu_items=None)

combined_data = pd.read_csv('data/Combined_data-Part_3.csv')

image = Image.open('image/Picture1.png')
st.sidebar.image(image, width=280)
st.sidebar.title('MG241')
st.sidebar.title('Marketing Analytics Project')
st.subheader('Group 3')
st.write('Chandan Malla (Mmgt), Sheshachandra(Mmgt), Ghulam(Phd), Prajwal(Mmgt), Niranjan(MMgt), ')

selectbox = st.selectbox('Which section you want to go to?', ['1. Introduction', '2. EDA-Univariate','3. EDA-Multivariate','4. RFM and Market Basket Analysis'])


if selectbox=='1. Introduction':
    st.subheader('1. How did we select an e-commerce platform for the Marketing Strategy Assignment?')
    st.write('Two criteria were set on whose basis every e-commerce platform was analyzed.')
    st.write('1. Ease of sharing of data by end user')
    st.write('2. Number of users available')
    st.write('3. Richness of the data available for analysis')
    st.write('After brainstorming, it was decided that data would be sourced from consumers who shop on Flipkart.')


    st.subheader('2. Evaluation of the type of data to be analyzed')
    st.write('**A. We analyzed the invoices generated by Flipkart and found the following data points to be useful for analysis:**')
    st.write('1. Invoice ID')
    st.write('2. Order Date')
    st.write('3. MRP')
    st.write('4. Name of Product')
    st.write('5. Discount')
    st.write('6. GST')
    st.write('7. Delivery Fee')
    st.write('8. State')
    st.write('9. City')
    st.write('10. PIN code')
    st.write('11. Quantity')
    st.write('**B. We also captured psychometric and demographic data from the consumers who had shared their purchase data**')
    st.write('Following is the survey form which we shared with the end user to fill up')
    st.write('https://docs.google.com/forms/d/1Ncinn_BE_vdlrOuikhdkX3zsHPj1ZdRzG_3DIn0PtzI/edit')


    st.subheader('3. How was the purchase data gathered?')
    st.write('**A. We asked consumers to share their invoices, either through email or by downloading purchase invoices from Flipkart\'s website.**')
    st.write('Email:')
    image = Image.open('image/email_pdf.png')
    st.image(image, width=700)
    st.write('Website:')
    image = Image.open('image/Flipkart_order.png')
    st.image(image, width=700)

    st.subheader('4. Feature Engineering')
    st.write('***A. Purchase Data***')
    st.write('1. We extracted ***Categories, Subcategories and Ratings*** from every product from the Flipkart website using ```BeautifulSoup```')
    st.write('Below is the code which extracts the required features.')
    st.code('import bs4\n'
            'from bs4 import BeautifulSoup as bs  import requests\n'
            'categories=[]\n'
            '\tfrom tqdm import tqdm:\n'
'\t\tfor i in tqdm(range(data.shape[0])):\n'
    '\t\t\ttemp =[]\n'
    '\t\t\tlink = \'https://www.flipkart.com/search?q=\' + \'str(data[\'Title\' ][i])\'\n'
    '\t\t\tpage = requests.get(link)\n'
    '\t\t\tsoup = bs(page.content, \'html.parser\')\n'
   '\t\t\ttry:\n'

        '\t\t\trating = soup.find(\'div\', attrs={\'class\': \'_3LWZlK\'}).\n'
        '\t\t\tfor foo in soup.find_all(\'div\', attrs={\'class\': \'TB_InB\'}):\n'
            '\t\t\t\tbar = foo.find(\'a\', attrs={\'class\': \'_2Mji8F\'})\n'
            '\t\t\t\tif len(temp)>=2:\n'
                '\t\t\t\t\tbreak\n'
            '\t\t\t\telse:\n'
                '\t\t\t\t\ttemp.append(bar.text)\n'
        '\t\t\tcategories.append([data[\'Invoice ID\'][i],temp,rating,data[\'Title \'][i]])\n'
    '\t\t\texcept:\n'
        '\t\t\tcategories.append([data[\'Invoice ID\'][i],[\'NA\',\'NA\'],\'NA\',data[\'Title \'][i]])\n'
        '\t\t\tpass\n')

    st.write('2.**GST-Data** and **Delivery Data** was converted from absolute values to percentages.')
    st.write('3.**City_Tier** was extracted from the name of the city indicated on the invoice, for tier-specific analysis.')
    st.write('4 **Brand** was extracted from the name of the product.')
    st.write('5   To get **Sale** column we compiled the date ranges of every Flipkart sale since 2019 and compared it with the order date')
    st.write('6   To get **Covid** information we set the *1st wave* interval from **\'1-April-2020\' till \'1-September-2020\'** and *2nd Wave* from **\'1-Mar-2021\' to \'1-June-2021\'**'
             'and rest were set as **\'No\'**')
    st.write('7.**Month:** To find out the purchase pattern along the year, we segregated orders according to the month of purchase, after extracting the month from the order date).')
    st.write('8.**Year:** To observe the purchase trends year on year, we extracted year from the purchase date in to year and analyzed it.')
    st.write('9.**Time_month:** To analyze the purchase behaviour during the starting, middle, and the end of month, the days were extracted from the order date).')
    st.write('10.**Weekend/Weekday:** From the purchase date, we identified the day of the week on the date of purchase, to observe changes over the weekend.')
    st.write('11.**Log_Final Price:** To better observe the purchase value distribution among consumers, the purchase price was converted to natural log.')
    st.write('12.**More than Average**: This feature was added to observe if a "buyer" was buying in more number of categories than the "Average number of purchase categories per buyer"( in our case it was 4.8)"')

    st.write('\n\n')
    st.write('***B. Survey Data***')
    st.write('1.**Age:** To analyze age wise behaviour, the age was extracted from Date of Birth.')
    st.write('2.**RFMClass:** To analyze customers whose RFM value was similar(extracted from purchase data using Final value, Order_date and number of orders place)')
    st.write('3..**RFMClass:** To analyze customers whose RFM value was similar(extracted from purchase data using Final value, Order_date and number of orders place)')
    st.write('4.**Collectiv**, **Life_Satsif**, **Indiv**, **LongTermOri**, **ShortTermOri**, **Materialism**, **Spiritualism**, **EnvBehav**: these attributes were extracted '
             'by taking the mean of the responses to the questions in the respective categories.')
    st.write('5.**Has child:** Based on the "number of children" a buyer has, he was classified as "Yes or No" in this feature.')
    st.write('6.**Lives_in_City Tier:** To perform better demographic analysis, we segregated these purchase order cities into "Tiers".'
             ' Wikipedia\'s classification of Indian cities was used as the reference for this classification.'
             'Link:  https://en.wikipedia.org/wiki/Classification_of_Indian_cities')
    st.write('7.**Cluster:** The buyers were separated into three clusters using "K-Prototype Clustering".')
    st.write('8.**Participated_in_Sale**: The buyers were separated into three group: \'Never participated\', \'Participated once\',\'Participated more than once\'')
    st.write('9.**More than Average**: This feature was added to classify if a "buyer" was buying in more number of categories than "Average number of purchase categories per buyer( in our case it was 4. 8)"')

    st.subheader('5. Data Cleaning')
    st.write('This involved rather strenous manual efforts.')
    #st.write('Let\'s not discuss this part!')

    st.subheader('6. What was the approach used?')
    st.write('')
    st.write('We used Statistical concepts like *Non Parameteric Testing, Chi-Squared Test, ANOVA, Two-Sample Hypothesis Testing* taught in the Applied Statistics course to test some of our hypotheses.')
    st.write('For clustering the data, we experimented with different clustering algorithms and found *K-Prototype* to be the best, after visualising the results using a *T-SNE plot.')
    st.write('*PCA and Factor Analysis* were also examined, but were eventually abandoned due to lack of interpretability.')
    st.write('Finally, the observations we came up with are summarized with little or no statistical jargon in the below presentation.')
    st.write('**PPT**: https://docs.google.com/presentation/d/1z0njc1ZyZVfasgrO519wanvFSBUcBPvD/edit?usp=drive_web&ouid=116307560489086489304&rtpof=true')
    st.write('Some Highlights of PPT:')
    image1 = Image.open('image/Highlights_PPT_1.png')
    st.image(image1, width=1000)
    image2 = Image.open('image/Highlights_PPT_2.png')
    st.image(image2, width=1000)
    st.write('You can find the Colab Notebook we used for reference:')
    st.write('**Data Cleaning and Feature Engineering**: https://colab.research.google.com/drive/1v1n1ZbsmR-hXYUy6XycBQYZTAgaqzzJO?usp=sharing')
    st.write('**Main Notebook**: https://colab.research.google.com/drive/19HkBXu4_c0SM_3glibtmUSNPSM7LfGrx#scrollTo=EwsE7WsWdYSE')
    st.subheader('7. Marketing Strategies Developed')
    st.write('**1)Channelizing the Panic buying and dealing with Stock-home syndrome**')
    st.write('During a pandemic like this, we\'ve seen people suffer from Stock-Home Syndrome, when they buy more than they need and end up depleting '
             'supplier stock. In the event of a pandemic\'s first '
             'phase, when individuals become overly obsessed with utilitarian things, we can set a limit on how much they can buy from a single account, '
    'preventing supply shortages and allowing '
    'suppliers to continue serving customers. This is '
    'advantageous in two ways. To begin with, it may '
    'serve a huge number of customers rather than a '
    'small number of customers. Second, by doing so, '
    'they will get many new customers, as well as '
    'increased website reliability, as they appear to be '
    'a lifesaver for many. this will make turn the '
    'consumer into their loyal consumer in future. ')
    st.write('**2)Strategies that can be implemented**')
    st.write('Consumer confidence can be gained gradually with the support of previous purchasing patterns, as consumers may '
             'have to trust us with low-value products. If customers are satisfied, they will come to rely on us for higher-quality products. '
             ' This can be observed in the second wave, where high-value orders were placed as well.')
    st.write('**3) Cater what they don’t have and gradually increase the horizon.**')
    st.write('Tier 2 and 3 cities will be targeted with more brand-oriented suggestions, while Tier 1 cities will be targeted with more utilitarian products and added conveniences such as same-day delivery. Also, gradually broaden the vision by moving tier 1 cities upstream and tier 2 and 3 cities downstream.')
    st.write('**4) Encourage shoppers by discount during dry period**')
    st.write('Sales have been demonstrated to encourage more customers to buy, and they can be employed during times when people aren\'t as interested in buying. This will enhance not only purchases but also online visitors to the website, which may then be directed to sponsored products. This will assist us in capitalize traffic even during the dry seasons.')
    st.write('**5) Channelizing the shopping enthusiasm as well as Revenge shopping**')
    st.write('To channel the consumer\'s shopping energy at the start of the month. Consumers should be targeted for high-value products with discounts that are only slightly greater than the main competitors.	')
    st.write('Options such as "buy now, pay later,cheap EMI, and others are availableat the end of the month, allowing individuals to shop even when they are short on cash.')
    st.write('**6) Utilizing weekdays and weekends**')
    st.write('On weekdays, a greater number of unitarian products should be displayed, as well as the greatest number of discounts. Hedonic products should be shown more on weekends. Also, items that  demand a high level of involvement should target customers on weekends, whereas products that require a low level of involvement should target customers throughout the week.')

###############################################EDA#####################################################################33



elif selectbox=='2. EDA-Univariate':

    selection_data = st.selectbox("Select the Data for which you want EDA:", ['Purchase_Data/Combined_data','Survey_Data'])
    st.write('Coding Language: ```Python```')
    st.write('Libraries Used for EDA: ```pywaffle, prettytable, plotly, matplotlib, seaborn```')

    if selection_data=='Purchase_Data/Combined_data':

        columns = ['GST%%', 'City_Tier', 'Discount%', 'Delivery Fee%',
               'Sale', 'Covid', 'Month', 'Year', 'WEEKDAY',
               'Time_Month', 'Gender', 'Marital Status', 'More_than_average', 'Clusters', 'Lives_in_city_tier']
        discrete = ['State',
                'City','Categories','Current Job Title','Brand']
        continuous =['Age','Quantity','MRP','Ratings','Final Price','Log_Final Price']

        st.sidebar.subheader('Purchase Data')
        column_for_univariate = st.sidebar.selectbox("Select a Categorical Column:", columns)
        column_for_discrete = st.sidebar.selectbox("Select a Discrete Column:", discrete)
        column_for_continuous = st.sidebar.selectbox("Select a Discrete Column:", continuous)



        st.title('A. Purchase/Combined Data')
        st.header('1.) Categorical Data')
        st.subheader('I) Univariate Analysis for '+column_for_univariate)


        combined_data = pd.read_csv('data/Combined_data-Part_3.csv')

        if(column_for_univariate):

            fig = px.histogram(data_frame=combined_data, y=None, x=column_for_univariate, color=None,
                           facet_row=None, facet_col=None, marginal=None, width=1200, height=700,
                           title="Univariate plot for "+str(column_for_univariate)+" on Combined_data")
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.70)
            fig.update_layout(
            autosize=True,
            # margin=dict(l=0, r=50, t=5, b=4  ),
            )
        #st.header("Distribution of Log_Final Price")
            st.plotly_chart(fig)
        st.header('2.) Discrete Data')
        if(column_for_discrete=='Brand'):

            st.subheader('I) Univariate Analysis for '+column_for_discrete+ ' purchased ')
            image = Image.open('image/wordcloud.png')
            st.image(image, width=1000)
        else:

            temp = combined_data.groupby(column_for_discrete).agg({"Quantity": lambda item: item.sum()}).sort_values('Quantity',
                                                                                                        inplace=False,
                                                                                                        ascending=False).reset_index()
            fig = px.bar(data_frame=temp[0:20], x=column_for_discrete, y='Quantity', color=None,
                        facet_row=None, facet_col=None,width=1200, height=700, )
            fig.update_layout(barmode='group')
            fig.update_traces(opacity=0.70)
            st.subheader('I.) Univariate Analysis on Top '+column_for_discrete)
            st.plotly_chart(fig)
        st.header('3.) Continuous Data')

        if(column_for_continuous):
            fig = px.histogram(data_frame=combined_data, y=None, x=column_for_continuous, color=None,
                               facet_row=None, facet_col=None, marginal=None, width=1200, height=700,
                               )
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.70)
            fig.update_layout(
                autosize=True,
                # margin=dict(l=0, r=50, t=5, b=4  ),
            )
            # st.header("Distribution of Log_Final Price")
            st.subheader('I.) Univariate Analysis on ' + column_for_continuous)
            st.plotly_chart(fig)
        st.subheader('II) Purchase Pattern through Months ')
        image = Image.open('image/Sale_month_wise.png')
        st.image(image, width=1500)

    #==========================================================================================================================================================
    #=============================================================Survey Data==================================================================================
    #==========================================================================================================================================================
    else:
        st.title('B. Survey Data')
        survey_data = pd.read_csv('data/Clustered_survey_data_final_2.csv')
        survey_data['RFMClass'] = survey_data['RFMClass'].astype('str')
        categorical_sur = ['Gender','Marital Status','Do you have to care for anyone with chronic illness?','Income (per month)', 'Preferred Mode of Payment',
                       'Do you practise meditation? Yes/No', 'If yes','Do you do any form of exercise?', 'If yes.1',' How often do you volunteer for social-service activities?',
           'Hobbies_Count', 'How often do you pursue your hobbies?', 'Collectiv',
           'Life_Satsif', 'Indiv', 'LongTermOri', 'ShortTermOri', 'Materialism',
           'Spiritualism', 'EnvBehav','has_child', 'Lives_in_city_tier',
           'Clusters', 'More_than_average', 'Participated_in_Sale']

        discrete_sur = ['RFMClass','Current Job Title']
        continuous_sur = ['Age']

        st.sidebar.subheader('Survey Data')
        st.header('1.) Categorical Data')

        column_for_categorical_sur = st.sidebar.selectbox("Select a Categorical Column:", categorical_sur)
        column_for_discrete_sur = st.sidebar.selectbox("Select a Discrete Column:", discrete_sur)
        column_for_continuous_sur = st.sidebar.selectbox("Select a Continuous Column:", continuous_sur)

        if (column_for_categorical_sur):
            fig = px.histogram(data_frame=survey_data, y=None, x=column_for_categorical_sur, color=None,
                               facet_row=None, facet_col=None, marginal=None, width=1200, height=700,
                               )
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.70)
            fig.update_layout(
                autosize=True,
                # margin=dict(l=0, r=50, t=5, b=4  ),
            )
            # st.header("Distribution of Log_Final Price")
            st.subheader('I.) Univariate Analysis on ' + column_for_categorical_sur)
            st.plotly_chart(fig)
        st.header('2.) Discrete Data')

        if (column_for_discrete_sur):
            temp = survey_data.groupby(column_for_discrete_sur).size().sort_values(
                inplace=False,
                ascending=False).reset_index()
            fig = px.bar(data_frame=temp[0:20], x=column_for_discrete_sur, y=0, color=None,
                         facet_row=None, facet_col=None, width=1200, height=700, )
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.70)
            st.subheader('I.) Univariate Analysis on Top ' + column_for_discrete_sur)
            st.plotly_chart(fig)
        st.header('3.) Continuous Data')

        if (column_for_continuous_sur):

            fig = px.histogram(data_frame=survey_data, y=None, x=column_for_continuous_sur, color=None,
                               facet_row=None, facet_col=None, marginal=None, width=1200, height=700,
                               )
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.70)
            fig.update_layout(
                autosize=True,
                # margin=dict(l=0, r=50, t=5, b=4  ),
            )
            # st.header("Distribution of Log_Final Price")
            st.subheader('I.) Univariate Analysis on ' + column_for_continuous_sur)
            st.plotly_chart(fig)


elif selectbox=='3. EDA-Multivariate':

    selection_data = st.selectbox("Select the Data for which you want EDA:",
                                  ['Purchase_Data/Combined_data', 'Survey_Data'])
    st.write('Coding Language: ```Python```')
    st.write('Libraries Used for EDA: ```pywaffle, prettytable, plotly, matplotlib, seaborn```')

    if selection_data == 'Purchase_Data/Combined_data':
        columns = [None, 'GST%%', 'City_Tier', 'Sale', 'Covid', 'Month', 'Year', 'WEEKDAY',
                   'Log_Final Price',
                   'Time_Month', 'Gender', 'Marital Status',
                   'Do you have to care for anyone with chronic illness?',
                   'Do you practise meditation? Yes/No',
                   'Do you do any form of exercise?', 'Collectiv',
                   'Life_Satsif', 'Indiv', 'LongTermOri', 'ShortTermOri', 'Materialism',
                   'Spiritualism', 'EnvBehav', 'has_child', 'Lives_in_city_tier',
                   'Clusters', 'More_than_average']

        column_x = ['Age','Log_Final Price','GST%%', 'City_Tier', 'Sale', 'Covid', 'Month', 'Year', 'WEEKDAY',
                   'Log_Final Price',
                   'Time_Month', 'Gender', 'Marital Status',
                   'Do you have to care for anyone with chronic illness?',
                   'Do you practise meditation? Yes/No',
                   'Do you do any form of exercise?', 'Collectiv',
                   'Life_Satsif', 'Indiv', 'LongTermOri', 'ShortTermOri', 'Materialism',
                   'Spiritualism', 'EnvBehav', 'has_child', 'Lives_in_city_tier',
                   'Clusters', 'More_than_average']

        st.title('A. Purchase/Combined_Data')
        st.sidebar.subheader('Options to Analyze Distribution/Barplot')
        x_value = st.sidebar.selectbox("Select X-Axis:", column_x,key = 'EDA324')
        color = st.sidebar.selectbox("Select a Color:", columns,key = 'EDA')
        row = st.sidebar.selectbox("Select a Row:",columns,key = 'EDA1')
        col = st.sidebar.selectbox("Select a Column:", columns,key = 'EDA2')
        st.subheader('I.) Distribution of '+str(x_value)+' with color ='+str(color)+', Row ='+str(row)+', Column  ='+str(col))
        fig = px.histogram(data_frame=combined_data, y=None, x=x_value, color=color,
                        facet_row=row, facet_col=col, marginal='box',width=1200, height=700,)
        fig.update_layout(barmode='group')
        fig.update_traces(opacity=0.70)
        st.plotly_chart(fig)

        colss = ['City_Tier', 'GST%%',
               'Sale', 'Covid', 'Month', 'Year', 'WEEKDAY',
               'Time_Month', 'Gender', 'Marital Status', 'More_than_average', 'Clusters', 'Lives_in_city_tier']
        st.subheader('II.)Top ' + 'Brands ')
        cols_selected = st.selectbox("Select a Column:", colss,key = 'EDA')
        st.subheader('By ' + str(cols_selected))

        # fig = px.histogram(data_frame= combined_data.groupby(['Brand', 'City_Tier']).size().reset_index(), y=None, x=x_value, color=color,
        #                    facet_row=row, facet_col=col, marginal='box', width=1500, height=700, )
        # fig.update_layout(barmode='group')
        # fig.update_traces(opacity=0.70)
        # st.plotly_chart(fig)

        unique_colss = np.unique(combined_data[cols_selected])
        for col in unique_colss:
            fig = plt.figure(figsize=(18, 8),
            FigureClass=Waffle,
            rows=4,
            title={'label': 'Top Brands by '+col, 'loc': 'left'},
            values=combined_data.groupby(['Brand', cols_selected]).size().reset_index()[
                       combined_data.groupby(['Brand', cols_selected]).size().reset_index()[
                           cols_selected] == col].sort_values(by=0, ascending=False)[0][:10],
            labels=list(combined_data.groupby(['Brand', cols_selected]).size().reset_index()[
                            combined_data.groupby(['Brand', cols_selected]).size().reset_index()[
                                cols_selected] == col].sort_values(by=0, ascending=False).Brand[:10]),
                legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)})
            st.pyplot(fig)

        colss = ['City_Tier', 'GST%%',
                 'Sale', 'Covid', 'Month', 'Year', 'WEEKDAY',
                 'Time_Month', 'Gender', 'Marital Status', 'More_than_average', 'Clusters', 'Lives_in_city_tier']
        st.subheader('III.)Top ' + 'Categories ')
        cols_selected = st.selectbox("Select a Column:", colss, key='EDAef')
        st.subheader('By ' + str(cols_selected))


        unique_colss = np.unique(combined_data[cols_selected])
        for col in unique_colss:
            fig = plt.figure(figsize=(16, 8),
                             FigureClass=Waffle,

                             rows=9,
                             title={'label': 'Top Categories by ' + col, 'loc': 'left'},
                             values=combined_data.groupby(['Categories', cols_selected]).size().reset_index()[
                                        combined_data.groupby(['Categories', cols_selected]).size().reset_index()[
                                            cols_selected] == col].sort_values(by=0, ascending=False)[0][:10],
                             labels=list(combined_data.groupby(['Categories', cols_selected]).size().reset_index()[
                                             combined_data.groupby(['Categories', cols_selected]).size().reset_index()[
                                                 cols_selected] == col].sort_values(by=0, ascending=False).Categories[:10]),
                             legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1)})
            st.pyplot(fig)



    elif selection_data == 'Survey_Data':
        st.title('B. Survey Data')
        survey_data = pd.read_csv('data/Clustered_survey_data_final_2.csv')
        survey_data['RFMClass'] = survey_data['RFMClass'].astype(str)
        columns =[None,
            'Gender',
            'Marital Status',
            'Do you practise meditation? Yes/No',
            'Do you do any form of exercise?', 'Collectiv',
            'Life_Satsif', 'Indiv', 'LongTermOri', 'ShortTermOri', 'Materialism',
            'Spiritualism', 'EnvBehav', 'has_child', 'Lives_in_city_tier',
            'Clusters', 'More_than_average', 'Participated_in_Sale'
        ]

        columns_x = ['Age',
                   'Gender',
                   'Marital Status',
                   'Do you practise meditation? Yes/No',
                   'Do you do any form of exercise?', 'Collectiv',
                   'Life_Satsif', 'Indiv', 'LongTermOri', 'ShortTermOri', 'Materialism',
                   'Spiritualism', 'EnvBehav', 'has_child', 'Lives_in_city_tier',
                   'Clusters', 'More_than_average', 'Participated_in_Sale'
                   ]
        x_value_x = st.sidebar.selectbox("Select a Color:", columns_x, key='EDA45')
        colorq = st.sidebar.selectbox("Select a Color:", columns, key='EDA45')
        rowq = st.sidebar.selectbox("Select a Row:", columns, key='EDA451')
        colq = st.sidebar.selectbox("Select a Column:", columns, key='EDA245')
        st.subheader('I) Distribution of ' + str(x_value_x) + ' with color =' + str(colorq) + ', Row =' + str(
            rowq) + ', Column  =' + str(colq))
        fig = px.histogram(data_frame=survey_data, y=None, x=x_value_x, color=colorq,
                           facet_row=rowq, facet_col=colq, marginal='box', width=1200, height=700, )
        fig.update_layout(barmode='overlay')
        fig.update_traces(opacity=0.70)
        st.plotly_chart(fig)


        st.subheader('II) Visualising the Clusters using *T-SNE* generated by *K-Prototype Clustering* on *Survey Data*')
        image = Image.open('image/T-SNE_Plot_Clusters.png')
        st.image(image, width=1200)

elif selectbox=='4. RFM and Market Basket Analysis':

    st.write('Coding Language: ```Python```')
    st.write('Libraries Used for EDA: ```pywaffle, prettytable, plotly, matplotlib, seaborn```')

    rfm = pd.read_csv('data/RFM_Analysis.csv')
    st.title('A. Top Consumers whose RFM Score is high')
    db=rfm[rfm['RFMClass'] == 111].sort_values('monetary_value', ascending=False)
    st.dataframe(db)

    st.title('B. Market Basket Analysis arranged by high confidence')
    mba = pd.read_csv('data/Market_Basket.csv')
    mba.drop('Unnamed: 0',inplace=True,axis=1)
    mba = mba.sort_values("confidence", ascending = False)
    st.dataframe(mba)

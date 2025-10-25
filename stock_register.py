import streamlit as st,pandas as pd
import read_data
from typing import Union

def opening_balance():
    sheet=read_data.connect_to_gsheet(sheet_name='Opening Balance')
    data=sheet.get_all_records()
    date=st.date_input('Date to show','today')
    df=pd.DataFrame(data)
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')

    filtered_df=df[df['Date'].dt.date==date]
    st.dataframe(filtered_df)


rmc:list[Union[float,int,str]]=[0,0,0,0,0]
def raw_material_received():
    sheet=read_data.connect_to_gsheet(sheet_name='Raw Material Recieved')
    global rmc
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        date=st.date_input('Date of Materials Received',key='date_inp_rmc')
        add_date=st.button('Add Date',key='date_rmc')
        if add_date and rmc[0]==0:
            rmc[0]=date.isoformat()
    with col2:
        grn=st.text_input('GRN Number',key='grn_inp_rmc')
        add_grn=st.button('Add GRN',key='grn_rmc')
        if add_grn and rmc[1]==0:
            rmc[1]=grn
    with col3:
        provider=st.text_input('Provider Name',key='provider_inp_rmc')
        add_provider=st.button('Add Provider Details',key='provider_rmc')
        if add_provider and rmc[2]==0:
            rmc[2]=provider
    with col4:
        product=st.text_input('Product Type',key='product_inp_rmc')
        add_quantity=st.button('Add Product Type',key='product_rmc')
        if add_quantity and rmc[3]==0:
            rmc[3]=product
    with col5:
        qty=st.number_input('Quantity in Kg',key='qty_inp_rmc')
        add_quantity=st.button('Add Quantity',key='qty_rmc')
        if add_quantity and rmc[4]==0:
            rmc[4]=qty
    rmc_df=pd.DataFrame(rmc).T
    st.dataframe(rmc_df)
    submit=st.button('Submit',key='submit_rmc')
    if submit:
        sheet.append_row(rmc)
        st.write('Adding the following:',rmc)
        rmc=[0,0,0,0,0]
        st.rerun()

# cons:list[Union[float,int,str]]=[0,0,0]
# def consumed():
#     sheet=read_data.connect_to_gsheet(sheet_name='Raw Material Consumed')
#     global cons
#     date=st.date_input('Date of Items consumed',key='date_inp_cons')
#     add_date=st.button('Add Date',key='date_cons')
#     if add_date and cons[0]==0:
#         cons[0]=date.isoformat()
#     qty=st.number_input('Quantity in Kg',key='qty_inp_cons')
#     add_quantity=st.button('Add Quantity',key='qty_cons')
#     if add_quantity and cons[1]==0:
#         cons[1]=qty
#     product=st.text_input('Product Batch Number',key='product_inp_cons')
#     add_product=st.button('Add Product Number',key='product_cons')
#     if add_product and cons[2]==0:
#         cons[2]=product
#     submit=st.button('Submit',key='submit_cons')
#     if submit:
#         sheet.append_row(cons)
#         st.write('Adding the following:',cons)
#         cons=[0,0,0]
#         st.rerun()
def opening_balance():
    st.header('Opening Balance')
    sheet=read_data.connect_to_gsheet(sheet_name='Opening Balance')
    data=sheet.get_all_records()
    date=st.date_input('Date to show',value=datetime.date.today(),key='ob')
    df=pd.DataFrame(data)
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')

    filtered_df=df[df['Date'].dt.date==date]
    st.dataframe(filtered_df)


rmc:list[Union[float,int,str]]=[0,0,0,0]
def raw_material_received():
    st.header('Raw Material Received')
    sheet=read_data.connect_to_gsheet(sheet_name='Raw Material Recieved')
    global rmc
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        date=st.date_input('Date of Materials Received',key='date_inp_rmc')
        add_date=st.button('Add Date',key='date_rmc')
        if add_date and rmc[0]==0:
            rmc[0]=date.isoformat()
    with col2:
        provider=st.text_input('Provider Name',key='provider_inp_rmc')
        add_provider=st.button('Add Provider Details',key='provider_rmc')
        if add_provider and rmc[1]==0:
            rmc[1]=provider
    with col3:
        product=st.text_input('Product Type',key='product_inp_rmc')
        add_quantity=st.button('Add Product Type',key='product_rmc')
        if add_quantity and rmc[2]==0:
            rmc[2]=product
    with col4:
        qty=st.number_input('Quantity in Kg',key='qty_inp_rmc')
        add_quantity=st.button('Add Quantity',key='qty_rmc')
        if add_quantity and rmc[3]==0:
            rmc[3]=qty        
    rmc_df=pd.DataFrame(rmc).T
    st.dataframe(rmc_df)
    submit=st.button('Submit',key='submit_rmc')
    if submit:
        sheet.append_row(rmc)
        st.write('Adding the following:',rmc)
        rmc=[0,0,0,0]
        st.rerun()


def raw_material_consumed():
    st.header('Raw Material Consumed')
    sheet=read_data.connect_to_gsheet(sheet_name='Raw Material Consumed')
    data=sheet.get('A:O')
    date=st.date_input('Date to show',value=datetime.date.today(),key='date_rmc_2')
    df=pd.DataFrame(data[1:],columns=data[0])
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')

    filtered_df=df[df['Date'].dt.date==date]
    st.dataframe(filtered_df)

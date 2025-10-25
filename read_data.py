import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
from datetime import datetime
import time
from typing import Union,cast,Sequence

def connect_to_gsheet(sheet_name='Sheet1'):
    scope = ["https://spreadsheets.google.com/feeds", 
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", 
             "https://www.googleapis.com/auth/drive"]
    creds_dict=st.secrets['gcp_service_account']
    credentials = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(credentials) # type: ignore
    spreadsheet = client.open('Testing1')  
    return spreadsheet.worksheet(sheet_name)  


sheet_by_name = connect_to_gsheet()
st.title("Simple Data Entry using Streamlit")

dpr:list[Union[int, str]]=[0,0,0,0,0,0,0,0,0,0]
def daily_production_report():
    st.header('Daily Production Report')
    global dpr
    supervisor_name=st.text_input('Supervisor Name')
    sn=st.button('Add Supervisor Name',key='SN')
    if sn and dpr[0]==0:
        dpr[0]=supervisor_name
        st.write(f'Supervisor Name Updated with {supervisor_name}')
    operator_name=st.text_input('Operators Name')
    on=st.button('Add Operator Name',key='ON')
    if on and dpr[1]==0:
        dpr[1]=operator_name
        st.write(f'Operator Name updated with {operator_name}')
    reactor_no=st.text_input('Reactor Number')
    rn=st.button('Add Reactor Number',key='rn')
    if rn and dpr[2]==0:
        dpr[2]=reactor_no
        st.write(f'Reactor Number Updated with {reactor_no}')
    product_batch_no=st.text_input('Product Batch Number')
    pbn=st.button('Add Product Batch Number',key='pbn')
    if pbn and dpr[3]==0:
        dpr[3]=product_batch_no
        st.write(f'Product Batch Number Updated with {product_batch_no}')
    date=st.date_input('Date')
    td=st.button('Add Date of Production',key='td')
    if td and dpr[4]==0:
        dpr[4]=product_batch_no
        st.write(f'Production started on {date}')
    process_started=st.button('Process Start Time',key='pst')
    if process_started and dpr[5]==0:
        dpr[5]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.write(f'Process started at {dpr[5]}')
    reaction_started=st.button('Reaction Start Time',key='rst')
    if reaction_started and dpr[6]==0:
        dpr[6]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.write(f'Reaction started at {dpr[6]}')
    cooling_started=st.button('Cooling Start Time',)
    if cooling_started and dpr[7]==0:
        dpr[7]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.write(f'Cooling started at {dpr[7]}')
    filter_started=st.button('Filter Start Time',key='fst')
    if filter_started and dpr[8]==0:
        dpr[8]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.write(f'Filter started at {dpr[8]}')
    process_completed=st.button('Process Completed at Time',key='pct')
    if process_completed and dpr[9]==0:
        dpr[9]=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.write(f'Process Completed at {dpr[9]}')
    submit_button=st.button('Submit',key='Submit_DPR')
    if submit_button:
        st.write(f"Form submitted at {datetime.now()}!")
        st.write(f'Values updated: {dpr}')
        connect_to_gsheet(sheet_name='Daily Production Report').append_row(dpr) 
        dpr=[0,0,0,0,0,0,0,0,0,0]
        time.sleep(2)
        st.rerun()


poc:list[Union[int, str]]=[0,0,0,0,0,0,0,0,0,0]

def pre_operation_checksheet():
    st.header('Pre Operation Checksheet')
    global poc
    shift=st.selectbox('Shift',['Day','Night'],index=None,placeholder='Please select a shift')
    add_shift=st.button('Add Shift',key='as')
    if add_shift and shift is not None and poc[0]==0:
        poc[0]=shift
        st.write(f'You added {shift}')
    batch_Number=st.text_input('Batch Number',key='batch_number')
    add_batch_number=st.button('Add Batch Number',key='bn')
    if add_batch_number and poc[1]==0:
        poc[1]=batch_Number
        st.write(f'You added {batch_Number}')
    raw_material=st.button('CHECKED RAW MATERIAL',key='crm')
    if raw_material and poc[2]==0:
        poc[2]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    check_water_sample=st.button('CHECKED D.M. WATER SAMPLE',key='cws')
    if check_water_sample and poc[3]==0:
        poc[3]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    charge_water_sample=st.button('CHARGE D.M.  WATER',key='chws')
    if charge_water_sample and poc[4]==0:
        poc[4]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    close_reactor=st.button('CLOSE REACTOR  BOTTOM  VALVE',key='crbv')
    if close_reactor and poc[5]==0:
        poc[5]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    close_valve=st.button('CLOSE MONOMER TANK  BOTTOM  &  ROTAMETER VALVE',key='cntb')
    if close_valve and poc[6]==0:
        poc[6]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    charge_cooling_tower=st.button('CHARGE  COOLING TOWER CHEMICAL',key='cct')
    if charge_cooling_tower and poc[7]==0:
        poc[7]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    take_belt_off=st.button('TAKE OFF THE BELT  OF THE REACTOR AND LINK OFF ELECTRICAL  CONNECTION  FROM MAIN SWITCH WHEN  IT CLEANS',key='tbo')
    if take_belt_off and poc[8]==0:
        poc[8]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    check_monomer_tank=st.button('CHECK  MONOMER TANK AFTER  REACTION COMPLETE',key='cmt')
    if check_monomer_tank and poc[9]==0:
        poc[9]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f'You added {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    submit_button = st.button("Submit")
    if submit_button:
        st.write(f"Form submitted at {datetime.now()}!")
        st.write(f'Values updated: {poc}')
        connect_to_gsheet(sheet_name='Pre Operation Checksheet').append_row(poc)
        poc=[0,0,0,0,0,0,0,0,0,0]
        time.sleep(2)
        st.rerun()


pr:list[Union[None,int,str]]=[0]*35

def production_report():
    st.header('Production Report')
    global pr
    col1,col2=st.columns(2)
    with col1:
        dmw=st.text_input('DM Weight',value=454.19,key='DM Weight')
        add_dmw=st.button('Add DM Weight',key='Add DM Weight')
        if add_dmw and pr[0]==0:
                pr[0]=dmw
                st.write(f'You added {dmw}')
        ew=st.text_input('E-01 Weight',value=7.275,key='E-01 Weight 1')
        add_ew=st.button('Add E-01 Weight',key='Add E-01 Weight 1')
        if add_ew and pr[2]==0:
                pr[2]=ew
                st.write(f'You added {ew}')
        mw=st.text_input('M-03 Weight',value=1594.5,key='M-03 Weight')
        add_mw=st.button('Add M-03 Weight',key='Add M-03 Weight')
        if add_mw and pr[4]==0:
            pr[4]=mw
            st.write(f'You added {mw}')
        m5w=st.text_input('M-05 Weight',value=32.100,key='M-05 Weight')
        add_m5w=st.button('Add M-05 Weight',key='Add M-05 Weight')
        if add_m5w and pr[6]==0:
            pr[6]=m5w
            st.write(f'You added {m5w}')
        dm2w=st.text_input('DM2 Weight',value=720,key='DM2 Weight')
        add_dm2w=st.button('Add DM2 Weight',key='Add DM2 Weight')
        if add_dm2w and pr[8]==0:
            pr[8]=dm2w
            st.write(f'You added {dm2w}')
        ew=st.text_input('E-01 Weight',value=1.5,key='E-01 Weight 2')
        add_ew=st.button('Add E-01 Weight',key='Add E-01 Weight 2')
        if add_ew and pr[10]==0:
            pr[10]=ew
            st.write(f'You added {ew}')
        e2w=st.text_input('E-02 Weight',value=1.5,key='E-02 Weight')
        add_e2w=st.button('Add E-02 Weight',key='Add E-02 Weight')
        if add_e2w and pr[12]==0:
            pr[12]=e2w
            st.write(f'You added {e2w}')
        s2w=st.text_input('S-02 Weight',value=0.855,key='S-02 Weight')
        add_s2w=st.button('Add S-02 Weight',key='Add S-02 Weight')
        if add_s2w and pr[14]==0:
            pr[14]=s2w
            st.write(f'You added {s2w}')   
        cb=st.text_input('C-01 Weight',value=7.5,key='C-01 Weight')
        add_cb=st.button('Add C-01 Weight',key='Add C-01 Weight')
        if add_cb and pr[16]==0:
            pr[16]=cb
            st.write(f'You added {cb}')
        an1w=st.text_input('An-01 Weight',value=18.75,key='An-01 Weight')
        add_an1w=st.button('Add An-01 Weight',key='Add An-01 Weight')
        if add_an1w and pr[18]==0:
            pr[18]=an1w
            st.write(f'You added {an1w}')
        e3w=st.text_input('E-03 Weight',value=10.500,key='E-03 Weight')
        add_e3w=st.button('Add E-03 Weight',key='Add E-03 Weight')
        if add_e3w and pr[20]==0:
            pr[20]=e3w
            st.write(f'You added {e3w}')
        tw=st.text_input('T-01 Weight',value=0.600,key='T-01 Weight')
        add_tw=st.button('Add T-01 Weight',key='Add T-01 Weight')
        if add_tw and pr[22]==0:
            pr[22]=tw
            st.write(f'You added {tw}')
        rw=st.text_input('R-01 Weight',value=1.050,key='R-01 Weight')
        add_rw=st.button('Add R-01 Weight',key='Add R-01 Weight')
        if add_rw and pr[24]==0:
            pr[24]=rw
            st.write(f'You added {rw}')
        f2w=st.text_input('F-02 Weight',value=4.5,key='F-02 Weight')
        add_f2w=st.button('Add F-02 Weight',key='Add F-02 Weight')
        if add_f2w and pr[26]==0:
            pr[26]=f2w
            st.write(f'You added {f2w}')
        f1w=st.text_input('F-01 Weight',value=0.180,key='F-01 Weight')
        add_f1w=st.button('Add F-01 Weight',key='Add F-01 Weight')
        if add_f1w and pr[28]==0:
            pr[28]=f1w
            st.write(f'You added {f1w}')
        
    with col2:
        dmb=st.text_input('DM Batch',key='DM Batch')
        add_dmb=st.button('Add DM Batch',key='Add DM Batch')
        if add_dmb and pr[1]==0:
            pr[1]=dmb
            st.write(f'You added {dmb}')
        eb1=st.text_input('E-01 Batch',key='E-01 Batch 1')
        add_eb1=st.button('Add E-01 Batch',key='Add E-01 Batch 1')
        if add_eb1 and pr[3]==0:
            pr[3]=eb1
            st.write(f'You added {eb1}')
        mb=st.text_input('M-03 Batch',key='M-03 Batch')
        add_mb=st.button('Add M-03 Batch',key='Add M-03 Batch')
        if add_mb and pr[5]==0:
            pr[5]=mb
            st.write(f'You added {mb}')
        m5b=st.text_input('M-05 Batch',key='M-05 Batch')
        add_m5b=st.button('Add M-05 Batch',key='Add M-05 Batch')
        if add_m5b and pr[7]==0:
            pr[5]=m5b
            st.write(f'You added {m5b}')
        dm2b=st.text_input('DM2 Batch',key='DM2 Batch')
        add_dm2b=st.button('Add DM2 Batch',key='Add DM2 Batch')
        if add_dm2b and pr[9]==0:
            pr[9]=dm2b
            st.write(f'You added {dm2b}')
        eb2=st.text_input('E-01 Batch',key='E-01 Batch 2')
        add_eb2=st.button('Add E-01 Batch',key='Add E-01 Batch 2')
        if add_eb2 and pr[11]==0:
            pr[11]=eb2
            st.write(f'You added {eb2}')
        e2b=st.text_input('E-02 Batch',key='E-02 Batch')
        add_e2b=st.button('Add E-02 Batch',key='Add E-02 Batch')
        if add_e2b and pr[13]==0:
            pr[13]=e2b
            st.write(f'You added {e2b}')
        s2b=st.text_input('S-02 Batch',key='S-02 Batch')
        add_s2b=st.button('Add S-02 Batch',key='Add S-02 Batch')
        if add_s2b and pr[15]==0:
            pr[15]=s2b
            st.write(f'You added {s2b}')
        c1b=st.text_input('C-01 Batch',key='C-01 Batch')
        add_c1b=st.button('Add C-01 Batch',key='Add C-01 Batch')
        if add_c1b and pr[17]==0:
            pr[17]=c1b
            st.write(f'You added {c1b}')
        an1b=st.text_input('An-01 Batch',key='An-01 Batch')
        add_an1b=st.button('Add An-01 Batch',key='Add An-01 Batch')
        if add_an1b and pr[19]==0:
            pr[19]=an1b
            st.write(f'You added {an1b}')
        e3b=st.text_input('E-03 Batch',key='E-03 Batch')
        add_e3b=st.button('Add E-03 Batch',key='Add E-03 Batch')
        if add_e3b and pr[21]==0:
            pr[21]=e3b
            st.write(f'You added {e3b}')
        tb=st.text_input('T-01 Batch',key='T-01 Batch')
        add_tb=st.button('Add T-01 Batch',key='Add T-01 Batch')
        if add_tb and pr[23]==0:
            pr[23]=tb
            st.write(f'You added {tb}')
        rb=st.text_input('R-01 Batch',key='R-01 Batch')
        add_rb=st.button('Add R-01 Batch',key='Add R-01 Batch')
        if add_rb and pr[25]==0:
            pr[25]=rb
            st.write(f'You added {rb}')
        f2b=st.text_input('F-02 Batch',key='F-02 Batch')
        add_f2b=st.button('Add F-02 Batch',key='Add F-02 Batch')
        if add_f2b and pr[27]==0:
            pr[27]=f2b
            st.write(f'You added {f2b}')
        f1b=st.text_input('F-01 Batch',key='F-01 Batch')
        add_f1b=st.button('Add F-01 Batch',key='Add F-01 Batch')
        if add_f1b and pr[29]==0:
            pr[29]=f1b
            st.write(f'You added {f1b}')
    pun=st.text_input('PRODUCTION UNIT NUMBER',key='PRODUCTION UNIT NUMBER')
    add_pun=st.button('Add PRODUCTION UNIT NUMBER',key='Add PRODUCTION UNIT NUMBER')
    if add_pun and pr[30]==0:
        pr[30]=pun
        st.write(f'You added {pun}')
    yp=st.text_input('YIELD PRODUCED IN KG',key='YIELD PRODUCED IN KG')
    add_yp=st.button('Add YIELD PRODUCED IN KG',key='Add YIELD PRODUCED IN KG')
    if add_yp and pr[31]==0:
        pr[31]=yp
        st.write(f'You added {yp}')
    wp=st.text_input('WASTAGE IN KG',key='WASTAGE IN KG')
    add_wp=st.button('Add WASTAGE IN KG',key='Add WASTAGE IN KG')
    if add_wp and pr[32]==0:
        pr[32]=wp
        st.write(f'You added {wp}')
    r=st.text_input('REMARKS',key='REMARKS')
    add_r=st.button('Add REMARKS',key='Add REMARKS')
    if add_r and pr[33]==0:
          pr[33]=r
    date=st.date_input('Date',key='Date PR')
    add_date=st.button('Add Date',key='Add Date PR')
    if add_date and pr[34]==0:
          pr[34]=date.isoformat()
    submit_button = st.button("Submit",key='SUBMIT_PR')
    if submit_button:
        st.write(f"Form submitted at {datetime.now()}!")
        st.write(f'Values updated: {pr}')
        connect_to_gsheet(sheet_name='Production Report').append_row(cast(Sequence[str | int | float],pr))
        pr=[0]*35
        time.sleep(2)
        st.rerun()

def in_process_and_final_testing_report():
    st.header('Final Testing Report')
    parameters=['APPEARANCE','SOLID CONTENT','VISCOSITY','pH','COLOUR','ROLLING BALL TACK TEST']
    col1,col2=st.columns(2,gap='small')
    v=[]
    with st.form('final_testing_report'): 
        for i in range(len(parameters)):
            st.header(f'**{parameters[i]}**')
            col1=st.text_input('SPECIFICATION',key=f'specification{i}')
            v.append(col1)
            col2=st.text_input('OBS_VALUE',key=f'obs_value{i}')
            v.append(col2)    
        packing=st.text_input('PACKING PER CONTAINER',key=f'packing')
        v.append(packing)
        number_container=st.text_input('NO OF CONTAINERS',key=f'no_containers')
        v.append(number_container)
        total_qty=st.text_input('TOTAL QUANTITY IN CONTAINER',key=f'total_qty')
        v.append(total_qty)
        submit_button = st.form_submit_button(label="Submit")
        date=st.date_input('Date',key='Date ftr')
        v.append(date.isoformat())
        if submit_button:
            st.write(f"Form submitted at {datetime.now()}!")
            connect_to_gsheet(sheet_name='In Process And Final Testing Report').append_row(v)
            time.sleep(2)
            st.rerun()

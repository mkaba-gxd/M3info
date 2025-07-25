import pandas as pd
from .func import *

use_column_simp = ['SAMPLE_ID','PATIENT_NO','BATCH','DIAGNOSIS_NAME','Institution','Cohort','ANAL_STATUS']
use_column_comp = ['SAMPLE_ID','PATIENT_NO','BATCH','GENDER','BIRTH_DATE','AGE','SAMPLING_DATE','DIAGNOSIS_NAME','OCCURRED_ORGAN','BIOPSY_OR_SURGERY','Clinician','Institution','Cohort','Timepoint','ANAL_STATUS','REPORT_DATE']

def sampleid_query(sid) :
    query = f"""
    SELECT tesh.run_id, concat(tesh.equip_side, tesh.fc_id) AS sub_name, gp.SAMPLE_ID, gp.PATIENT_NO, gp.GENDER, gp.BIRTH_DATE, gp.AGE, gp.SAMPLING_DATE, gp.PI_NAME AS Clinician, gp.OCCURRED_ORGAN, gp.DIAGNOSIS_NAME, gp.PRJ_TYPE, tol.cohort AS Cohort, tol.timepoint AS Timepoint, tpm.pi_comp AS Institution, tol.biopsy_or_surgery AS BIOPSY_OR_SURGERY, ghl.ANAL_STATUS, ghl.REPORT_DATE
    FROM gxd.tb_expr_seq_header tesh
    INNER JOIN gxd.gc_qc_sample gqs
    ON tesh.run_id = gqs.run_id
    INNER JOIN gxd.gc_project gp
    ON gqs.SAMPLE_ID = gp.SAMPLE_ID
    RIGHT OUTER JOIN gxd.gc_history_log ghl
    ON gqs.SAMPLE_ID = ghl.SAMPLE_ID
    AND ghl.idx = (SELECT MAX(idx) FROM gc_history_log WHERE SAMPLE_ID = gqs.SAMPLE_ID)
    INNER JOIN gxd.tb_order_line tol
    ON tol.sample_id = gp.SAMPLE_ID
    LEFT OUTER JOIN gxd.tb_polaris_mst tpm
    ON tpm.patient_id = gp.PATIENT_NO
    WHERE gp.SAMPLE_ID = '{sid}'
    """
    return query

def patientid_query(pid) :

    query = f"""
    SELECT tesh.run_id, concat(tesh.equip_side, tesh.fc_id) AS sub_name, gp.SAMPLE_ID, gp.PATIENT_NO, gp.GENDER, gp.BIRTH_DATE, gp.AGE, gp.SAMPLING_DATE, gp.PI_NAME AS Clinician, gp.OCCURRED_ORGAN, gp.DIAGNOSIS_NAME, gp.PRJ_TYPE, tol.cohort AS Cohort, tol.timepoint AS Timepoint, tpm.pi_comp AS Institution, tol.biopsy_or_surgery AS BIOPSY_OR_SURGERY, ghl.ANAL_STATUS, ghl.REPORT_DATE
    FROM gxd.tb_expr_seq_header tesh
    INNER JOIN gxd.gc_qc_sample gqs
    ON tesh.run_id = gqs.run_id
    INNER JOIN gxd.gc_project gp
    ON gqs.SAMPLE_ID = gp.SAMPLE_ID
    INNER JOIN gxd.gc_history_log ghl
    ON gqs.SAMPLE_ID = ghl.SAMPLE_ID
    AND ghl.idx = (SELECT MAX(idx) FROM gc_history_log WHERE SAMPLE_ID = gqs.SAMPLE_ID)
    INNER JOIN gxd.tb_order_line tol
    ON tol.sample_id = gp.SAMPLE_ID
    LEFT OUTER JOIN gxd.tb_polaris_mst tpm
    ON tpm.patient_id = gp.PATIENT_NO
    WHERE gp.PATIENT_NO = '{pid}'
    """
    return query

def run_info(args) :

    sid = args.sample_id
    pid = args.patient_id
    verbose = args.verbose
    directory = args.directory

    if sid is None and pid is None :
        init("Please specify either the specimen ID or patient ID.")
    elif sid is not None and pid is not None :
        init("Please specify either the specimen ID or patient ID.")

    if sid is not None :
        df_info = getinfo(sampleid_query(sid))
    else :
        df_info = getinfo(patientid_query(pid))

    if df_info.shape[0] == 0 :
        init("No matching data found.")

    df_info['PRJ_TYPE'] = df_info['PRJ_TYPE'].str.replace('EWES',"eWES")
    df_info['SAMPLING_DATE'] = df_info['SAMPLING_DATE'].dt.date
    df_info['REPORT_DATE'] = pd.to_datetime(df_info['REPORT_DATE'], errors='coerce')
    df_info['REPORT_DATE'] = df_info['REPORT_DATE'].dt.date
    df_info['BATCH'] = [ Search_fcDir(df_info['sub_name'][i], Path(os.path.join(directory, df_info['PRJ_TYPE'][i]))) for i in range(df_info.shape[0]) ]

    if verbose :
        df_info = df_info[use_column_comp]
    else :
        df_info = df_info[use_column_simp]

    print(df_info.T)


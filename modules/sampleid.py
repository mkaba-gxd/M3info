import pandas as pd
from .func import *

use_column = ['SAMPLE_ID','PATIENT_NO','BATCH','GENDER','BIRTH_DATE','AGE','SAMPLING_DATE','DIAGNOSIS_NAME','OCCURRED_ORGAN','BIOPSY_OR_SURGERY','Clinician','Institution','Cohort','Timepoint']

def sampleid_query(sid) :
    query = f"""
    SELECT tesh.run_id, concat(tesh.equip_side, tesh.fc_id) AS sub_name, gp.SAMPLE_ID, gp.PATIENT_NO, gp.GENDER, gp.BIRTH_DATE, gp.AGE, gp.SAMPLING_DATE, gp.PI_NAME AS Clinician, gp.OCCURRED_ORGAN, gp.DIAGNOSIS_NAME, gp.PRJ_TYPE, tol.cohort AS Cohort, tol.timepoint AS Timepoint, tpm.pi_comp AS Institution, tol.biopsy_or_surgery AS BIOPSY_OR_SURGERY
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
    INNER JOIN gxd.tb_polaris_mst tpm
    ON tpm.patient_id = gp.PATIENT_NO
    WHERE gp.SAMPLE_ID = '{sid}'
    """
    return query


def run_sampleid(args):

    sid = args.sample_id
    directory = args.directory

    df_info = getinfo(sampleid_query(sid))
    if df_info.shape[0] == 0 :
        init("No matching data found.")
    elif df_info.shape[0] > 1 :
        init("Multiple pertinent data.")

    df_info['PRJ_TYPE'] = df_info['PRJ_TYPE'].str.replace('EWES',"eWES")
    df_info['SAMPLING_DATE'] = df_info['SAMPLING_DATE'].dt.date
    df_info['BATCH'] = Search_fcDir(df_info.sub_name[0], Path(os.path.join(directory, df_info['PRJ_TYPE'][0])))

    print(df_info[use_column].T)

